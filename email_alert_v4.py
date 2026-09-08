#!/usr/bin/env python3
"""Email transport for V4 BUY_READY / REENTRY_READY signals. No second trading filter."""
from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

import email_alert as base

V4_JSON = Path('v4_watch.json')
STATE = Path('alert_state_v4.json')
GLOBAL_COOLDOWN = 30 * 60
MARKET_COOLDOWN = 4 * 3600
MAX_SNAPSHOT_AGE = 15 * 60


def n(x, default=None):
    try: return float(x)
    except Exception: return default


def load(path, default):
    try: return json.loads(path.read_text(encoding='utf-8'))
    except Exception: return default


def save(path, data):
    from research.common import atomic_json
    atomic_json(path, data)


def ts(v):
    try: return datetime.fromisoformat(str(v).replace('Z','+00:00')).timestamp()
    except Exception: return None


def fmt(x, d=2):
    v=n(x)
    return 'n/d' if v is None else f'{v:.{d}f}'


def price(x):
    v=n(x)
    if v is None: return 'n/d'
    d=2 if v>=100 else 4 if v>=1 else 6 if v>=0.01 else 8
    return f'{v:.{d}f} €'


def select_events(payload, state, now):
    """A continuous identical signal is sent once, including REENTRY_READY.

    Observations persist even on empty scans. Delivery markers only change after
    SMTP succeeds. A failed delivery therefore remains retryable.
    """
    import copy
    state = copy.deepcopy(state)
    state.setdefault('markets', {})
    generated = ts(payload.get('generated_at_utc'))
    if generated is None or not -30 <= now - generated <= MAX_SNAPSHOT_AGE:
        return [], state
    eligible = {r['market']: r for r in payload.get('watch', [])
                if r.get('market') and r.get('buy_ready')
                and r.get('action_status') in {'BUY_READY', 'REENTRY_READY'}
                and r.get('data_quality', {}).get('ok', True)}
    events = []
    for m in sorted(set(state['markets']) | set(eligible)):
        previous = state['markets'].setdefault(m, {})
        row = eligible.get(m)
        was_active = previous.get('active', previous.get('status') in {'BUY_READY', 'REENTRY_READY'})
        if row is None:
            previous['active'] = False
            continue
        if not was_active:
            previous['episode'] = int(previous.get('episode', 0)) + 1
        previous['active'] = True
        episode = int(previous.get('episode', 0))
        last = n(previous.get('last_sent_ts'))
        new_episode = last is None or episode != previous.get('sent_episode', 0)
        improved = (n(row.get('opportunity_score'), 0) - n(previous.get('opportunity'), 0) >= .7
                    and n(row.get('entry_score'), 0) - n(previous.get('entry'), 0) >= .5)
        if (new_episode or improved) and (last is None or now - last >= MARKET_COOLDOWN):
            events.append(row)
    last_global = n(state.get('last_global_sent_ts'))
    if last_global is not None and now - last_global < GLOBAL_COOLDOWN:
        return [], state
    events.sort(key=lambda r: (n(r.get('opportunity_score'), 0), n(r.get('entry_score'), 0)), reverse=True)
    return events[:1], state


def main() -> int:
    user=os.getenv('ALERT_GMAIL_USER','').strip(); recipient=os.getenv('ALERT_EMAIL_TO','').strip(); password=os.getenv('GMAIL_APP_PASSWORD','').strip().replace(' ','')
    test=os.getenv('ALERT_TEST_MODE','').lower() in {'1','true','yes','on'}
    if not user or not recipient or not password:
        print('EMAIL_V4_CONFIG_MISSING'); return 0
    payload=load(V4_JSON,{})
    generated=ts(payload.get('generated_at_utc'))
    if generated is None or not -30 <= time.time()-generated <= MAX_SNAPSHOT_AGE:
        print('EMAIL_V4_SKIPPED stale'); return 0
    state=load(STATE,{'markets':{}})
    state.setdefault('markets',{})
    now=time.time()
    last_global=n(state.get('last_global_sent_ts'))
    candidates=[r for r in payload.get('watch',[]) if isinstance(r,dict) and r.get('buy_ready') and r.get('action_status') in {'BUY_READY','REENTRY_READY'}]
    candidates.sort(key=lambda r:(n(r.get('opportunity_score'),0),n(r.get('entry_score'),0)), reverse=True)
    selected=[]
    if test:
        selected=candidates[:1] or [r for r in payload.get('watch',[])[:1] if isinstance(r,dict)]
    else:
        selected,state=select_events(payload,state,now)
        save(STATE,state)
    if not selected:
        print('EMAIL_V4_SKIPPED no_new_buy_ready'); return 0

    r=selected[0]; m=r.get('market'); plan=r.get('trade_plan') or {}; p=r.get('trend_profile') or {}
    try:
        local=datetime.fromisoformat(str(payload.get('generated_at_utc')).replace('Z','+00:00')).astimezone(ZoneInfo('Europe/Paris')).strftime('%d/%m/%Y %H:%M:%S')
    except Exception: local=str(payload.get('generated_at_utc'))
    subject=(f"[TEST] Bitvavo V4 — {m}" if test else f"🚨 Bitvavo V4 {r.get('action_status')} — {m}")
    body='\n'.join([
        'BITVAVO SCAN V4 — OPPORTUNITY + ENTRY',
        f'Snapshot: {local} (Paris)', '',
        f"{m} — {r.get('action_status')} — entry mode {r.get('entry_mode')}",
        f"Opportunity: {fmt(r.get('opportunity_score'))}/10 | Entry: {fmt(r.get('entry_score'))}/10 | Trend: {fmt(r.get('trend_score'))}/10 | confirms: {r.get('confirm_count')}",
        f"Price: {price(r.get('last'))} | 24h {fmt(r.get('change_24h_pct'))}% | 7d {fmt(p.get('ret7d'))}% | 30d {fmt(p.get('ret30d'))}%",
        f"Relative vs BTC: 7d {fmt(p.get('rs_btc_7d'))}% | 30d {fmt(p.get('rs_btc_30d'))}%",
        f"Since first V4 signal: {fmt(r.get('since_first_signal_pct'))}%",
        f"Flags: {', '.join(r.get('risk_flags') or []) or 'none'}",
        f"Sizing guide: {fmt(plan.get('suggested_stake_eur'),0)} € | structural stop guide {fmt(plan.get('structural_stop_guide_pct'))}% | risk ~{fmt(plan.get('risk_eur_at_guide'))} €",
        f"TP framework: TP1 +{fmt(plan.get('tp1_pct'))}% | runner target +{fmt(plan.get('runner_target_pct'))}% | keep {fmt(plan.get('runner_keep_pct'),0)}% runner",
        '',
        'The email is an execution alert, not an automatic order. Validate the live price/book before placing an order.'
    ])
    base.send_email(user,password,recipient,subject,body)
    if not test:
        state['last_global_sent_ts']=now
        previous=state['markets'].get(str(m),{})
        state['markets'][str(m)]={**previous,'last_sent_ts':now,'sent_episode':previous.get('episode',0),'opportunity':r.get('opportunity_score'),'entry':r.get('entry_score'),'price':r.get('last'),'status':r.get('action_status')}
        state['updated_at_utc']=datetime.now(timezone.utc).isoformat(); save(STATE,state)
    print(f"EMAIL_V4_SENT recipient={recipient} market={m} test={test}")
    return 0


if __name__=='__main__':
    try: raise SystemExit(main())
    except Exception as exc:
        print(f'EMAIL_V4_ERROR {exc}', file=sys.stderr); raise

"""Append-only compressed scan journals and an ephemeral indexed evaluation DB.

The journals are authoritative and committed before notifications. The SQLite
index can always be rebuilt; it is never a required Actions cache or artifact.
"""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path

from research.common import atomic_json, read_json


def save_scan(root, scan):
    path = Path(root) / scan['scan_at_utc'][:10] / (scan['scan_id'] + '.json.gz')
    if path.exists():
        if read_json(path) != scan:
            raise ValueError('scan_id_collision')
        return path
    atomic_json(path, scan)
    return path


def connect(path=':memory:'):
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    db.executescript('''
        CREATE TABLE IF NOT EXISTS scans(id TEXT PRIMARY KEY, ts REAL, policy TEXT, source TEXT);
        CREATE TABLE IF NOT EXISTS observations(scan_id TEXT, market TEXT, ts REAL, price REAL,
            detected INTEGER, buy INTEGER, decision TEXT, payload TEXT,
            PRIMARY KEY(scan_id, market));
        CREATE INDEX IF NOT EXISTS observation_market_time ON observations(market, ts);
        CREATE TABLE IF NOT EXISTS candles(market TEXT, t INTEGER, o REAL, h REAL, l REAL, c REAL,
            v REAL, PRIMARY KEY(market,t));
    ''')
    return db


def ingest(db, scan):
    sid, ts = scan['scan_id'], scan['scan_ts']
    if db.execute('SELECT 1 FROM scans WHERE id=?', (sid,)).fetchone():
        return
    with db:
        db.execute('INSERT INTO scans VALUES (?,?,?,?)', (sid, ts, scan['policy'], scan.get('source', 'live')))
        for obs in scan['observations']:
            baseline = obs.get('baseline') or {}
            action = baseline.get('action_status', 'UNOBSERVED')
            detected = action in {'WATCH', 'ENTRY_WINDOW', 'BUY_READY', 'REENTRY_READY'}
            db.execute('INSERT INTO observations VALUES (?,?,?,?,?,?,?,?)',
                (sid, obs['market'], ts, obs.get('price_eur'), detected, int(bool(baseline.get('buy_ready'))),
                 obs['decision'], json.dumps(obs, separators=(',', ':'), allow_nan=False)))
        for market, candles in scan.get('candles_5m', {}).items():
            for c in candles:
                # Only CLOSED candles, validated by features.closed_candles.
                # First observation wins: an exchange revision must not rewrite
                # already scored outcomes silently.
                db.execute('INSERT OR IGNORE INTO candles VALUES (?,?,?,?,?,?,?)',
                           (market, c['t'], c['o'], c['h'], c['l'], c['c'], c['v']))


def rebuild(root, db):
    for path in sorted(Path(root).glob('*/*.json.gz')):
        ingest(db, read_json(path))
    return db


def new_candles(db, candles):
    """Store first-seen bars once; never drop a previously unseen late bar."""
    result = {}
    for market, rows in candles.items():
        known = {r[0] for r in db.execute('SELECT t FROM candles WHERE market=?', (market,))}
        result[market] = [r for r in rows if r['t'] not in known]
    return result


def recurrent(db, market, now, current_category, window=7200):
    rows = db.execute('SELECT scan_id,ts,payload FROM observations WHERE market=? AND ts>=? AND ts<? ORDER BY ts',
                      (market, now - window, now)).fetchall()
    # Repeated executions of one decision candle count once, not as new evidence.
    buckets = {}
    for row in rows:
        obs = json.loads(row['payload'])
        if obs.get('category') in {'PRE-IGNITION', 'IGNITION'}:
            buckets[int(row['ts'] // 900)] = {'at': row['ts'], 'category': obs['category']}
    if current_category in {'PRE-IGNITION', 'IGNITION'}:
        buckets[int(now // 900)] = {'at': now, 'category': current_category}
    events = [buckets[k] for k in sorted(buckets)]
    return {'distinct_15m_periods': len(events), 'recurrent': len(events) >= 2,
            'sequence': events, 'affects_baseline': False}

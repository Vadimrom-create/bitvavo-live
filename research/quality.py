"""Versioned data capabilities; neither a score nor a global veto policy."""
from research.common import finite, freshness, INTERVAL_MS, timestamp
from research.input_contract import source_close_bound
from research.policies import CORRECTED_DATA

QUALITY_POLICY = 'CAPABILITIES_V1'
SPREAD_FLAGS = {'WIDE_SPREAD_RISK':1,'WIDE_SPREAD':2,'VERY_WIDE_SPREAD_RISK':3}
EXECUTION_WICK_REASONS = {'SPREAD_UNSUITABLE','LOW_LIQUIDITY','ILLIQUID'}


def spread_diagnostic(flags, value):
    raw = sorted(set(flags)&set(SPREAD_FLAGS))
    value = finite(value)
    severity = max([SPREAD_FLAGS[f] for f in raw] + [2 if value is not None and value > .8 else 1 if value is not None and value > .4 else 0])
    known = value is not None and value >= 0
    return {'severity':severity,'value_pct':value,'raw_flags':raw,'measured':known,
            'execution_allowed':known and severity==0}


def wick_diagnostic(payload):
    status = payload.get('status', 'UNAVAILABLE')
    reasons = sorted(set(payload.get('reasons') or []))
    execution = [r for r in reasons if r in EXECUTION_WICK_REASONS]
    price = [r for r in reasons if r == 'REPEATED_DIRECTIONLESS_REJECTIONS']
    return {'raw_status':status,'raw_reasons':reasons,'execution_reasons':execution,'price_reasons':price,
            'price_confirmation_required':bool(price) or status in {'POTENTIALLY_EXPLOITABLE','WAIT_FOR_DIRECTION'},
            'known':status in {'NORMAL','POTENTIALLY_EXPLOITABLE','WAIT_FOR_DIRECTION','DANGEROUS_STRUCTURE'}}


def assess(obs, now):
    baseline = obs.get('baseline') or {}
    flags = set(baseline.get('risk_flags') or []) | set(obs.get('exclusions') or [])
    profile = baseline.get('trend_profile') or {}
    sources = obs.get('input_sources') or {}
    features = obs.get('features') or {}
    caps = {}
    def cap(name, reasons, refs):
        caps[name] = {'available':not reasons,'reasons':sorted(set(reasons)), 'source_ids':sorted(set(r for r in refs if r))}
    def timeframe(interval):
        f = features.get(interval) or {}
        r = sources.get(interval) or {}
        reasons = []
        if not f.get('valid'):
            reasons.append('UNUSABLE_'+interval.upper())
        try:
            close = f['last_closed_start_ms'] + INTERVAL_MS[interval]
            if not r.get('response_id') or close > source_close_bound(r)*1000 or timestamp(r['retrieved_at_utc']) > now:
                reasons.append('UNVERIFIED_SOURCE_'+interval.upper())
            reasons += freshness(now=now, retrieved=r.get('retrieved_at_utc'), candle_start_ms=f.get('last_closed_start_ms'), interval=interval)['reasons']
        except (KeyError, TypeError, ValueError):
            reasons.append('MISSING_SOURCE_'+interval.upper())
        return reasons, [r.get('response_id')]
    structural, refs = timeframe('15m')
    if obs.get('data_policy') != CORRECTED_DATA:
        structural.append('STRUCTURAL_SOURCE_CLOSURE_UNVERIFIED')
    if not baseline or baseline.get('market') != obs.get('market'):
        structural.append('MARKET_IDENTITY_UNVERIFIED')
    if finite(obs.get('price_eur'),0) <= 0:
        structural.append('REFERENCE_PRICE_UNAVAILABLE')
    acquired = finite(profile.get('updated_ts'))
    if acquired is None or not -30 <= now-acquired <= 10800 or not profile.get('response_id'):
        structural.append('DAILY_PROFILE_UNVERIFIED_OR_STALE')
    dependencies = profile.get('dependencies') or {}
    refs += [r.get('response_id') for r in dependencies.values() if isinstance(r, dict)]
    references_fresh = all(isinstance(dependencies.get(m), dict) and dependencies[m].get('valid') is True
                           and dependencies[m].get('response_id')
                           and finite(dependencies[m].get('acquired_at')) is not None
                           and -30 <= now-finite(dependencies[m]['acquired_at']) <= 10800 for m in ('BTC-EUR','ETH-EUR'))
    if profile.get('dependencies_fresh') is not True or not references_fresh:
        structural.append('DAILY_DEPENDENCIES_UNVERIFIED_OR_STALE')
    refs += [profile.get('response_id')]
    cap('structure',structural,refs)
    entry_reasons, entry_refs = timeframe('5m')
    entry_reasons += timeframe('15m')[0]
    score = finite(baseline.get('entry_score'))
    if score is None or flags & {'NOT_ENTRY_ENRICHED','ENTRY_INPUTS_UNAVAILABLE'}:
        entry_reasons.append('ENTRY_NOT_MEASURED')
    cap('entry',entry_reasons,entry_refs+refs)
    spread = spread_diagnostic(flags,baseline.get('spread_pct'))
    wick = wick_diagnostic(obs.get('wick_setup') or {})
    execution = []
    if not spread['execution_allowed']: execution.append('SPREAD_NOT_EXECUTABLE')
    if finite(baseline.get('quote_volume_24h_eur'),0) < 30000 or flags & {'LOW_LIQUIDITY','ILLIQUID'}:
        execution.append('LIQUIDITY_NOT_EXECUTABLE')
    if wick['price_confirmation_required']: execution.append('PRICE_CONFIRMATION_REQUIRED')
    cap('immediate',structural+entry_reasons+execution,refs+entry_refs)
    passive = list(structural)
    if finite((features.get('15m') or {}).get('support_eur'),0) <= 0:
        passive.append('PASSIVE_REFERENCE_UNAVAILABLE')
    cap('passive',passive,refs)  # Inactive planning capability, not an order authorization.
    cap('retrace',structural,refs)
    cap('outcome',[] if finite(obs.get('price_eur'),0)>0 else ['MISSING_REFERENCE_PRICE'],refs)
    return {'schema_version':1,'quality_policy':QUALITY_POLICY,'structure_state':'VALID' if not structural else 'UNVERIFIABLE',
            'entry_status':'MEASURED' if not entry_reasons else 'UNKNOWN',
            'entry_score_measured':score if not entry_reasons else None,
            'capabilities':caps,'spread':spread,'wick':wick,'execution_constraints':execution,
            'raw_flags':sorted(flags),'future_outcome_status':'NOT_KNOWN_AT_DECISION'}

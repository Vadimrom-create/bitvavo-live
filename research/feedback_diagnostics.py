"""Versioned diagnostic overlay. Never redefines historical V4 events or scores."""
import copy
from research.common import finite, freshness, INTERVAL_MS, timestamp
from research.input_contract import source_close_bound
from research.feedback_loop import acceleration_signal, BASELINE_SIGNAL_STATES
from research.policies import CORRECTED_DATA

POLICY = 'FEEDBACK_CAUSAL_V1_SHADOW'


def acceleration(obs, cutoff):
    """Candle capability only: neither order book nor V4 profile is required."""
    candidate = copy.deepcopy(obs)
    reasons = []
    if obs.get('data_policy') != CORRECTED_DATA:
        reasons.append('SOURCE_CLOSURE_UNVERIFIED')
    for interval in ('5m', '15m'):
        f = (obs.get('features') or {}).get(interval) or {}
        source = (obs.get('input_sources') or {}).get(interval) or {}
        try:
            start = f['last_closed_start_ms']
            if not f.get('valid') or not source.get('response_id'):
                reasons.append('UNUSABLE_' + interval)
            if start + INTERVAL_MS[interval] > source_close_bound(source) * 1000:
                reasons.append('SOURCE_OPEN_CANDLE_' + interval)
            if timestamp(source['retrieved_at_utc']) > cutoff:
                reasons.append('SOURCE_AFTER_CUTOFF_' + interval)
            reasons.extend(freshness(now=cutoff, retrieved=source['retrieved_at_utc'],
                                     candle_start_ms=start, interval=interval)['reasons'])
            keys = ('return_4bar_pct', 'relative_volume') + (
                ('momentum_acceleration_pp', 'volume_4_vs_prev4', 'distance_to_breakout_pct')
                if interval == '5m' else ('return_1bar_pct',))
            if any(finite(f.get(k)) is None for k in keys):
                reasons.append('NONFINITE_OR_MISSING_FEATURE_' + interval)
        except (KeyError, TypeError, ValueError, OverflowError):
            reasons.append('MISSING_SOURCE_' + interval)
    if reasons:
        candidate['features'] = {'5m': {'valid': False, 'reasons': sorted(set(reasons))}}
    return acceleration_signal(candidate)


def layers(obs, acceleration_result, baseline_ready_at, feedback_ready_at, decision=None, decision_ready_at=None):
    """Availability is recorded separately from reconstructed signal content."""
    baseline = obs.get('baseline') or {}
    detected = baseline.get('action_status') in BASELINE_SIGNAL_STATES
    return {
        'market': obs['market'], 'diagnostic_policy': POLICY,
        'reference_event_policy': 'HISTORY_CONTINUITY_V2_UNCHANGED',
        'V4': {'detected': detected, 'provenance': 'RECORDED_SCAN', 'available_at': baseline_ready_at},
        'ACCELERATION': {'detected': acceleration_result['detected'],
                         'state': acceleration_result['state'], 'provenance': 'RECONSTRUCTED_FROM_SCAN',
                         'available_at': feedback_ready_at, 'historical_availability': 'UNKNOWN'},
        'DL1': {'detected': bool(decision.get('bucket')) if decision is not None else None,
                'provenance': 'RECORDED_SHADOW' if decision_ready_at else 'RECONSTRUCTED' if decision is not None else 'UNKNOWN',
                'available_at': decision_ready_at},
        'diagnostic_layer': 'DATA' if acceleration_result['state'] == 'DATA_UNAVAILABLE' else
            'SCANNER_COVERAGE' if not baseline else 'INTERPRETATION' if detected else 'SCANNER_SCORING',
        'attribution': 'DESCRIPTIVE_NOT_CAUSAL', 'actionability': 'WATCH_ONLY', 'alert_eligible': False,
    }

"""Append-only compressed scan journals and an ephemeral indexed evaluation DB.

The journals are authoritative and committed before notifications. The SQLite
index can always be rebuilt; it is never a required Actions cache or artifact.
"""
from __future__ import annotations

import json
import hashlib
import time
import sqlite3
from pathlib import Path

from research.common import atomic_json, read_json
from research.input_contract import digest
from research.policies import LEGACY_DATA


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
        CREATE TABLE IF NOT EXISTS index_meta(key TEXT PRIMARY KEY, value TEXT);
        CREATE TABLE IF NOT EXISTS journal_integrity(id TEXT PRIMARY KEY, sha256 TEXT, data_policy TEXT, bytes_sha256 TEXT);
        CREATE TABLE IF NOT EXISTS journal_files(path TEXT PRIMARY KEY, sha256 TEXT);
        CREATE TABLE IF NOT EXISTS candle_source(market TEXT, t INTEGER, scan_ts REAL, scan_id TEXT, PRIMARY KEY(market,t));
        CREATE TABLE IF NOT EXISTS candles(market TEXT, t INTEGER, o REAL, h REAL, l REAL, c REAL,
            v REAL, PRIMARY KEY(market,t));
    ''')
    return db


def ingest(db, scan, bytes_sha256=None):
    sid, ts = scan['scan_id'], scan['scan_ts']
    data_policy = scan.get('data_policy', LEGACY_DATA)
    sha = digest(scan)
    old = db.execute('SELECT * FROM journal_integrity WHERE id=?', (sid,)).fetchone()
    if old:
        if old['sha256'] != sha or (bytes_sha256 and old['bytes_sha256'] and bytes_sha256 != old['bytes_sha256']):
            raise ValueError('SCAN_ID_COLLISION')
        return
    policy = db.execute("SELECT value FROM index_meta WHERE key='data_policy'").fetchone()
    if policy and policy[0] != data_policy:
        raise ValueError('INDEX_DATA_POLICY_MISMATCH')
    if db.execute('SELECT 1 FROM scans WHERE id=?', (sid,)).fetchone():
        raise sqlite3.DatabaseError('INDEX_REBUILD_REQUIRED')
    with db:
        db.execute("INSERT OR IGNORE INTO index_meta VALUES ('data_policy',?)", (data_policy,))
        db.execute('INSERT INTO scans VALUES (?,?,?,?)', (sid, ts, scan['policy'], scan.get('source', 'live')))
        db.execute('INSERT INTO journal_integrity VALUES (?,?,?,?)', (sid, sha, data_policy, bytes_sha256))
        for obs in scan['observations']:
            baseline = obs.get('baseline') or {}
            action = baseline.get('action_status', 'UNOBSERVED')
            detected = action in {'WATCH', 'ENTRY_WINDOW', 'BUY_READY', 'REENTRY_READY'}
            db.execute('INSERT INTO observations VALUES (?,?,?,?,?,?,?,?)',
                (sid, obs['market'], ts, obs.get('price_eur'), detected, int(bool(baseline.get('buy_ready'))),
                 obs['decision'], json.dumps(obs, separators=(',', ':'), allow_nan=False)))
        for market, candles in scan.get('candles_5m', {}).items():
            for c in candles:
                old_source = db.execute('SELECT scan_ts,scan_id FROM candle_source WHERE market=? AND t=?', (market,c['t'])).fetchone()
                # Canonical recorded first observation, independent of arrival in this disposable index.
                if old_source and tuple(old_source) <= (ts,sid):
                    continue
                db.execute('INSERT OR REPLACE INTO candles VALUES (?,?,?,?,?,?,?)',
                           (market, c['t'], c['o'], c['h'], c['l'], c['c'], c['v']))
                db.execute('INSERT OR REPLACE INTO candle_source VALUES (?,?,?,?)', (market,c['t'],ts,sid))


def refresh_index(root, db):
    paths = sorted(Path(root).glob('*/*.json.gz'))
    present = {str(p.relative_to(root)) for p in paths}
    indexed = {r[0] for r in db.execute('SELECT path FROM journal_files')}
    if indexed - present:
        raise ValueError('IMMUTABLE_JOURNAL_REMOVED')
    for path in paths:
        key = str(path.relative_to(root))
        sha = hashlib.sha256(path.read_bytes()).hexdigest()
        previous = db.execute('SELECT sha256 FROM journal_files WHERE path=?', (key,)).fetchone()
        if previous:
            if previous[0] != sha:
                raise ValueError('IMMUTABLE_JOURNAL_CHANGED')
            continue
        ingest(db, read_json(path), sha)
        with db:
            db.execute('INSERT INTO journal_files VALUES (?,?)', (key,sha))
    return db


def rebuild(root, db):
    return refresh_index(root, db)


def open_index(path, root):
    """Only a corrupt derived index is disposable. Source divergence still raises."""
    path = Path(path)
    path.parent.mkdir(parents=True,exist_ok=True)
    db = None
    try:
        db = connect(path)
        if db.execute('PRAGMA quick_check').fetchone()[0] != 'ok':
            raise sqlite3.DatabaseError('CORRUPT_INDEX')
        if db.execute('SELECT COUNT(*) FROM scans').fetchone()[0] != db.execute('SELECT COUNT(*) FROM journal_integrity').fetchone()[0]:
            raise sqlite3.DatabaseError('UNVERSIONED_INDEX')
        return refresh_index(root, db)
    except sqlite3.DatabaseError:
        if db is not None: db.close()
        if path.exists(): path.rename(path.with_name(path.name+'.corrupt-'+str(time.time_ns())))
        print('DERIVED_INDEX_REBUILT_FROM_IMMUTABLE_JOURNALS')
        return refresh_index(root, connect(path))


def new_candles(db, candles):
    """Store first-seen bars once; never drop a previously unseen late bar."""
    result = {}
    for market, rows in candles.items():
        known = {r[0] for r in db.execute('SELECT t FROM candles WHERE market=?', (market,))}
        result[market] = [r for r in rows if r['t'] not in known]
    return result


def recurrent(db, market, now, current_category, window=7200):
    rows = db.execute('SELECT scan_id,ts,payload FROM observations WHERE market=? AND ts>=? AND ts<? ORDER BY ts,scan_id',
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

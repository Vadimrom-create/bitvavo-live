"""Host-local public Bitvavo quota. No credentials, policy or market data.

Atomic SQLite reservations coordinate threads AND processes using the same path.
Monotonic timestamps are shared on one host; the boot ID prevents reboot reuse.
The 61-second window includes a one-second dispatch margin. Headers can only
restrict this independent ledger, never replenish it.
"""
from contextlib import contextmanager
import math
import os
from pathlib import Path
import sqlite3
import tempfile
import threading
import time
from email.utils import parsedate_to_datetime

LIMIT = 750
WINDOW = 61.0
_LOCAL_LOCKS = {}
_LOCAL_LOCKS_GUARD = threading.Lock()


def weight(path, params=None):
    if path == '/ticker/24h':
        return 1 if (params or {}).get('market') else 25
    return 5 if path.endswith('/trades') else 1


def default_path():
    root = Path(tempfile.gettempdir()) / ('bitvavo-public-budget-' + str(os.getuid()))
    root.mkdir(mode=0o700, exist_ok=True)
    boot = Path('/proc/sys/kernel/random/boot_id').read_text().strip()
    return root / (boot + '.sqlite3')


class WeightedBudget:
    def __init__(self, path=None, *, clock=None, sleeper=None):
        self.path = str(path if path is not None else default_path())
        with _LOCAL_LOCKS_GUARD:
            self._local_lock = _LOCAL_LOCKS.setdefault(os.path.abspath(self.path), threading.RLock())
        self.clock = clock or time.monotonic
        self.sleep = sleeper or time.sleep
        with self.connect() as db:
            db.execute('CREATE TABLE IF NOT EXISTS reservations (at REAL NOT NULL, weight INTEGER NOT NULL)')
            db.execute('CREATE INDEX IF NOT EXISTS reservations_at ON reservations(at)')
            db.execute('CREATE TABLE IF NOT EXISTS state (id INTEGER PRIMARY KEY, pause REAL NOT NULL)')
            db.execute('INSERT OR IGNORE INTO state VALUES (1,0)')

    @contextmanager
    def connect(self):
        # SQLite arbitrates processes. Serialize same-process threads first so
        # many connections cannot starve one another on a slow CI filesystem.
        # No quota sleep or network operation occurs inside this short lock.
        with self._local_lock:
            db = sqlite3.connect(self.path, timeout=5)
            try:
                with db:
                    yield db
            finally:
                db.close()

    def reserve(self, points, deadline=None):
        """Charge every attempted request, including failed requests and retries."""
        if not isinstance(points, int) or not 0 < points <= LIMIT:
            raise ValueError('INVALID_API_WEIGHT')
        began = self.clock()
        while True:
            with self.connect() as db:
                db.execute('BEGIN IMMEDIATE')
                now = self.clock()
                if deadline is not None and now >= deadline:
                    raise RuntimeError('API_BUDGET_DEADLINE')
                db.execute('DELETE FROM reservations WHERE at <= ?', (now-WINDOW,))
                rows = db.execute('SELECT at,weight FROM reservations ORDER BY at').fetchall()
                used = sum(w for _, w in rows)
                ready = max(now, db.execute('SELECT pause FROM state WHERE id=1').fetchone()[0])
                for at, w in rows:
                    if used + points <= LIMIT:
                        break
                    used -= w
                    ready = max(ready, at+WINDOW)
                if ready <= now:
                    db.execute('INSERT INTO reservations VALUES (?,?)', (now, points))
                    return now-began
                if deadline is not None and ready >= deadline:
                    raise RuntimeError('API_BUDGET_DEADLINE')
            # Never sleep with the transaction held. Recheck after wake-up: other
            # consumers may have reserved the capacity or received a 429 meanwhile.
            self.sleep(min(ready-now, 1.0))

    def pause(self, seconds):
        if math.isfinite(seconds) and seconds > 0:
            with self.connect() as db:
                db.execute('BEGIN IMMEDIATE')
                db.execute('UPDATE state SET pause=MAX(pause,?) WHERE id=1', (self.clock()+seconds,))

    def observe(self, headers, status=200, now=None):
        h = {str(k).lower(): v for k, v in (headers or {}).items()}
        now = time.time() if now is None else now
        def number(key):
            try:
                value = float(h[key])
                return value if math.isfinite(value) else None
            except (ValueError, TypeError, KeyError):
                return None
        reset = number('bitvavo-ratelimit-resetat')
        reset_wait = reset/1000-now if reset is not None else None
        if status in (403, 429):
            # Public-IP bans can last 15 minutes. Never turn 429 into rapid retries.
            delay = 900.0
            retry = number('retry-after')
            if retry is None and h.get('retry-after'):
                try: retry = parsedate_to_datetime(h['retry-after']).timestamp()-now
                except (ValueError, TypeError, OverflowError): pass
            for wait in (retry, reset_wait):
                if wait is not None and math.isfinite(wait): delay = max(delay, wait+1)
            self.pause(delay)
            return
        remaining, limit = number('bitvavo-ratelimit-remaining'), number('bitvavo-ratelimit-limit')
        # Reject past/far-future reset headers; non-monotonic increases never grant
        # capacity. A plausible low reading conservatively preserves our reserve.
        if (limit == 1000 and remaining is not None and 0 <= remaining < 250
                and reset_wait is not None and 0 < reset_wait <= 61):
            self.pause(reset_wait+1)

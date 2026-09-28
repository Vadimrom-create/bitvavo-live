"""Verify exported bytes without executing the audit or using the network."""
import hashlib
from pathlib import Path

root = Path(__file__).resolve().parent
count = 0
for line in (root / "CHECKSUMS.sha256").read_text().splitlines():
    expected, relative = line.split("  ", 1)
    path = root / relative
    assert path.is_file(), relative
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    assert actual == expected, f"SHA256 mismatch: {relative}"
    count += 1
print(f"Verified {count} exported files. CHECKSUMS.sha256 itself is anchored by the Git commit.")

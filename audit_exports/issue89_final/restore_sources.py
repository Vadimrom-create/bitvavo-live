"""Restore omitted public archives only; no audit, orders or production writes.

Run in a disposable copy of this export. Requires public GitHub network access.
"""
import argparse
import base64
import hashlib
import json
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent

def verify(data, item):
    blob = b"blob " + str(len(data)).encode() + b"\0" + data
    assert hashlib.sha1(blob).hexdigest() == item["git_blob_sha1"], item["destination"]
    assert hashlib.sha256(data).hexdigest() == item["decoded_sha256"], item["destination"]
    assert len(data) == item["decoded_bytes"], item["destination"]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--include-decision-samples", action="store_true")
    args = parser.parse_args()
    items = json.loads((ROOT / "SOURCE_ARCHIVES.json").read_text())["archives"]
    items = [x for x in items if args.include_decision_samples or "/history/" in x["destination"]]
    for number, item in enumerate(items, 1):
        target = ROOT / item["destination"]
        if target.exists():
            verify(base64.b64decode(target.read_bytes()), item)
            continue
        request = Request(item["url"], headers={"User-Agent": "issue89-audit-export-restore"})
        with urlopen(request, timeout=120) as response:
            data = response.read()
        verify(data, item)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(base64.b64encode(data))
        print(f"{number}/{len(items)} {item['destination']}")
    print(f"Verified {len(items)} immutable public archives.")

if __name__ == "__main__":
    main()

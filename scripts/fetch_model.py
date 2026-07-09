"""Download the MediaPipe pose_landmarker_full model into models/.

Idempotent: skips when the target file already exists. Uses only the stdlib
so it runs without extra dependencies.
"""
from __future__ import annotations

import sys
import urllib.request
from pathlib import Path

MODEL_URL = (
    "https://storage.googleapis.com/mediapipe-models/pose_landmarker/"
    "pose_landmarker_full/float16/1/pose_landmarker_full.task"
)
TARGET = Path(__file__).resolve().parent.parent / "models" / "pose_landmarker_full.task"


def main() -> int:
    if TARGET.exists():
        print(f"[fetch_model] already present: {TARGET}")
        return 0
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    print(f"[fetch_model] downloading {MODEL_URL}")
    print(f"[fetch_model] -> {TARGET}")

    def _report(block_num: int, block_size: int, total: int) -> None:
        if total <= 0:
            return
        done = min(block_num * block_size, total)
        pct = done * 100 // total
        sys.stderr.write(f"\r[fetch_model] {pct:3d}% ({done // 1024} KB)")
        sys.stderr.flush()

    urllib.request.urlretrieve(MODEL_URL, TARGET, _report)
    sys.stderr.write("\n")
    print(f"[fetch_model] done ({TARGET.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

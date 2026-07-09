"""Download a public squat clip and extract frames for the T3 integration test.

Default source is a royalty-free Pixabay squat clip (direct CDN URL, no API
key). Override with --url. After extraction, set the ground-truth rep count
with --ground-truth (or edit tests/fixtures/manifest.json); T3 only runs the
strict count check once ground_truth_count is set.

Usage:
    python scripts/fetch_test_clip.py
    python scripts/fetch_test_clip.py --url <mp4-url> --ground-truth 10
"""
from __future__ import annotations

import argparse
import json
import shutil
import urllib.request
from pathlib import Path

import cv2

HERE = Path(__file__).resolve().parent
CLIP_DIR = HERE.parent / "tests" / "fixtures" / "clip"
MANIFEST = HERE.parent / "tests" / "fixtures" / "manifest.json"

DEFAULT_URL = (
    "https://cdn.pixabay.com/video/2018/09/23/18369-291382852_large.mp4"
)


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    print(f"[fetch_test_clip] downloading {url}")
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
            )
        },
    )
    with urllib.request.urlopen(req) as resp:
        dest.write_bytes(resp.read())
    print(f"[fetch_test_clip] saved {dest} ({dest.stat().st_size // 1024} KB)")


def extract_frames(video: Path, out_dir: Path, max_frames: int = 600, max_width: int = 640) -> int:
    out_dir.mkdir(parents=True, exist_ok=True)
    cap = cv2.VideoCapture(str(video))
    if not cap.isOpened():
        raise RuntimeError(f"cannot open video: {video}")
    fps = cap.get(cv2.CAP_PROP_FPS) or 0.0
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    stride = max(1, round(total / max_frames)) if total else 1
    count = 0
    idx = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if idx % stride == 0:
            h, w = frame.shape[:2]
            if w > max_width:
                scale = max_width / w
                frame = cv2.resize(frame, (max_width, int(h * scale)))
            path = out_dir / f"{count:06d}.png"
            cv2.imwrite(str(path), frame)
            count += 1
        idx += 1
    cap.release()
    print(f"[fetch_test_clip] extracted {count} frames (stride={stride}, max_width={max_width}) @ {fps:.1f} fps")
    return count


def write_manifest(url: str, frame_count: int, ground_truth) -> None:
    MANIFEST.write_text(
        json.dumps(
            {
                "source": "public royalty-free squat clip",
                "url": url,
                "frame_count": frame_count,
                "ground_truth_count": ground_truth,
                "note": (
                    "First-try fixture. Replace ground_truth_count with dual-rater "
                    "labels before claiming accuracy (see evaluation protocol, ADR-0008)."
                ),
            },
            indent=2,
        )
    )
    print(f"[fetch_test_clip] wrote {MANIFEST}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default=DEFAULT_URL)
    ap.add_argument("--ground-truth", type=int, default=None)
    ap.add_argument("--max-frames", type=int, default=600)
    args = ap.parse_args()

    video = CLIP_DIR.parent / "source.mp4"
    if not video.exists():
        download(args.url, video)
    else:
        print(f"[fetch_test_clip] reusing {video}")

    # Clear old frames so stale PNGs don't leak into the run.
    if CLIP_DIR.exists():
        shutil.rmtree(CLIP_DIR)
    n = extract_frames(video, CLIP_DIR, args.max_frames)
    write_manifest(args.url, n, args.ground_truth)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

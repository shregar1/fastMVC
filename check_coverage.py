#!/usr/bin/env python3
"""Run coverage for each package and print percentages."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PACKAGES = [
    ("fastmvc_core", "src/fastmvc_core"),
    ("fastmvc_kafka", "src/fastmvc_kafka"),
    ("fastmvc_channels", "src/fastmvc_channels"),
    ("fastmvc_notifications", "src/fastmvc_notifications"),
    ("fastmvc_webrtc", "src/fastmvc_webrtc"),
    ("fastmvc_dashboards", "src/fastmvc_dashboards"),
]

def main():
    results = []
    for name, cov_src in PACKAGES:
        pkg_dir = ROOT / name
        if not pkg_dir.is_dir():
            results.append((name, None, "no dir"))
            continue
        tests_dir = pkg_dir / "tests"
        if not tests_dir.is_dir():
            results.append((name, None, "no tests"))
            continue
        try:
            r = subprocess.run(
                [sys.executable, "-m", "pytest", "tests/", f"--cov={cov_src}", "--cov-report=term", "--no-cov-on-fail"],
                cwd=str(pkg_dir),
                capture_output=True,
                text=True,
                timeout=120,
            )
            out = r.stdout + r.stderr
            # Parse line like "TOTAL  xxx    yy    zz%"
            pct = None
            for line in out.splitlines():
                if "TOTAL" in line and "%" in line:
                    parts = line.split()
                    for p in parts:
                        if p.endswith("%"):
                            try:
                                pct = float(p.rstrip("%"))
                                break
                            except ValueError:
                                pass
                    break
            results.append((name, pct, "ok" if r.returncode == 0 else "fail"))
        except Exception as e:
            results.append((name, None, str(e)[:30]))
    # Write to file and print
    lines = [
        "Package              Coverage   >=90%",
        "-" * 45,
    ]
    for name, pct, status in results:
        if pct is not None:
            pct_str = f"{pct:.1f}%"
            above = "yes" if pct >= 90 else "NO"
        else:
            pct_str = "N/A"
            above = status
        lines.append(f"{name:<20} {pct_str:>8}   {above}")
    out_path = ROOT / "coverage_summary.txt"
    out_path.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0

if __name__ == "__main__":
    sys.exit(main())

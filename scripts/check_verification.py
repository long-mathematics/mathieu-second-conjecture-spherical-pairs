#!/usr/bin/env python3
"""Run the exact supplementary checks and compare their output to the checked reference."""
from __future__ import annotations
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "verify_calculations.py"
EXPECTED = ROOT / "scripts" / "verification_output.txt"
proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=ROOT, text=True,
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if proc.returncode != 0:
    sys.stderr.write(proc.stderr)
    sys.stdout.write(proc.stdout)
    raise SystemExit(proc.returncode)
actual = proc.stdout.replace("\r\n", "\n")
expected = EXPECTED.read_text().replace("\r\n", "\n")
if actual != expected:
    sys.stderr.write("verification output differs from scripts/verification_output.txt\n")
    sys.stderr.write("--- expected ---\n" + expected)
    sys.stderr.write("--- actual ---\n" + actual)
    raise SystemExit(1)
print("Verification output matches scripts/verification_output.txt.")

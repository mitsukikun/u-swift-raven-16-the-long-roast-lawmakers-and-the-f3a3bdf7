#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (<=320 chars) to /output/entry.txt
and to this entry directory's entry.txt.
"""
import os
from pathlib import Path

ENTRY = "The congressman drafting the bill to license every AI model in the country just emailed his intern a Word file with the subject line: 'please turn this into a PDF'."

def main():
    text = ENTRY.strip()
    assert 1 <= len(text) <= 320, f"entry length {len(text)} out of range"
    assert text.count(".") == 1, "entry must be a single sentence"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    here = Path(__file__).resolve().parent / "entry.txt"
    here.write_text(text, encoding="utf-8")
    print(text)
    print(f"chars: {len(text)}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import argparse, re

def words(s):
    return re.findall(r"[A-Za-z0-9가-힣]+", s.lower())

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--title", required=True)
    p.add_argument("--thumb", default="")
    a = p.parse_args()

    issues = []
    if len(a.title) > 60:
        issues.append("Title may truncate on desktop/search.")
    if len(a.title) > 40:
        issues.append("Check the first 40 characters for mobile clarity.")

    tw = words(a.title)
    hw = words(a.thumb)
    if len(hw) > 3:
        issues.append("Thumbnail text exceeds 3 words.")

    overlap = sorted(set(tw) & set(hw))
    if overlap:
        issues.append("Title/thumbnail repeat words: " + ", ".join(overlap))

    caps = re.findall(r"\b[A-Z]{2,}\b", a.title)
    if len(caps) > 2:
        issues.append("Too many ALL-CAPS words.")

    if not issues:
        print("PASS: no basic packaging lint issues found.")
    else:
        print("REVIEW:")
        for x in issues:
            print("-", x)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import csv, statistics, sys
from collections import defaultdict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 outlier_score.py benchmark_log.csv")
        sys.exit(2)

    path = sys.argv[1]
    rows = list(csv.DictReader(open(path, encoding="utf-8-sig")))
    by_channel = defaultdict(list)

    for r in rows:
        try:
            views = int(float(r["views"]))
        except Exception:
            continue
        by_channel[r["channel"]].append((views, r))

    out = []
    for channel, items in by_channel.items():
        if len(items) < 4:
            continue
        med = statistics.median(v for v, _ in items)
        if med <= 0:
            continue
        for views, r in items:
            ratio = views / med
            out.append((ratio, channel, views, med, r.get("title",""), r.get("url","")))

    out.sort(reverse=True, key=lambda x: x[0])

    print("ratio\tchannel\tviews\tmedian\ttitle\turl")
    for ratio, channel, views, med, title, url in out:
        print(f"{ratio:.2f}x\t{channel}\t{views}\t{int(med)}\t{title}\t{url}")

if __name__ == "__main__":
    main()

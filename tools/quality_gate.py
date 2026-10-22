#!/usr/bin/env python3
import json, sys

MAX = {
    "market_demand": 15,
    "outlier_evidence": 15,
    "promise_clarity": 10,
    "package_synergy": 15,
    "hook_strength": 10,
    "retention_architecture": 10,
    "payoff_strength": 10,
    "channel_fit": 5,
    "series_potential": 5,
    "production_feasibility": 5,
}

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 quality_gate.py scores.json")
        sys.exit(2)

    data = json.load(open(sys.argv[1], encoding="utf-8"))
    scores = data.get("scores", data)

    total = 0
    problems = []
    for k, maxv in MAX.items():
        v = scores.get(k)
        if v is None:
            problems.append((k, "missing", maxv))
            v = 0
        if not isinstance(v, (int, float)):
            raise SystemExit(f"{k}: score must be numeric")
        if v < 0 or v > maxv:
            raise SystemExit(f"{k}: must be between 0 and {maxv}")
        total += v

    pct = round(total, 1)
    gate = "GREEN" if total >= 80 else "YELLOW" if total >= 70 else "RED"

    ratios = []
    for k, maxv in MAX.items():
        v = scores.get(k, 0)
        ratios.append((v / maxv, k, v, maxv))
    ratios.sort()
    weakest = ratios[0]

    print(f"500K QUALITY SCORE: {pct}/100")
    print(f"GATE: {gate}")
    print(f"WEAKEST: {weakest[1]} ({weakest[2]}/{weakest[3]})")
    if problems:
        print("MISSING:", ", ".join(p[0] for p in problems))

if __name__ == "__main__":
    main()

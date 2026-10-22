#!/usr/bin/env python3
"""Bilingual YouTube hook scorer (Korean + English).

Derived from the MIT-licensed hookscore concept in Jakeschincariol/youtube-agent-skill.
Scores five heuristic properties from 0-100. A low score is a review signal; a high score is not a
view prediction.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
HOOKS = json.load(open(os.path.join(HERE, "../references/hooks.json"), encoding="utf-8"))["hooks"]

FILLER = {"basically","actually","literally","just","really","very","guys","hey","welcome","today","video","subscribe","channel",
          "사실","그냥","정말","너무","약간","일단","안녕하세요","오늘","영상","구독","여러분"}
VAGUE = {"amazing","incredible","insane","crazy","huge","massive","game","changer","secret","ultimate","best",
         "대박","미친","엄청난","놀라운","최고","완벽","혁신","역대급","비밀"}
CONCRETE = re.compile(r"(?:\b\d[\d,.]*\s?(?:%|k|m|x)?\b|\$\d+|\d+\s?(?:초|분|시간|일|주|개월|달|년|배|%))", re.I)
YOU = re.compile(r"(?:\b(?:you|your|you're|youre|yourself)\b|당신|여러분|너(?:는|가|의)?|당신의|본인|직접|구독자.{0,12}라면|초보.{0,8}라면|처음.{0,8}라면|하는 분)", re.I)
STAKE = re.compile(r"(?:\b(?:lose|lost|wasting|waste|quit|fail|cost|risk|before|stop|never|die|dead|gain|grow)\b|손해|손실|실패|낭비|위험|비용|후회|망하|떨어지|놓치|멈추|올리기 전|차이|결과|늘|줄|성장)", re.I)
CURIOSITY = re.compile(r"(?:\b(?:why|how|what|which|until|before|but|nobody|almost|except|reason|actually)\b|왜|어떻게|무엇|뭐|어느|하지만|그런데|이유|사실|공개|보여|정체)", re.I)
TOKEN = re.compile(r"[A-Za-z0-9가-힣'%$.,]+")

def words(t):
    return TOKEN.findall(t.lower())

def specificity(t):
    w = words(t)
    if not w: return 0
    nums = len(CONCRETE.findall(t))
    vague = sum(1 for x in w if x in VAGUE)
    filler = sum(1 for x in w if x in FILLER)
    proper = min(18, 6 * sum(1 for x in t.split()[1:] if x[:1].isupper()))
    s = 34 + nums * 22 - vague * 16 - filler * 4 + proper
    return max(0, min(100, s))

def address(t):
    n = len(YOU.findall(t))
    first = 30 if YOU.search(" ".join(t.split()[:6])) else 0
    return max(0, min(100, 26 + n * 20 + first))

def stakes(t):
    n = len(STAKE.findall(t))
    return max(0, min(100, 22 + n * 26 + (14 if CONCRETE.search(t) else 0)))

def curiosity(t):
    n = len(CURIOSITY.findall(t))
    q = 18 if t.strip().endswith("?") else 0
    closed = -18 if re.search(r"(?:\b(?:because|so that|which means)\b|왜냐하면|즉,?|그러니까)", t, re.I) else 0
    return max(0, min(100, 24 + n * 17 + q + closed))

def brevity(t):
    n = len(words(t))
    if n == 0: return 0
    if 6 <= n <= 24: return 100
    if n < 6: return max(30, 100 - (6 - n) * 12)
    return max(10, 100 - (n - 24) * 7)

PROPS = [("SPECIFICITY", specificity), ("ADDRESS", address), ("STAKES", stakes),
         ("CURIOSITY", curiosity), ("BREVITY", brevity)]

FIX = {
 "SPECIFICITY": "replace a vague adjective with a number, name, date, or visible artifact",
 "ADDRESS": "name the viewer or use you/your/여러분 near the opening when natural",
 "STAKES": "state what the viewer gains, loses, avoids, or risks",
 "CURIOSITY": "leave one meaningful question unresolved instead of answering it in the hook",
 "BREVITY": "shorten the opening until it can be spoken cleanly in roughly 10-15 seconds",
}

def classify(t):
    best, hits = None, 0
    for f in HOOKS:
        n = sum(1 for p in f.get("match", []) if re.search(p, t, re.I))
        if n > hits:
            best, hits = f, n
    return (best["name"] if best else "Unclassified"), hits

def score(t):
    parts = {n: fn(t) for n, fn in PROPS}
    vals = list(parts.values())
    verdict = round(0.6 * (sum(vals) / len(vals)) + 0.4 * min(vals))
    name, hits = classify(t)
    return parts, verdict, name, hits

def band(v):
    return "STRONG" if v >= 72 else "WORKABLE" if v >= 55 else "WEAK"

def report(t, parts, verdict, name, hits):
    print(f"\n  {t.strip()}")
    print("  " + "-" * min(72, max(20, len(t.strip()))))
    for k, v in parts.items():
        print(f"    {k:<12} {v:3d}  {'#' * (v // 5)}")
    print(f"    {'VERDICT':<12} {verdict:3d}  {band(verdict)}")
    print(f"    formula      {name}" + (f" ({hits} pattern{'s' if hits != 1 else ''} matched)" if hits else ""))
    low = min(parts, key=parts.get)
    print(f"    weakest      {low} - {FIX[low]}")

def main():
    args = sys.argv[1:]
    as_json = "--json" in args
    args = [x for x in args if x != "--json"]
    if "--hook" in args:
        i = args.index("--hook")
        if i + 1 >= len(args): raise SystemExit("--hook requires text")
        lines = [args[i+1]]
    elif args and os.path.exists(args[0]):
        lines = [l.strip() for l in open(args[0], encoding="utf-8").read().splitlines() if l.strip()]
    else:
        raise SystemExit('Usage: hookscore.py --hook "text" | hookscore.py hooks.txt [--json]')

    out = []
    for t in lines:
        parts, verdict, name, hits = score(t)
        out.append({"hook":t, "properties":parts, "verdict":verdict, "band":band(verdict), "formula":name, "matched":hits})
    out.sort(key=lambda r: -r["verdict"])
    if as_json:
        print(json.dumps([{k:v for k,v in r.items() if k != "matched"} for r in out], ensure_ascii=False, indent=2))
    else:
        for r in out: report(r["hook"], r["properties"], r["verdict"], r["formula"], r["matched"])
        if len(out) > 1:
            print(f"\n  winner: {out[0]['hook']} ({out[0]['verdict']}, {out[0]['band']})")

if __name__ == "__main__":
    main()

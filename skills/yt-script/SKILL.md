---
name: yt-script
description: >-
  Turn an approved YouTube idea and package into a recordable script. Generate five hook options,
  score them with the bundled bilingual hook scorer, keep the top two, then write the full spoken
  script with retention beats and [ON SCREEN: ...] directions. Use for scripts, hooks, openings,
  recording drafts, and any video that has passed packaging but is not ready to shoot.
---

# yt-script

Turn one approved idea into a script people can finish.

## Non-negotiable

Do not eyeball the opening. Generate FIVE hook candidates and run them through the bundled scorer.
A low score means review the hook; a high score is not a view guarantee.

```bash
python3 scripts/hookscore.py hooks.txt
python3 scripts/hookscore.py --hook "한 줄 훅"
```

## Before writing

1. Use the creator voice profile if one is available. If none exists, use `references/voice-template.md`
   and infer a provisional profile from three of the creator's own transcripts/videos when provided.
2. Never invent numbers, results, dates, quotes, or sources. Remove unsupported claims rather than
   filling gaps.
3. The title + thumbnail promise is the contract. The first 15 seconds must confirm that contract.

## Hook workflow

Write FIVE hooks using different mechanisms from `references/hooks.json`.
Each hook should try to do three jobs:

1. Confirm the click promise.
2. Open a question, consequence, or unresolved gap.
3. Prove that the promised payoff exists or is coming soon.

Run all five through `scripts/hookscore.py`. Return the top TWO with:
- total score
- specificity
- viewer address
- stakes
- curiosity
- brevity
- detected formula
- weakest property

If both top hooks score below 55, rewrite all five and score again once before continuing.

## Script shape

### 0:00-0:15 — Hook
Use the winning hook. No greeting, channel intro, subscribe pitch, or biography unless the concept
itself requires it.

### 0:15-0:45 — The turn
In one sentence, say what the video is going to do, then start doing it.

### Body
One idea per beat. Every beat must contain both:
- what is SAID
- `[ON SCREEN: ...]` showing what the viewer should see

Do not use a visual change merely for stimulation. Change the visual when it clarifies, proves,
contrasts, escalates, or resets attention.

### Payoff
Deliver the exact thing promised by the package and hook. Make the payoff explicit.

### Close
One next action only. Prefer a next-video bridge when it is more useful than a generic subscribe ask.

## Output

1. HOOK A + score panel
2. HOOK B + score panel
3. WINNER + formula + why it fits
4. SCRIPT, beat by beat, with `[ON SCREEN: ...]` on every beat
5. Estimated runtime (label the estimate)
6. CLAIM CHECK — unsupported claims removed or marked for evidence
7. NEXT-VIDEO BRIDGE

This skill writes and evaluates the script. It does not promise views or publish the video.

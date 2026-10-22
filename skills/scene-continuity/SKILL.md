---
name: scene-continuity
description: >-
  Create and enforce a scene-state ledger for AI image/video production so outfits, props, counts,
  camera, background, character identity and story state change correctly from scene to scene.
---

# scene-continuity

Before writing per-scene prompts, create a state ledger.

## Track for every scene
- scene number and timecode
- character outfit
- character expression
- character action
- prop inventory and exact counts
- what is visible in background
- camera position / lens / framing
- lighting
- what changed since previous scene
- what MUST remain identical
- transition trigger
- end state that becomes the next scene's start state

## Continuity rule

A state change must happen ONCE and persist until another explicit change.
If one outfit leaves a rack and moves onto the character, the rack count must decrease by one in all later scenes.
Do not silently reset props or wardrobe.

## Prompt discipline

For each scene include:
1. MUST PRESERVE
2. MUST CHANGE
3. MUST NOT APPEAR

## Output table

SCENE | TIME | OUTFIT | PROP STATE | ACTION | CHANGE | PRESERVE | END STATE

Then run a continuity check:
- count mismatch?
- outfit mismatch?
- camera drift?
- background drift?
- identity drift?
- story-state reset?

Return PASS or FIX before production prompts.

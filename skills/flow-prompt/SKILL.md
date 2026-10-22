---
name: flow-prompt
description: >-
  Write production-ready Korean and English prompts for Google Flow and similar image/video models,
  clearly separating still-image generation from image-to-video motion prompts and preserving scene continuity.
---

# flow-prompt

Use after the episode contract and scene-state ledger are locked.

## First classify the user's request

Return exactly one production artifact unless the user asks for multiple:
- IMAGE PROMPT
- VIDEO MOTION PROMPT
- TRANSITION PROMPT
- ENDING ACTION PROMPT

Never substitute one for another.
If the user says "동영상 제작 아니야" or asks for image prompts, do not include motion/lip-sync prompts.
If the user asks for video prompts, assume the reference image already exists unless told otherwise; describe MOTION, not re-design.

## Prompt structure

### Image prompt
1. character invariant
2. exact outfit
3. exact prop/state count
4. composition/framing
5. expression/pose
6. environment/lighting
7. quality/style
8. negative constraints

### Video motion prompt
1. source image continuity statement
2. camera rule
3. character movement
4. transition trigger
5. object/wardrobe state change
6. fur/cloth physics
7. end pose/state
8. negative constraints

## Consistency language

Prefer explicit constraints:
- exact same character identity
- same camera position
- same room/background
- exactly N items remain
- no new objects
- no face/body morphing
- no camera move unless required
- no dialogue/lip-sync when the contract says no dialogue

## Output

For each requested scene/cut:
KOREAN PROMPT
ENGLISH PROMPT
NEGATIVE / DO-NOT-CHANGE
CONTINUITY CHECK

Do not invent a model capability. If a specific Flow model behavior is uncertain, write model-agnostic motion instructions rather than claiming support.

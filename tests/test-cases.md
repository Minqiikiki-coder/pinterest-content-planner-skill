# Test cases — Pinterest Content Planner

Behavioral tests for the skill. Each case gives inputs, a prompt, and the
observable criteria a correct run must satisfy. Case 1 is backed by a
mechanical validator (`validate_plan.py`); the rest are checked against the
listed criteria.

## Case 1 — Standard run (wabi-sabi interiors)

**Inputs:** `templates/inputs-template.md` defaults (3 boards, weights
50/30/20, 3 pins/day, image source `ai`) + `examples/sample-topic-log.md`.
**Prompt:** "Plan my next 7 days of pins."
**Expected output:** `examples/wabisabi-7day-plan.md`
**Pass criteria:**
- Exactly 21 pins across 7 days
- Board split within ±1 of weights (10 / 6 / 5)
- No subject repeats a topic-log entry dated within 14 days before its
  planned date, and no two pins share a subject
- All titles ≤ 100 characters, keyword-first, `Keyword | Vibe` format
- All descriptions: 2 sentences, ≥ 2 niche keywords, save prompt,
  `Image created with AI` disclosure
- ≥ 40% saveable compositions (lineups, flat lays, styled arrangements)
- Topic-log addition block present

**Run it:** `python3 tests/validate_plan.py examples/wabisabi-7day-plan.md`

## Case 2 — Generalization to a new niche

**Inputs:** niche "Small-space indoor plants for apartment renters"; boards
"Plant Shelf Styling" (60), "Beginner Plant Care" (40); keywords: indoor
plants, plant shelf, small apartment, plant care tips, low light plants;
2 pins/day; no topic log.
**Prompt:** "Plan my next 7 days of pins."
**Pass criteria:**
- 14 pins; board split ≈ 8 / 6
- Titles and descriptions use *only* the new niche's keywords and boards —
  no wabi-sabi / interiors vocabulary leaks in
- Because no topic log was provided, the output opens with a warning that
  repeats cannot be checked, and still ends with a topic-log block to start one
- All copy rules (length, save prompt, format) still hold

## Case 3 — Saturated topic log (edge case)

**Inputs:** Case 1 inputs, but the topic log is extended so that the 20 most
obvious subjects in the niche were all posted within the last 14 days.
**Prompt:** "Plan my next 7 days of pins."
**Pass criteria:**
- The planner does **not** silently repeat blocked subjects
- It either (a) proposes fresh sub-themes inside the niche and plans from
  those, clearly labeled, or (b) stops and tells the user the pool is
  exhausted, with options (shorten the no-repeat window, add a board, widen
  the niche)
- Any repeated subject is flagged explicitly, never hidden

## Case 4 — Short keyword list (edge case)

**Inputs:** Case 1 inputs, but only 3 keywords provided.
**Prompt:** "Plan my next 7 days of pins."
**Pass criteria:**
- Plan is still generated
- Additional keyword phrases are derived from the niche and board
  descriptions and marked as *suggested* in the output
- Titles still satisfy the keyword-first rule using provided + suggested
  keywords

## Regression checklist (every release)

- [ ] Case 1 validator passes (`ALL CHECKS PASSED`)
- [ ] Case 2 run shows zero vocabulary leakage from the example niche
- [ ] Case 3 never produces an unflagged repeat
- [ ] SKILL.md validation checklist matches what `validate_plan.py` checks
- [ ] Example plan's stated board split equals the validator's counted split

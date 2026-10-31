---
name: pinterest-content-planner
description: Plan a week of Pinterest pins for a niche account — image concepts, keyword-first titles, save-driven descriptions, and board rotation — without repeating recent topics. Use when a creator needs a batch content plan for Pinterest.
version: 1.0.0
author: Kiki Jin
license: MIT
---

# Pinterest Content Planner

Turn a niche, a set of boards, and a list of past topics into a ready-to-produce
7-day Pinterest content plan. Built for small creators who post daily but don't
have time to brainstorm every pin.

The planner handles the repetitive 80% of Pinterest content work:

- picking subjects that don't repeat recent posts
- rotating across boards in proportion to their performance
- writing keyword-first titles and descriptions that are built to be *saved*
- briefing each image so it can be produced (photo, design, or AI-generated)

## Inputs

Ask for these once; reuse the answers for every later run.

| Input | Required | Example |
|---|---|---|
| `niche` | yes | "Wabi-sabi and calm interior design / cafes" |
| `boards` | yes | Name + one-line description per board |
| `board_weights` | no | Percent share per board (default: equal) |
| `keywords` | yes | 8–15 search phrases your audience types into Pinterest |
| `pins_per_day` | no | Default 3 |
| `topic_log` | no | Markdown list of past subjects with dates (see `examples/sample-topic-log.md`) |
| `style_guide` | no | Palette, materials, mood, image style |
| `image_source` | no | `photo`, `design`, or `ai` (default: ask) |

If `image_source` is `ai`, every description must end with the disclosure line
`Image created with AI`.

## Workflow

### Step 1 — Load context
Read the inputs and the topic log. Build a blocklist: every subject posted in
the **last 14 days** is off-limits. A subject means the specific scene/object
combination (e.g. "stoneware bowls on a cafe counter"), not the broad theme —
a fresh angle on a proven theme is allowed after 14 days.

### Step 2 — Allocate boards
Distribute the week's pins across boards according to `board_weights`.
With 3 pins/day × 7 days = 21 pins and weights 50/30/20, the split is
roughly 10 / 6 / 5. Never let the weakest board drop to zero — feeding it
regularly is how it grows.

### Step 3 — Pick subjects
For each slot, choose a subject that:
- matches the board's theme and the niche
- is **not** on the 14-day blocklist
- fits the style guide (palette, materials, mood)

Mix compositions — at least **40% saveable formats**, not just pretty scenes:
- styled lineups / shelf arrangements
- flat lays with 4–6 intentional objects
- "corner" compositions (one chair, one table, one hero object)
- checklists and step visuals ("3 ways to style…", "morning ritual setup")
- before/after or empty-vs-styled pairs

Clone proven winners with fresh angles: if a past subject performed well,
reuse its *theme* with a different room, object, or composition after the
14-day window.

### Step 4 — Write the copy
**Title** (max 100 characters):
`Main Keyword Phrase | Vibe or Benefit Phrase`
Keyword first — Pinterest is a search engine. Title case. No hashtags,
no emojis, no clickbait.

**Description** (exactly 2 sentences + optional disclosure):
1. Describe the scene using 2–3 searchable keywords from the input list,
   woven in naturally.
2. A gentle save prompt tied to the pin's use ("Save this for your slow
   morning corner.").
3. If `image_source` is `ai`, add the line `Image created with AI`.

### Step 5 — Validate before delivering
Run every check in the Validation section. If a check fails, fix the plan —
do not deliver a plan that fails its own rules.

### Step 6 — Deliver
Output:
1. The plan table (day, #, image concept, title, board).
2. One detail block per pin (title, description, board, image brief).
3. A `topic_log` addition block listing the new subjects with dates, so the
   user can append it to their log and the next run stays repeat-free.

## Image brief rules
Each pin gets a one-paragraph production brief:
- vertical 2:3 composition (1000 × 1500 px or larger)
- the hero object, supporting objects, surface, background, light
- what must NOT appear (text, logos, people — unless the niche requires them)
- style-guide anchors (palette, materials, mood)

## Validation checklist
- [ ] Every title ≤ 100 characters and starts with a keyword phrase
- [ ] Every description is 2 sentences, contains 2–3 keywords, ends with a
      save prompt
- [ ] No subject repeats a topic-log entry from the last 14 days
- [ ] No two pins in the plan share the same subject
- [ ] Board counts match the weights (±1 pin)
- [ ] ≥ 40% of pins use saveable compositions
- [ ] AI disclosure present on every description when `image_source` is `ai`
- [ ] Topic-log addition block included

## Edge cases
- **Blocklist covers almost everything:** say so, propose widening to new
  sub-themes inside the niche instead of silently repeating subjects.
- **No topic log provided:** warn that repeats can't be checked, generate the
  plan, and start a log from this plan.
- **Keyword list too short (< 5):** derive additional phrases from the niche
  and board descriptions, and mark them as suggested in the output.
- **Seasonal events within the plan window:** reserve ~20% of slots for the
  event theme if it fits the niche; never force an off-niche seasonal pin.

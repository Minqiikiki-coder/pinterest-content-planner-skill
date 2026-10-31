# Tutorial — your first week with the Pinterest Content Planner

Time needed: ~15 minutes of setup, then ~10 minutes per weekly plan.

## 1. Set up the skill

**Option A — agent frameworks (Claude / skills-based agents):**
Copy `SKILL.md` into your skills folder. The agent will pick it up whenever
you ask for Pinterest planning.

**Option B — any chat model (ChatGPT, Claude.ai, Gemini…):**
Start a new chat, paste the full contents of `SKILL.md`, and add:
*"Follow this skill. First, ask me for the inputs."*

## 2. Fill in your inputs

Copy [`../templates/inputs-template.md`](../templates/inputs-template.md) and
fill it in. The four things that matter most:

- **Niche** — one specific sentence. "Home decor" is too broad;
  "Wabi-sabi and calm interior design / cafes" works.
- **Boards** — your real board names, one line each on what belongs there.
- **Board weights** — look at your Pinterest analytics (last 30 days,
  impressions per board) and split 100 points across boards by performance.
  Weak boards still get ≥ 15 — they can't grow if they never get pins.
- **Keywords** — open Pinterest, type the start of a phrase your audience
  would search, and note the autocomplete suggestions. Collect 8–15.

## 3. Start (or maintain) your topic log

Create a file like [`../examples/sample-topic-log.md`](../examples/sample-topic-log.md):

```markdown
- 2026-10-28 | Calm Interiors & Neutral Aesthetics | Neutral reading nook with linen armchair
```

One line per published pin: date, board, subject. This file is what stops the
planner from repeating you. Backfill it from your existing boards if you can
(just the last 2 weeks matter most).

## 4. Generate a plan

Say: *"Plan my next 7 days of pins using my inputs and topic log."*

You'll get:
1. A plan table (day, image concept, title, board)
2. A detail block per pin, including the image brief
3. A topic-log addition block

**Check the plan like an editor, not a fan.** Veto anything off-brand, ask for
swaps ("replace Tuesday's cafe pin with a shelf styling pin"), and only then
produce images.

## 5. Produce and publish

Work from the image briefs:
- **Photographers:** the brief is your shot list (hero object, surface, light).
- **AI image tools:** paste the brief as your prompt; keep the exclusions
  ("no text, no people, no logos"). If you publish AI images, the plan's
  descriptions already carry the `Image created with AI` disclosure line —
  keep it.

Publish at a consistent time. Spreading pins across the day beats dumping all
of them at once.

## 6. Close the loop weekly

1. Append the plan's topic-log block to your log (subjects + publish dates).
2. Once a month, re-check board analytics and adjust the weights.
3. Note your top-3 saved pins — tell the planner to clone those *themes* with
   fresh angles in the next plan ("clone winners" is built into Step 3 of the
   skill).

## Troubleshooting

| Problem | Fix |
|---|---|
| Planner repeats a topic | Your topic log is missing entries — backfill the last 14 days. |
| Titles feel generic | Your keyword list is too short; add autocomplete phrases (Step 2). |
| Weak board gets no pins | Set explicit weights; the default is equal split. |
| Plan ignores your style | Add palette/materials/mood to the style guide — be concrete ("cream, sand, raw wood, stoneware; no bright colors"). |
| Everything is a "pretty scene" | Remind it of the ≥ 40% saveable-formats rule (lineups, flat lays, checklists). |

## Worked example

See [`../examples/wabisabi-7day-plan.md`](../examples/wabisabi-7day-plan.md)
for a complete run: inputs, plan table, detail blocks, and the topic-log
addition — generated for a wabi-sabi interiors account with 3 boards.

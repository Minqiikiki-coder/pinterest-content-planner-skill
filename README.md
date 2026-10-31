# Pinterest Content Planner — an AI Skill

**Plan a week of Pinterest pins in minutes: image concepts, keyword-first titles, save-driven descriptions, and board rotation — with no repeated topics.**

A small, runnable AI skill for small Pinterest creators. Give it your niche,
your boards, and a log of what you've already posted; it returns a 7-day
content plan that is ready to produce and publish.

> Built by [Kiki Jin](https://www.pinterest.com/ikiknij) — cognitive science
> student and creator of [@ikiknij](https://www.pinterest.com/ikiknij)
> (wabi-sabi & calm interior design). This skill is a productized version of
> the exact workflow used to run that account daily.

---

## Why this exists

Posting on Pinterest every day is not hard because of any single pin — it's
hard because of the repetition: *What do I post today? Did I already do this
topic? Which board needs feeding? Is this title searchable?*

This skill turns that daily decision pile into one weekly planning session.

## What it does

- 🗓️ **Plans 7 days of pins** (configurable pins/day) from one input form
- 🔁 **Never repeats a recent topic** — checks every subject against your
  topic log (14-day no-repeat window)
- 🎯 **Rotates boards by weight** — strong boards get more slots, weak boards
  never starve
- 🔍 **Writes SEO-first copy** — keyword-first titles (≤ 100 chars) and
  2-sentence descriptions engineered for *saves*, Pinterest's strongest signal
- 🖼️ **Briefs every image** — composition, objects, light, and exclusions, so
  each pin can be photographed, designed, or AI-generated
- ✅ **Self-validates** — the plan must pass an 8-point checklist before it is
  delivered (title length, keyword coverage, board split, saveable-format
  ratio, AI disclosure, …)

## Quick start

1. Copy this repo's `SKILL.md` into your AI assistant (Claude, ChatGPT, or any
   agent that accepts instruction files), or install it as a skill in your
   agent framework.
2. Fill in [`templates/inputs-template.md`](templates/inputs-template.md) —
   niche, boards, keywords, style guide.
3. Ask: *"Plan my next 7 days of pins."*
4. Produce the images from the briefs, publish, and append the returned
   topic-log block to your log.

Full walkthrough: [`docs/tutorial.md`](docs/tutorial.md)

## Example output

A real 7-day plan for a wabi-sabi interiors account (3 pins/day, 3 boards,
50/30/20 weights): [`examples/wabisabi-7day-plan.md`](examples/wabisabi-7day-plan.md)

Excerpt:

| Day | Title | Board |
|---|---|---|
| Sun Nov 1 | Japandi Kitchen Shelves \| Stoneware Stacks & Raw Wood Calm | Calm Interiors & Neutral Aesthetics |
| Sun Nov 1 | Minimalist Cafe Window Bar \| Wood Stools & Ceramic Cups | Minimalist & Wabi-Sabi Cafes |
| Sun Nov 1 | Iced Matcha Moment \| Glass, Linen & Stone Coaster | Matcha, Coffee & Slow Mornings |

## Testing

Behavioral test cases with pass criteria live in
[`tests/test-cases.md`](tests/test-cases.md). A small Python validator checks
any generated plan against the mechanical rules (title length, save prompts,
duplicate subjects, disclosure):

```bash
python3 tests/validate_plan.py examples/wabisabi-7day-plan.md
# → ALL CHECKS PASSED (21 pins)
```

## Case study: @ikiknij

The workflow behind this skill runs a real account:

- **Account:** @ikiknij — wabi-sabi & calm interiors, business account
- **Baseline (first audit, Sep–Oct 2026):** 97 pins, 4 boards, ~34k monthly
  views, 179 saves in 30 days — with all planning done manually
- **With this workflow:** daily batches are planned against a topic log with
  board weights (Interiors > Cafes > Matcha), published every evening, and
  reviewed weekly

*(The account is run growth-only, with no affiliate links or selling, while
its owner is an international student in the US.)*

## Design decisions

- **Why a topic log instead of memory?** A plain Markdown file is portable
  across models and tools, auditable by the user, and doubles as a content
  archive. The 14-day window matches how Pinterest re-surfaces content.
- **Why "saves" as the optimization target?** Saves are the strongest
  distribution signal for small accounts — a saved pin keeps circulating.
  Hence the ≥ 40% saveable-composition rule (lineups, flat lays, checklists).
- **Why self-validation inside the skill?** Planner outputs fail quietly
  (a 104-character title, a repeated subject). Making the model check its own
  plan against a checklist before delivering catches most of it.

## Limitations

- The planner cannot see Pinterest analytics; board weights are set by the
  user from their own stats.
- Keyword suggestions are derived from the niche, not from live search-volume
  data.
- Image briefs still need a human (or an image model) to produce the visuals.

## Roadmap

- [ ] Analytics feedback loop: import monthly stats, auto-adjust board weights
- [ ] Seasonal calendar packs (holiday hooks per niche)
- [ ] Idea-pin / video brief variant

## License

MIT — see [`LICENSE`](LICENSE). Use it for your own account; a link back is
appreciated.

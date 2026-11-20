# Results, setup and the log

## First time for a project

Do this once, before the first prompt, in one short message:

1. **The user's Dreamina.** MODEL-NOTES.md holds what the screen showed on 2026-11-20 (models, credits, sizes, ratios, Background, Elements, video modes). Ask only what it lacks: the plan (which models are free or unlimited, and until when), and the names of any saved Elements. Or ask for a screenshot of the model and settings panel. Write new facts in the "Seen on the screen" column of MODEL-NOTES.md, with the date.
2. **Cards.** Draft the Style Card and the Character Cards the job needs (STYLE-BRIDGE.md), each with one line saying which doc every field came from. The user approves or corrects them.
3. **Files.** Create `docs/dreamina/cards.md` and `docs/dreamina/prompt-log.md` in the project's folder (formats below), unless PROJECT-NOTES.md names other places.

If the user wants a prompt right away, give it with the draft cards marked "draft v0" and do the setup alongside.

## What the user may say

| The user says | Do |
|---|---|
| "Dreamina prompt for ..." | One prompt in the output format |
| "three variants", "give me options" | Complete variants that differ in moment, angle or mood, never only in adjectives |
| "new character", "three poses", "transparent" | One picture per pose or side, each made from the approved first picture, never several in one picture (IMAGE.md); Seedream 5.5 with Background: Transparent, or a flat background and Remove BG; the word "transparent" never goes in a prompt |
| "same picture as a vertical capsule", "change X" | Edit mode: one change, everything else pinned; or Expand image when only the shape changes |
| "fix just the hand", "it's cropped", "make it bigger", "show it from the side" | The tool in "The cheapest fix first", below |
| "series", "all the cards", a list of names | Series mode: anchor first, then frame and sheet |
| "animate this", "teaser from this picture" | Video from that still as the first frame; test on Seedance 2.5 Draft |
| "longer", "25 seconds" | Segments by extension |
| "like <a game or film>" | Turn it into qualities in words, show the reading, keep the name out |
| "new card", "update the style card: ..." | New card version in cards.md; note which pictures were made under the old one |
| "kept", "that fixed it", "log it" | Log the round; a fix that worked twice becomes a Lesson; an approved anchor is saved as an Element |
| "my Dreamina shows ..." | Update MODEL-NOTES.md and replan anything that depended on it |
| "shorter", "simpler" | Cut clauses in this order: secondary details, place, mood words; never the subject, counts or card |

## The cheapest fix first

Before rewriting a prompt, check whether a Dreamina tool fixes the problem in one step. A tool keeps everything that is already right; a new generation risks it. Tool prices and controls were not read yet (MODEL-NOTES.md, the paid-plan screen pass): name the tool and say what to do in plain words.

| Problem | Cheapest fix | What to write |
|---|---|---|
| One region is wrong in a good picture (a hand, an extra tail, a stray sign) | **Smart edit** on that region | One line with the region's end state: "the fox has one bushy tail" |
| The subject is cropped, or the picture needs more room (a taller or wider shape) | **Expand image** | What fills the new space, if the tool asks |
| Too small or soft for its use | **Creative upscale** (to 8K) | Nothing |
| The background must go (a cut-out) | **Seedream 5.5, Background: Transparent** for a new picture; **Remove BG** for a picture already made | Nothing; the word "transparent" never goes in a prompt |
| A new side or camera angle of an approved subject | **Angles** (All tools, Camera & Motion) from the approved picture | The angle in words, if asked; the edit prompt in IMAGE.md is the fallback |
| Style drifts across a series | Attach the anchor picture, or mention the **Style Element** with @ | The frame, unchanged |
| Learning the words for an approved picture's look | **Visual to prompt** on that picture | Check its output against the Style Card and keep only the words that match; never paste it unchecked |
| Parts must be edited one at a time (a character over a background) | **Separate layers** | Nothing |
| One thing wrong in a clip that is otherwise right | **Smart edit** mode in AI Video | The one change, as the end state |
| The moment, the medium or the composition is wrong | A new generation, one layer changed (below) | The changed prompt line |

## Reading a result

When the user pastes the picture or a frame of the clip, look at it before answering and compare it with the prompt and the cards: counts (legs, fingers, ears, tails), the medium (drawn or photographic), the accent colour, how much of the frame the subject fills, any stray lettering, the light direction. Say what you see in one or two lines, then the fix.

When the user only describes it, map their words to one layer:

| The user says | Layer | The change |
|---|---|---|
| "not our style", "looks AI", "looks 3D", "too realistic", "too smooth" | Medium | Remove lens and photo words; medium first in Style; attach the anchor picture or mention the Style Element |
| "too busy", "can't see the subject", "messy" | Composition | Fewer elements; "the subject fills two thirds of the frame"; plain background |
| "boring", "flat", "static", "nothing happens" | The moment | A different action or viewpoint; never more adjectives |
| "wrong mood", "too dark", "too cute", "too scary" | Light and mood | One new light story and one mood word |
| "colours are off", "too colourful" | Colour | Hex plus name on the large areas; one accent, "everything else muted" |
| "the character looks different" | Identity | Attach the primary picture or mention the Character Element; repeat Counts and Marks; remove any re-description |
| "letters are wrong" | Text | Shorter text in double quotes, "Draw text on image" on, or move it to the editor |
| "too fast", "rushed", "too slow" | Timing | Fewer actions per beat, or longer and shorter beats |
| "camera does its own thing" | Camera | Camera line earlier; one move; "static" if needed |
| "it melts", "morphs", "extra legs when moving" | Motion size | Smaller, slower movement; closer shot; fewer movers |
| "close", "almost" | - | Ask which one thing is off; change only that |

Rules for a round:
- One layer per round, and name the line that changed so the user can see cause and effect.
- Keep what the user said is right by saying it in the KEEP line or pinning it in an edit.
- A local flaw in a good picture is Smart edit (table above), not a new generation.
- After three rounds without progress, stop tweaking: rewrite from the brief, or change the method (attach a reference, go still-first, split the shot, simplify the scene). Say that this is what you are doing.
- Results vary between generations of the same prompt. If one of four is right, the prompt is right: log it as kept.

## The log

`docs/dreamina/cards.md`:
```
# Dreamina cards - <project>
## Style Card v<n> (approved <date>) · Element: <@Name, if saved>
<card>
## Character Card - <name> v<n> (approved <date>) · primary picture: <file> · Element: <@Name, if saved>
<card>
## Older versions
<kept, with the date they were replaced>
```

`docs/dreamina/prompt-log.md`:
```
# Dreamina prompt log - <project>
## Lessons            <- rules that held at least twice; read these first
- <rule> (since <date>)

## Log
| Date | Asset | Model, settings | Prompt (or link) | Result | What fixed it |
```
- Result is one of: kept, close, redo, dropped.
- Log every round the user reports, in a few words. Long prompts are linked to a sheet or written under the table.
- A fix that works twice moves up to Lessons. A Lesson that holds for more than one project is proposed to the user as a change to this skill.
- Follow any extra logging rule in PROJECT-NOTES.md.

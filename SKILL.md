---
name: dreamina-prompt
description: Writes prompts and the settings to pick for Dreamina (CapCut) - Seedream and other image models, image edits, series of matching pictures, Seedance videos (still first, then motion), voice-overs and character dialogue (ElevenLabs, MiniMax, SeedAudio), sound scenes and music (MiniMax Music) - keeping one project's look, palette, characters and voices consistent through Style and Character Cards, saved Elements, references and a per-project log; with Dreamina's own CLI it reads the live model catalog, places prompts on the user's canvas, or runs them after the user approves the credits. Use when the user asks for a Dreamina, Seedream, Seedance or Dreamina audio or music prompt, or for key art, Steam capsules, social posts, card or icon pictures, trailers, teasers, Shorts, TikToks, Reels, voice lines, narration or music they will make in Dreamina, or reports or shows how a Dreamina result came out.
---

# Dreamina prompt writer

If PROJECT-NOTES.md exists beside this file, read it first: its project rules win over this skill's defaults.

This skill writes the prompt and the settings to pick; the art is made by Dreamina on the user's account. By default the user runs it. With Dreamina's CLI the skill can also place the prompt on the user's canvas, or run it after the user approves the credits ([CLI.md](CLI.md)). Claude never draws a picture itself.

## Pick the job

| The user asks for | Mode | Read |
|---|---|---|
| One picture | Image | [IMAGE.md](IMAGE.md) |
| A new character, several poses or sides, transparent pictures | Character set: one picture each | [IMAGE.md](IMAGE.md), "Characters, poses and cut-outs" |
| A change to a picture they made, or the same art in another shape | Edit | [IMAGE.md](IMAGE.md), "Editing" |
| One region wrong, a cropped edge, a small or soft picture, a background to remove, a new angle | A Dreamina tool, not a new prompt | [FEEDBACK.md](FEEDBACK.md), "The cheapest fix first" |
| Many pictures of one kind (cards, icons, a post series) | Series | [SERIES.md](SERIES.md) |
| A clip | Still first, then motion | [VIDEO.md](VIDEO.md) |
| A clip longer than one generation | Segments | [VIDEO.md](VIDEO.md), "Longer clips" |
| Several shots, a speaking character, cuts on the music | The director's block | [VIDEO.md](VIDEO.md), "The director's block" |
| A motion-graphics video from a Motion Studio style (tiles, type, charts, explainers) | Motion Studio: read the style's card first | [MODEL-NOTES.md](MODEL-NOTES.md), "Motion Studio" |
| Voice lines, dialogue, narration, a voice-over | Voice | [AUDIO.md](AUDIO.md) |
| Voices, effects and music placed by time in one track | Sound scene | [AUDIO.md](AUDIO.md), "A timed sound scene" |
| A song, a theme, a music bed | Music | [AUDIO.md](AUDIO.md), "Music" |
| "Put it in Dreamina", "run it for me", "what can model X do" | CLI | [CLI.md](CLI.md) |
| They say or show how a result came out | Result | [FEEDBACK.md](FEEDBACK.md) |
| The first prompt ever for a project | Setup, then the job | [FEEDBACK.md](FEEDBACK.md), "First time for a project" |

A complete worked answer of each kind is in [EXAMPLES.md](EXAMPLES.md).

## Workflow

1. **Brief.** Five things: the project; what it is and where it goes; the moment (who does what, where); what the viewer must notice first; what the user already has (approved pictures, saved Elements). Ask at most two questions, and only for what changes the prompt. Fill the rest with a sensible choice and show it on the ASSUMED line.
2. **Read the project's files**, lessons first:
   - `docs/dreamina/prompt-log.md` (its Lessons section) and `docs/dreamina/cards.md` in the project's folder, when they exist. PROJECT-NOTES.md names the folders.
   - The project's look: its art-direction doc, style guide or approved pictures (PROJECT-NOTES.md names them).
   - A project with no notes and no docs: ask for its look in three lines, or the name of its saved Style Element.
3. **Cards.** Reuse the Style Card and Character Cards from `cards.md`, or draft them with [STYLE-BRIDGE.md](STYLE-BRIDGE.md) and get the user's yes before a series depends on them. Card text is pasted unchanged, never reworded.
4. **Settings.**
   - Model: [IMAGE.md](IMAGE.md), "Which image model" (an Unlimited model for tries: Seedream 5.5 or 5.0 Flash at 1.5K-2K; Seedream 5.0 Pro for a final at 4K; GPT Image 2.5 for exact text and unusual ratios). For video, [VIDEO.md](VIDEO.md), "Which video model" (test on Seedance 2.5 Draft, run the keeper on Seedance 2.5). For voice and music, [AUDIO.md](AUDIO.md), "Pick the tool".
   - When the CLI is installed and a limit matters, check it live: `scripts/catalog.py` ([CLI.md](CLI.md)).
   - Size and ratio: [FORMATS.md](FORMATS.md). What each model offers on the screen: [MODEL-NOTES.md](MODEL-NOTES.md).
   - Background (Seedream 5.5 only): Transparent for a cut-out, Opaque for a picture with a scene.
   - Elements: when an approved subject or look is saved as an Element, the prompt mentions it with @ and does not describe it again.
5. **Build** with the mode's formula: the use case first, then the subject with its colour, texture and action, then place, composition and light, style last. Short sentences, concrete words, matched to the medium (STYLE-BRIDGE.md, "Match the words to the medium"). The order follows Dreamina's own prompt article (MODEL-NOTES.md).
6. **Check** (list below), then answer in the output format, with nothing before it but a one-line read of the brief.
7. **Save what is approved.** When the user approves an anchor picture (a character, a prop, a place, or the look of a series), tell them to save it as an Element: type Character, Scene, Prop, Product, Style or Other; a name of up to 20 characters. Record the name in `cards.md`. Later prompts mention it with @ and describe only what is new.
8. **Learn.** When the user reports a result, follow FEEDBACK.md: the cheapest fix first (a Dreamina tool when one region, the crop, the size, the background or the angle is wrong); otherwise one layer changed, the changed line named, the round logged.

## Standing rules

- No names of artists, studios, films or other games in any prompt. When the user names one in chat as a reference, turn it into two or three qualities in words, show them that reading, and use only the words.
- A reference picture shared for reading a look is not a Dreamina input until the user says so. Ask first.
- A prompt is complete on its own: settings, uploads and Elements named, so whoever runs it in Dreamina needs nothing from this chat.
- A fact about Dreamina is "per the guide" until it is seen on the user's screen; seen facts go in MODEL-NOTES.md with the date.
- Follow the project's own rules (its CLAUDE.md, contributing notes or PROJECT-NOTES.md) when writing files there. One project's content never goes in another project's files.

## Output format

```
## <what it is> - <project> - <mode>
SETTINGS  Model: <...> · Ratio: <...> (target <px>) · Resolution: <...> · Pictures: <per run> · Background: <Auto / Opaque / Transparent> · Mode: <text / reference / first frame / ...> · Element: <@Name, or none>
UPLOAD    <picture -> its role>, or "nothing"
ASSUMED   <choices made for the user, each in a few words>, or leave the line out

PROMPT
<English, one short paragraph per formula part, in one code block they can copy whole>

KEEP
<what must not change: only for edits, series and video; inside the same code block>

IF IT COMES OUT WRONG
- <likely problem> -> <the one line to change, or the Dreamina tool to use>
```
- SETTINGS names everything to set by hand: the model, the ratio, the resolution (Seedream 5.5: 1.5K or 2K; 5.0 Pro: up to 4K), the pictures a run (5.5: 4; 5.0 Pro: 2), Background (Seedream 5.5 only; leave it out on other models), the mode, and any saved Element to mention with @.
- For video, SETTINGS names the model, ratio, resolution, duration, mode and Elements; no Pictures or Background. When the mode changes the model (Multiframes, Smart edit, Video recreator), say so.
- For voice and music, use the output format in AUDIO.md.
- Name the price when it is known (MODEL-NOTES.md): "6 credits a picture, free with Unlimited".
- Everything the user pastes into Dreamina sits in one code block; settings and notes stay outside it.
- Two or three variants only when the brief leaves a real choice (moment, angle, mood) or the user asks; each is a complete prompt with a one-line label of how it differs.

## Check before answering

- [ ] Format and purpose open the prompt; the focal subject comes before any style word, with its colour, texture and action.
- [ ] Card text is identical to earlier prompts of the series; colours are hex plus a colour name.
- [ ] Words match the medium: no lens, film or photo terms in an inked or painted look.
- [ ] Short sentences and concrete words, not "cinematic", "epic", "beautiful", "high quality", "nice", "some". The short form under about 200 words; the labelled form only for layouts, text or preserved references (IMAGE.md), inside the model's prompt limit.
- [ ] One accent colour, one light story, one camera move per shot, one job per shot.
- [ ] Counts stated positively where models slip (a hand: five fingers; a fox: four legs, one tail).
- [ ] Text in the picture is the exact words in double quotes with letter style, colour and place; logos are added in an editor.
- [ ] Exclusions are "keep ..." lines or positive statements first; a closing "Avoid:" paragraph lists only concrete defects. The word "transparent" is never in a prompt: transparency is the Background setting (Seedream 5.5, GPT Image) or the Remove BG tool.
- [ ] Voice scripts use the model's own tag brackets (ElevenLabs `[ ]`, MiniMax `( )`, Seed TTS none) and an exact voice name from the library; one voice per character.
- [ ] A run through the CLI has the user's yes to its price and a `--credit-ceiling` (CLI.md).
- [ ] SETTINGS fits what the model offers (MODEL-NOTES.md): the ratio is in its list, no 4K on Seedream 5.5, Background only on 5.5.
- [ ] A saved Element is mentioned with @ and not described again; a newly approved anchor is flagged to be saved as an Element.
- [ ] Size and the destination's rules match FORMATS.md (Steam: no text beyond the title; none on the library hero).
- [ ] Every Lesson in the project's prompt-log is applied, and the standing rules and PROJECT-NOTES.md hold.

## Files

[IMAGE.md](IMAGE.md) · [VIDEO.md](VIDEO.md) · [AUDIO.md](AUDIO.md) · [SERIES.md](SERIES.md) · [FEEDBACK.md](FEEDBACK.md) · [STYLE-BRIDGE.md](STYLE-BRIDGE.md) · [FORMATS.md](FORMATS.md) · [CLI.md](CLI.md) · [MODEL-NOTES.md](MODEL-NOTES.md) · [EXAMPLES.md](EXAMPLES.md)

`scripts/look_up.py` (styles, palettes, fonts from the ui-ux-pro-max skill, installed beside this one) · `scripts/expand_series.py` (one frame + many subjects -> a prompt sheet) · `scripts/catalog.py` (Dreamina's live models and voices, read-only, needs the CLI). Run them as `python "<skill folder>/scripts/<name>.py" ...`.

[MANUAL.md](MANUAL.md) is the user's guide to this skill. Read it only when the user asks how to use the skill; keep it true when the skill changes.

PROJECT-NOTES.md (optional, personal): project folders, team roles and project rules that win over these defaults. It is never part of a published copy.

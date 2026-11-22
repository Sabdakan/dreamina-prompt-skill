# Images: Seedream

Built from Dreamina's own text-to-image prompt article, its Seedream 5.0 Pro guide, two provider guides (Runware for 5.0 Pro, fal for 5.0 Lite), and, on 2026-11-22, a paid account's screen, Dreamina's own example prompts and its CLI's live model list. Where they differ, the screen wins; see MODEL-NOTES.md.

## The formula, in this order

The order follows Dreamina's own prompt article: state the use case, then the subject first and its description (colour, texture, action), then style and context. The provider guides add place, composition and light, and put style last. Seedream reads each clause as an instruction; a part left out falls back to the model's default. Write short sentences, not keyword lists, and no ambiguous words ("nice", "some", "a bit", "interesting").

1. **Format and purpose** - the use case: what kind of picture and its job: "Steam capsule key art, 16:9, must read as a small thumbnail".
2. **Subject** - who or what, its colour and texture, doing one clear thing. Paste the Character Card for a recurring character, or mention its saved Element with @.
3. **Place** - where, when, weather; only what the picture shows.
4. **Composition** - viewpoint, distance, where the subject sits ("in the right two thirds"), what is in front and behind, where empty space is kept. Positions need spatial words: left, right, foreground, between.
5. **Light and mood** - one light story (source, direction, colour) and one named mood.
6. **Text in the picture** - only if wanted (see below).
7. **Style** - the Style Card, pasted unchanged, last.

## Short form or labelled form

- **Short form** (under about 200 words): one subject, one place, little or no text. Longer free prose starts to contradict itself. When a result is vague, sharpen a clause; don't add clauses.
- **Labelled form** for a layout with several parts: a poster, a capsule with a title, a product shot, a picture that must keep a reference's identity. Dreamina's own Seedream 5.5 examples are written this way (2,500 to 4,500 characters; the limit is 5,000 on Seedream 5.5 and 5.0 Pro, 4,000 on Seedream 4.x, 7,000 on GPT Image):
  - an opening sentence with the format, ratio, purpose and look;
  - one short paragraph per part, each starting with its label (LAYOUT, BACKGROUND, SUBJECT, PRODUCT, LIGHTING, TYPOGRAPHY, or Lighting:, Background:, Overall mood:);
  - layout in percentages of the canvas ("keep 4-5% margins; the left 35% for the title, the right 55% for the subject");
  - for a reference: one sentence naming what to preserve ("Preserve the character's face, proportions, colours and marks from the reference picture");
  - every word to render in quotes, with its place, its size as a share of the canvas ("letter height 2-3% of canvas height"), colour and letter style, and "Spell every letter correctly";
  - a closing **Avoid:** paragraph of concrete defects (below).
- Never pad a short brief into the labelled form: length buys control of parts, not quality.

## Template

```
<Format and purpose>.
<Subject / Character Card / @Element>, <its colour and texture>, <one clear action>, in <place, time, weather>.
Composition: <viewpoint and distance>, <subject position>, <foreground / background>, <empty space for ...>.
Light: <source, direction, colour>. Mood: <one mood>.
<Text: "EXACT WORDS" in <letter style>, <colour>, <where>.>
Style: <Style Card>.
```

Labelled form:
```
Create a <ratio> <kind of picture> for <purpose>. <One line of look and mood>. <Preserve ... from the reference picture / @Element.>

LAYOUT: <margins and shares of the canvas in %; where each part sits; where empty space is kept>.
SUBJECT: <who or what, colour, texture, pose or action>.
<OTHER PART>: <one short paragraph per part: background, props, product>.
LIGHTING: <source, direction, softness, colour>.
TYPOGRAPHY: "<EXACT WORDS>" at <place>, letter height <n>% of canvas height, <colour>, <letter style>. Spell every letter correctly. No other wording.
STYLE: <Style Card>.

Avoid: <concrete defects: changed identity, extra limbs, misspelled text, borders, watermarks, ...>.
```

## Text in the picture

- Put the exact words in double quotes; unquoted words are read as description. Short phrases render best (1-5 words).
- Say the letter style in words, the colour and the place: `the title "MOSSWELL" across the top third in chunky hand-cut woodblock capitals, ink black`. Take the letter style from `typography-designer` or `look_up.py --table fonts`.
- Seedream 5.5, the 3.x models and the GPT Image models have a "Draw text on image" switch: turn it on when the picture carries words.
- Long or layout-heavy text: GPT Image 2 ("precise text rendering"), Ideogram 4.0 ("precise layouts and multilingual text") or Seedream 5.0 Pro ("optimized for cinematic and text-rich visuals"). End with "No additional wording, borders or watermarks."
- Check the spelling in every result.
- A logo is never generated: reserve the space ("clean empty band across the top third") and place the real logo in an editor. Steam capsules allow no text beyond the title.

## Colour

Write hex together with a colour name ("#C8553D brick red"). Hex works best on large areas (sky, ground, a cloak), not on small details.

## References

- Upload a reference when identity matters: a character, a prop, the anchor picture of a series. A reference beats any description of the same thing.
- Refer to each by what it shows ("the fox scout from the reference picture"), not by its number alone; numbers break when the set is reordered. If Dreamina inserts a tag when you type @, use that tag and still name its role.
- With a reference attached, describe only what is new: pose, place, composition, light. Do not describe the character again, or the two fight.
- Clean references work best: one subject, plain background, the angle you need. Two references that disagree give a blend of both.
- How many references a model takes (image-to-image, the CLI's model list, 2026-11-22): GPT Image 2.5 Flare and Sunburst 16; Nano Banana 2.1 14; Seedream 5.5 and 5.0 Pro 10; Seedream 4.x, Nano Banana Pro and GPT Image 2 6. Seedream 4.6 and 4.7 also take up to 14 in text-to-image.
- Say what each reference is for, and what to preserve from it: "Preserve the fox's face, proportions, fur colours and scarf from @FoxScout; take only the brush texture and palette from the second picture."
- **Saved Elements** (Assets & Elements, Elements tab): an approved subject or look saved once and mentioned with @ in any prompt, picture or video. Types: Character, Scene, Prop, Product, Style, Other. A name of up to 20 characters. Save each approved anchor as an Element; a prompt then names it ("@FoxScout standing on a mossy rock") and describes only what is new. An Element is a saved reference, not a trained model: the rules above still hold.
- **Visual to prompt** (All tools) writes a prompt from an approved picture. Use it to learn which words Dreamina reads from that picture, then keep only what matches the Style Card; never paste its output unchecked.

## Which image model

Seen on a paid plan, 2026-11-22. Credits are per picture and rise with resolution; "Unlimited" means the plan's Unlimited switch makes it free (up to 3 pictures a prompt).

| Use | Model | Sizes, pictures a run | Credits a picture |
|---|---|---|---|
| Tries, a series, transparent cut-outs | **Seedream 5.5** | 1.5K, 2K; 1-8 (3 when Unlimited); Background Auto/Opaque/Transparent | 6 (1.5K), 9 (2K); **Unlimited** at both |
| Free tries at 4K too | **Seedream 5.0 Flash** | 1.5K, 2K, 4K; 1-4 | 6, 6, 10; Unlimited at 1.5K and 2K |
| The final at the largest size, text-rich pictures | **Seedream 5.0 Pro** | 1.5K, 2K, 4K; 1-4; adds 9:21 | 9, 12, 18 |
| Cheapest drafts, character consistency | **Seedream 4.6 / 4.7** (4.6: "improved character consistency") | 2K, 4K; 1-8 | 2, 4 |
| Exact text, layouts, many ratios (1:2, 2:1, 4:5, 5:4, 1:3, 3:1) | **GPT Image 2.5 Flare / Sunburst** | 1K, 2K, 4K; 1; Quality Low-Max; Background setting | Medium 4-6 (Unlimited at 1K, 2K); High 17-30, Max 54-104 |
| Precise text | **GPT Image 2** | 1K, 2K, 4K; 1-4 | Medium 21-48, High 4K 180 |
| Consistent subjects, many references | **Nano Banana 2.1** | 1K, 2K, 4K; 1-4 | 12, 18 (both Unlimited), 37 |
| Multilingual text and layouts | **Ideogram 4.0 / 4.5** | 1K, 2K; 1; Quality | 4-16 at Medium |

- Start on an Unlimited model (Seedream 5.5 or 5.0 Flash) for tries; spend credits only on the final.
- Keep one model for one series: changing models changes the drawing hand.
- Quality (GPT, Grok, Ideogram) multiplies the price: Medium for tries, High only for a final that needs it.
- The resolution chosen stays when the model is switched; check it, because the price follows it.
- A kept picture that is only too small: Creative upscale (to 8K), not a new run on another model.
- Name the model, resolution, pictures a run and Background in the SETTINGS line (SKILL.md, "Output format").

## Editing a picture the user made

First check FEEDBACK.md, "The cheapest fix first": one wrong region is Smart edit, a crop is Expand image, a new angle is Angles. An edit prompt is for a change to the whole picture or a new shape of it.

One edit per prompt, then pin everything else:

```
Using the picture as reference: <the one change, described as the end state>.
Keep exactly: <silhouette / pose / camera angle / background / light / palette>.
```
Without the "keep exactly" line, things the user did not mention drift. "Make it better" fails: name the end state ("the well's stones are darker and wet, the windmill twice as large").

## Characters, poses and cut-outs

- **One picture per pose or side, never several in one picture.** A sheet gives each figure a fraction of the pixels and has to be cut apart by hand, and side views for 3D must be separate files anyway.
- **The first picture is the anchor.** Make one pose or side alone, full body, nothing cropped, and get it approved. Save it as a Character Element. Every other pose or side is its own generation with the anchor attached or the Element mentioned:
  ```
  Using the picture as reference: the same character <in the new pose | seen from the left side>. One character only, the same size in the frame.
  Keep exactly: the design, the proportions, the colours and every mark.
  ```
- Same canvas size and the same scale for every picture of the set.
- **Side views:** for a picture going to Tripo, Tripo's own Generate Multi-Views comes first (the `tripo-prompt` skill, when installed). Otherwise, and when Tripo's views drift, Dreamina's **Angles** tool (All tools, Camera & Motion) makes new camera angles of the same subject from the anchor; the edit prompt above is the fallback.
- **Transparent pictures:** on **Seedream 5.5**, set **Background: Transparent** in the settings bar (seen 2026-11-20). On other models, or when the edge is poor, generate on a flat single-colour background that appears nowhere in the character (white for a coloured character with dark outlines), with no ground line and no cast shadow, then use Dreamina's **Remove BG** tool. Transparency is a setting, never a word in the prompt. A picture going to Tripo stays on plain white or grey (Tripo's input rules).
- The approved anchor is the character's primary picture: scenes attach it (or mention its Element) and describe only the place, the pose and the light.
- A picture that will be turned into a 3D model in Tripo follows the `tripo-prompt` skill's INPUT-IMAGES.md (neutral pose, even light, no shadow, matching views), not the rules for a good-looking picture.
- A character that will be small on screen (an icon, a sprite) is drawn large and simple: few big shapes, one mark that identifies it, nothing that vanishes when scaled down.

## Refining

- Close: keep what works, change one clause, regenerate.
- Central idea missed: rewrite from the brief, not from the failed prompt.
- A local flaw in a good picture: Smart edit on that region, not a new generation (FEEDBACK.md, "The cheapest fix first").
- Exclusions: say what you want first ("plain flat background", "empty sky"). Dreamina has no negative-prompt box; its own examples end with an **Avoid:** paragraph inside the prompt. Use one in the labelled form, or after a defect has been seen: concrete things only ("Avoid: extra legs, a second scarf, misspelled title, watermark, white cutout halo"), never vague ones ("bad quality").

## Problems seen in still images

| Problem | Line to change |
|---|---|
| Wrong number of legs, fingers, ears, tails | State the count positively in the subject clause; one bad spot in a good picture is Smart edit |
| Looks like a photo or a 3D render | Remove lens and photo words; restate the medium first in Style |
| Two accent colours fight | Name one accent in the Style Card, call the rest muted |
| Subject too small for a thumbnail | "the subject fills two thirds of the frame", simpler background |
| Random letters or signs | "no lettering anywhere in the picture" (only after it appears) |
| Style drifts across a series | Attach the anchor picture or mention the Style Element; see SERIES.md |

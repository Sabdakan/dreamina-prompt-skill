# Style bridge: one look across every prompt

Consistency comes from four things used together, strongest first: an approved picture attached as a reference, a saved Dreamina Element (style or character), the same card text in every prompt, and words that match the medium.

## 1. The Style Card

One per project or series. Draft it from the project's own docs, get the user's yes, save it in `docs/dreamina/cards.md` with a version number, then paste it unchanged.

```
STYLE CARD - <project> - v<n>
Medium: <what it is made of: flat woodblock print / gouache painting / ink line over flat colour>
Line: <who gets outlines, how heavy, what colour>
Colour: <3-5 colours as hex + name, one marked ACCENT; "everything else muted">
Light: <the usual light story, one sentence>
Detail: <where detail goes and where it stops: sharp at the focal point, flat shapes at the edges>
Surface: <paper grain / brush texture / none>
```
Keep it to about 60 words: it rides in every prompt. Rules about what never appears stay in the skill's check list, not in the card, because exclusion words can summon the thing.

Where the fields come from: the project's own art docs (an art-direction page, a style guide, notes on approved pictures). PROJECT-NOTES.md names them per project. When the docs say nothing about a field, describe in words the qualities the user's reference pictures share, show that reading, and ask.

## 2. The Character Card

One per recurring character or creature type.

```
CHARACTER CARD - <name> - v<n>
Shape: <silhouette in one line: proportions, size against the world>
Counts: <four legs, one bushy tail, two pointed ears / two arms, five fingers>
Colour: <2-3 colours as hex + name>
Marks: <the fixed details: a torn left ear, a green scarf, a leather satchel>
Primary picture: <which approved picture is the reference> · Element: <@Name of the saved Character Element, if any>
Voice: <model> · <exact voice name from the library> · <how they speak: pace, pitch, two delivery tags they use most>
```
Once an approved picture exists, attach it (or mention its Element) and send only Counts and Marks as text: the picture carries the rest, and describing it again makes the two fight. The same card feeds `3d-prompt-engineer` or `tripo-prompt`, so the user's 3D model and Dreamina pictures match.

## 3. Match the words to the medium

Camera and film words pull Seedream and Seedance toward photographs and 3D renders. Use the vocabulary of the look being made.

| Look | Use | Leave out |
|---|---|---|
| Flat ink, woodblock, cel | flat shapes, layered flat planes, bold contour, limited palette, paper grain; in video: drawn animation, held poses, the frame slides across layers (parallax) | lens sizes, depth of field, bokeh, film stock, volumetric light, "photoreal", "8K" |
| Painted | brush texture, soft and lost edges, haze, warm and cool masses, painterly light | macro detail, HDR, lens flare |
| Printed, halftone | halftone dots, misregistered cyan and magenta, speed lines, flat black shadows | smooth gradients, glow |
| Photographic or rendered 3D (only when asked) | lens, aperture, depth of field, film stock, studio light | - |

Shot sizes (wide, close-up) and viewpoints (low, from above) are safe in every look.

## 4. Dreamina's own tools

- **Saved style or character: Dreamina's Elements** (Assets & Elements, Elements tab; seen 2026-11-20). Types: Character, Scene, Prop, Product, Style, Other. Each has a name of up to 20 characters, an Element Reference (the approved pictures) and a description, and is mentioned with @ in any prompt, picture or video. Make a **Style** Element from the approved anchor pictures once the final look exists, and a **Character**, **Prop** or **Scene** Element for each approved asset; paste the Style Card's Medium, Line and Colour lines into the description. Then name the Element in the prompt and shorten the card text to what must not drift. Record every Element's name in the project's cards file. In a series, the frame mentions the Style Element in every prompt (SERIES.md). It is a saved reference, not training: a picture that drifts is fixed by a stronger reference, not by rewording.
- **References:** each with a stated role; see IMAGE.md and VIDEO.md.
- **First and last frames:** for video, the approved stills.
- **Smart edit:** for one flawed area. The other fix tools (Expand image, Creative upscale, Remove BG, Angles, Visual to prompt, Separate layers) are routed in FEEDBACK.md, "The cheapest fix first".

Menu names change: describe what to pick in plain words.

## 5. Vocabulary and colours from ui-ux-pro-max

Needs the `ui-ux-pro-max` skill installed beside this one (a sibling folder in the same skills directory).

```
python "<skill folder>/scripts/look_up.py" "organic" --table styles
python "<skill folder>/scripts/look_up.py" "game" --table colors
python "<skill folder>/scripts/look_up.py" "playful" --table fonts
```
- **styles**: prompt keywords and colours per named style, as starting vocabulary to rewrite in the project's words.
- **colors**: palettes with exact hex, for a social series or a page that needs its own palette.
- **fonts**: pairings with mood words, for describing lettering.

The tables are made for websites and apps: take words and colours, never a layout. A project's own palette always comes from its art docs first.

## 6. Other skills

| Need | Skill | What to take |
|---|---|---|
| Lettering in a picture | `typography-designer` | The letter style in words |
| Naming a motion the user describes loosely | `animation-vocabulary` | The term, turned into a visible action |
| Several things moving in one beat | `choreograph` | The order: what moves first, what follows, what stays still |
| What a capsule or trailer hook must do | `game-marketer`, `steam-store-launch-ops` | Purpose and hook timing for the brief |
| Icons and cards readable at small size | `game-ui-ux` | Silhouette and contrast rules |
| The same character in 3D | `3d-prompt-engineer`, `tripo-prompt` | Shares the Character Card |

Load one only when the prompt needs it and it is installed. Seedance does not read easing names: turn every borrowed term into something seen ("the arm snaps past its rest and settles").

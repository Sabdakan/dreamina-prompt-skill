# Model notes: what the guides say, and what the user's Dreamina shows

Dreamina changes its models and limits often, and the guides disagree. A figure in the middle column is a claim; the right column is what the screen showed. Fill it the first time each fact comes up, by asking the user what their screen shows.

The right column was read on 20.11.2026 in Claude's browser pane, on a **free-plan** Dreamina login (120 credits). **The section "A paid plan and the CLI (22.11.2026)" below is newer and wins where they differ.**

## A paid plan and the CLI (22.11.2026)

Read on a paid "Advanced" account's screen, every model and mode opened without generating, and from Dreamina's CLI (`dreamina-canvas` 1.4.0: `model list`, `voice list`). Prices are credits, before the Unlimited switch; "list" = the struck-through price.

**Images (20 models on the screen; 13 callable from the CLI).** Per picture:
| Model | Sizes | Pictures a run | Credits | Unlimited | Prompt limit, references |
|---|---|---|---|---|---|
| Seedream 5.5 | 1.5K, 2K (CLI also lists 3K for members) | 1-8 | 6 / 9 (list 8 / 13) | yes, 1.5K and 2K, up to 3 a prompt | 5,000; 10 |
| Seedream 5.0 Flash | 1.5K, 2K, 4K | 1-4 | 6, 6, 10 | 1.5K and 2K | - |
| Seedream 5.0 Pro | 1.5K, 2K, 4K | 1-4 | 9, 12, 18 | no | 5,000; 10 |
| Seedream 5.0 Lite / 4.5 | 2K, 4K | 1-8 | 6, 8 | no | 4,000; 6 |
| Seedream 4.7 / 4.6 / 4.1 | 2K, 4K | 1-8 | 2, 4 | no | 4,000; 6 (4.6, 4.7: 14 in text-to-image) |
| Seedream 4.0, 3.1, 3.0 | 2K-4K; 1K-2K | 1-8; 1 | 2-4 (a few free uses) | no | 4,000 |
| GPT Image 2.5 Flare / Sunburst | 1K, 2K, 4K, Custom; 15 ratios incl. 1:2, 2:1, 4:5, 5:4, 1:3, 3:1 | 1 | Medium 4-6; High 17-30; Ultra 26-63; Max 54-104 | Medium at 1K, 2K | 7,000; 16 |
| GPT Image 2 | 1K, 2K, 4K | 1-4 | Medium 21 / 38 / 48; High 4K 180 | no | 7,000; 6 |
| Nano Banana 2.1 / Pro | 1K, 2K, 4K | 1-4 | 12, 18, 37 / 42, 42, 75 | 1K, 2K | 5,000; 14 / 6 |
| Grok Imagine 2.0, FLUX 3 Image, Ideogram 4.5 / 4.0 | 1K-2K | 1 | 12-55 | no | - |
- Background (Auto / Opaque / Transparent): Seedream 5.5 and the GPT Image models. "Draw text on image": Seedream 5.5, 3.x and GPT Image. No negative-prompt box, no seed, no prompt-enhance switch. The chosen resolution carries over when the model changes.
- Dreamina's own image examples (three "Try it" prompts on Seedream 5.5): 2,500-4,500 characters in labelled paragraphs, layout in percentages, quoted text with size and font, a "preserve the reference" sentence, and a closing "Avoid:" or "Negative prompt:" paragraph. Explore shows community prompts in both long prose and comma-tag styles.

**Video (31 models on the screen; 25 callable from the CLI).** Credits for the default length:
| Model | Length | Sizes | References (CLI) | Credits |
|---|---|---|---|---|
| Seedance 2.5 | 4-30 s | 480P, 720P, 1080P, 4K | 50: 30 images, 10 clips, 10 audio | 0 with Unlimited at 480P, 720P (list 85, 185); 1080P 455 |
| Seedance 2.5 Draft | 4-30 s | 480P | 50 | 0 with Unlimited (list 85) |
| Seedance 2.5 Flash | 4-30 s | 480P, 720P | 20 (screen); CLI 10 images, 5 clips, 5 audio | 0 with Unlimited (list 55, 120) |
| Seedance 2.0 | 4-15 s | 720P, 1080P, 4K | 12: 9 images, 3 clips, 3 audio | 1080P 205, 4K 490 |
| Seedance 2.0 Fast | 4-15 s | 720P-4K | 12 | 1080P 70, 2K 85, 4K 110 |
| Seedance 2.0 Mini | 4-15 s | 720P (CLI); screen also 1080P-4K | 12 | 1080P 55, 4K 95 |
| Seedance 1.0 / 1.0 Fast | 5-10 s | 1080P / 720P-1080P | first frame | 125 / 25-40 |
| Recreate / Recreate Lite | up to 30 s / 15 s | 720P | a template clip | 29 / 17 |
| Veo 3.1 / Fast / Lite | 8 s fixed; 16:9, 9:16 | 720P-4K | 3 images | 800-1,200 / 200-600 / 104-160 |
| Others (Wan 3.0, Grok Imagine, FLUX 3 Video, Vidu Q2-Q4, LTX 2.5, PixVerse 5-5.6, Luma Ray 3.2, HappyHorse 1.1, Gemini Omni) | 4-20 s | 360P-4K | 0-20 | 25-944 |
- Prompt limits: Seedance 2.5 family 15,000 characters; Seedance 2.0 family, Veo 4,000; Wan, FLUX 3 Video 20,000; PixVerse 512.
- Choosing a reference mode switches the model: Multiframes -> Seedance 1.0 Fast; Smart edit -> Seedance 2.5 Flash; Video recreator -> Recreate Lite; Long video -> Seedance 2.5 at 30 s.
- Dreamina's own video examples (three "Try it" prompts on Seedance 2.0 Mini): a one-line opener, time-coded beats ("0-1.5s:"), ACTIVE REFERENCES with "@image1 ... 100% matches the reference", shot sizes with field of view, "HARD CUT", dialogue in quotes with delivery notes, an AUDIO section with a BPM beat grid, LIGHTING, OUTPUT, POSITIVE LOCKS and an Avoid list.

**Audio.** AI Audio modes: Omni audio (SeedAudio 1.0) and Voiceover (ElevenLabs v3, v4, MiniMax Speech 2.8 HD, Turbo, Seed TTS). AI Music is a separate mode: MiniMax Music 3.0, 35 credits shown. Prompt limits: ElevenLabs v4 and MiniMax 10,000; ElevenLabs v3 2,000; SeedAudio 3,000; Seed TTS 600. Voices: ElevenLabs 105, Seed TTS 24, MiniMax and SeedAudio 13. Tags: ElevenLabs square brackets (a preset list plus free phrases), MiniMax round brackets (vocal sounds only), Seed TTS none. SeedAudio takes up to 3 audio references or 1 image (not both) and timestamps for speech, effects and music. AUDIO.md has the details.

**Tools (All tools).** Smart edit, Creative upscale (images to 8K, video to 4K), Video recreator, Edit segment, Visual to prompt, Extend video, Reframe video (6 ratios), Video dubbing (9 languages and more), Create avatar, Remove BG, Image resizer (up to 8 sizes at once), Expand image, Separate layers, Recreate image, Look swap, Localize image, Angles, Relight, Panorama, 3D Director Console, Motion capture, Clay renderer (Blender and Maya). The CLI adds video interpolation to 30 or 60 fps (free for members) and depth capture.

**Not read yet:** the plan page, queue and concurrency limits, Create avatar's panel, Seedance 2.5 at 4K, the length controls of Veo, LTX, PixVerse and Luma.

## As seen in the user's Dreamina

| Fact | Per the guides (read 2026-11-19) | Seen on the screen (20.11) |
|---|---|---|
| Image models offered | Seedream 5.0 Pro, 5.0 Lite, 4.x | Seedream 5.5 (default), 5.0 Pro, 5.0 Flash, 5.0 Lite, 4.7, 4.6 ("improved character consistency, efficient on credits"), 4.5 ("reliable character and style consistency"), 4.1, 4.0 ("multiple references and batch generation"), 3.1, 3.0; GPT Image 2.5 Flare, 2.5 Sunburst, 2; Nano Banana 2.1 ("consistent subjects"), Nano Banana Pro; Grok Imagine 2.0; FLUX 3 Image; Ideogram 4.5, 4.0 |
| Seedream 5.5 | - | **6 credits a picture** (8 struck through), **4 pictures a run**, 1.5K or 2K (no 4K, Custom greyed), ratios Auto, 1:1, 3:4, 16:9, 4:3, 9:16, 2:3, 3:2, 21:9. **Background: Auto / Opaque / Transparent.** A "Draw text on image" switch |
| Seedream 5.0 Pro | - | **9 credits a picture, 2 pictures a run**, 1.5K, 2K or **4K**, ratios as above plus 9:21. No background switch |
| Image references per prompt | Up to 10 on 5.0 Pro (Runware); 6 on 4.0 | The box takes uploads (the + square) and **@ to mention elements**; the count per model was not shown without an upload |
| Negative prompt box for images | None in the API; exclusions go in the prompt | None on the screen |
| Transparent output / background remover | No real transparency from the model | **Seedream 5.5 has Background: Transparent.** A separate **Remove BG** tool ("keep the subject, drop the rest") and **Separate layers** ("split images into editable layers") |
| Saved style and characters | The user says Dreamina has it; no help page found | **Elements** (Assets & Elements, Elements tab): types Character, Scene, Prop, Product, Style, Other. Set up: a name of up to 20 characters ("so you can mention it with @"), a type, an Element Reference (upload, or pick from Assets), a description. Its note: "Save an element to keep results consistent. Reuse it anytime with "@" to maintain style, characters, or key elements across your creations." It is a saved reference, not a trained model. None saved yet on this login |
| Other image tools | - | Smart edit ("target every edit with precision"), Creative upscale (to 8K), Expand image, Image resizer, Recreate image ("make the style yours"), Look swap ("restyle your character"), **Angles** ("generate new camera angles from a reference image while keeping your subject visually consistent"), Relight, **Visual to prompt** ("turn an image or video into a prompt you can use to create similar visuals"), Clay renderer (a Blender and Maya plugin), Canvas |
| Unlimited image generation | Dreamina's offer of 9 to 16.11.2026: eligible paid plans got credit-free generation per model (Seedream 5.0 Flash for 180 or 365 days, others for days). Basic monthly excluded | On the free login: none active. Pop-ups offer "Up to 30-Day Unlimited Gen" of Seedance 2.5 with a plan, and up to 83% off credits for Black Friday. A paid account's plan page shows what is active |
| Video models offered | Seedance 2.5, 2.0, 2.0 Mini | Seedance 2.5 Flash ("faster, fewer credits"), **2.5 Draft (480p drafts to test ideas before spending more credits)**, 2.5 ("up to 50 references"), Recreate and Recreate Lite (motion transfer, object swap; 30 s and 15 s), 2.0 Mini (default), 2.0 Fast, 2.0, 1.0, 1.0 Fast; also Veo 3.1 (and Fast, Lite), Gemini Omni, Wan 3.0, Grok Imagine Video, FLUX 3 Video, Vidu, LTX 2.5, PixVerse, Luma Ray 3.2, HappyHorse |
| Video entry modes | First and last frame; all-reference (Omni) mode | **Omni reference** (default), First and last frames, Multiframes, Smart edit, Long video, Video recreate |
| Video references | Up to 9 pictures, 3 clips, 3 audio files, 12 files together (2.0); "up to 50" (2.5 page) | 2.0 Mini: "Upload up to **12 references**, mixing images, videos, and audio, or use @ to mention elements" |
| Clip length per generation | 4-15 s (2.0); up to 30 s (2.5 page) | 2.0 Mini: a slider to 15 s, default 5 s; 16:9, 720P; **25 credits** for 5 s (60 struck through) |
| Reference tag in the prompt | @Image1, @Video1, @Audio1; typing @ opens the picker | Typing @ mentions uploads and saved Elements |
| Extending a clip | Supported | "Extend video" tool ("continue the shot naturally") |
| Realistic human faces in uploads | Blocked on the Chinese platform | Not checked |
| Sound | Generated with the clip | Not checked |
| Agent access | - | "Plugins & CLI: create with Dreamina in your Agent" (not used: Claude makes no art) |

## Where these facts change the instructions

- SETTINGS line (SKILL.md, "Output format"): model, ratio, resolution, pictures a run, Background on Seedream 5.5, any Element to mention with @.
- Model choice: IMAGE.md, "Which image model"; VIDEO.md, "Which video model" (test on 2.5 Draft, keeper on the full model).
- Ratios and sizes: FORMATS.md (no 4:5 and no 2:1 on the screen: generate at the nearest and crop).
- Elements: SKILL.md workflow step 7, IMAGE.md "References", SERIES.md step 1 and 4, STYLE-BRIDGE.md section 4.
- Fix tools: FEEDBACK.md, "The cheapest fix first".
- Video modes and reference tags: VIDEO.md, "Modes" and "References".

## The paid-plan screen pass (done on 22.11.2026, above; repeat it after a big Dreamina update)

On 20.11 only a free-plan login was read, and the info icons were not opened. When the paid plan is bought, read the whole screen again, read-only (nothing that spends credits without the user's word):

**How to read:** hover every "?" and "i" icon and copy its tooltip; read every badge (New, Beta, a struck-through price, the blue mark beside a setting); for every greyed option, read why it is greyed; read placeholders and empty-state lines; open every menu and scroll it to its end; after each setting change, read the credits beside the Generate arrow; read the small print of banners and pop-ups. Write each fact into the table above with the date.

**What to read:**
1. The plan: its name, credits and renewal, which models are free or unlimited and until when, the queue and how many tasks at once.
2. AI Image, model by model: credits a picture, pictures a run, sizes, ratios, the Background setting, "Draw text on image", the tooltip of each control, and the model's own tooltip in the list.
3. References: how many pictures the + box takes on each model (the user drops one test picture in; reading the box costs nothing), what @ offers.
4. Elements: the Set up element form's every field and hint, how many pictures one Element takes, how a saved Element shows in the @ list.
5. All tools, one by one, opened without running: Angles, Remove BG, Separate layers, Smart edit, Creative upscale, Expand image, Recreate image, Look swap, Relight, Visual to prompt, Image resizer: each one's controls, tooltips and price. Tools that show controls only after a picture: the user drops one test picture in.
6. AI Video, model by model: credits a second, lengths, sizes, the mode menu (Omni reference, First and last frames, Multiframes, Smart edit, Long video, Video recreate) and each mode's tooltip, references a model takes, the sound setting.
7. Canvas, Marketing Studio, Motion Studio, Drama Studio: what each is for, read from its own screen.
8. Plugins & CLI: what it offers (read only; Claude makes no art).

## Points where the guides disagree

- **Image prompt length:** Dreamina's own article says it has "no word limitations"; fal (5.0 Lite) advises under about 200 words, Runware (5.0 Pro) under 600. The skill uses 200.
- **Image formula order:** Dreamina's article: the use case, then subject, description (colour, texture, action), style, context; short sentences, no ambiguous words. Runware puts format first and style last; fal puts subject first. The skill uses format and purpose (the use case), subject with its colour, texture and action, place, composition, light, text, style. It matches Dreamina's order except that place comes before style, as in Runware.
- **Text in pictures:** fal says double quotes are required; Runware's examples use plain capitals. The skill uses double quotes. Seedream 5.5 also has the "Draw text on image" switch.
- **Reference tags:** the guides write @Image1; the Seedance 2.5 page writes @Image 1. Use whatever tag Dreamina inserts when @ is typed, and name its role in words.
- **Clip length and reference counts:** see the table. Nothing longer than 15 s or with more than 12 references is planned until the user's paid account shows more.

## Sources

- The user's Dreamina, read in Claude's browser pane on 20.11.2026 (free-plan login): the AI Image and AI Video panels, the model lists, the size menus, Assets & Elements, All tools.
- Dreamina: "text-to-image prompts" article (dreamina.capcut.com/resource/text-to-image-prompts), the Seedance 2.5 page (reference tags @Image 1, @Video 1, @Audio 1, timecoded shots "0-4s: ..."), the pricing page (read 17.11 by a helper). Seedream 4.0's page at seed.bytedance.com: edits by plain instruction ("Remove the boy in this picture."), "Keep the colour scheme ... unchanged".
- Runware: Seedream 5.0 Pro prompting guide. fal: Seedream 5.0 Lite prompting guide. Provider pages about the same models through an API.
- songguoxs/seedance-prompt-skill (GitHub): community skill for Seedance 2.0 on the Chinese platform.
- Steamworks: store assets and library assets pages.
- Not read: BytePlus' official Seedream guide (its body did not load on 19.11 or 20.11) and Dreamina's YouTube tutorials.

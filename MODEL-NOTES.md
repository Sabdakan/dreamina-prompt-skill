# Model notes: what the guides say, and what the user's Dreamina shows

Dreamina changes its models and limits often, and the guides disagree. A figure in the middle column is a claim; the right column is what the screen showed. Fill it the first time each fact comes up, by asking the user what their screen shows.

The right column was read on 20.11.2026 in Claude's browser pane, on a **free-plan** Dreamina login (120 credits). A paid plan may show more models, sizes or free allowances.

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

## The paid-plan screen pass (the next read of the user's Dreamina)

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

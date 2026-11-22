# How to use the Dreamina prompt skill

This is your guide. The skill writes the prompt and tells you which settings to pick. You run it in Dreamina. Claude makes no pictures.

---

## The short version

1. Say **what it is, where it goes, and the moment**.
2. Copy the prompt block into Dreamina, set the settings shown above it, and generate.
3. Come back with a **verdict, what is right, what is wrong**, and paste the picture.
4. One thing is changed per round. When it is right, say **"kept"**, and save it as an Element.

Everything else in this guide makes those four steps work better.

---

## 1. Asking for a prompt

Give five things. One line each is enough.

| # | Tell me | Example |
|---|---|---|
| 1 | The project | Mosswell (a village-building game) |
| 2 | What it is and where it goes | Steam main capsule / TikTok teaser / upgrade card picture / a cosy cafe poster for Instagram |
| 3 | The moment: who does what, where | The fox scout hauls a bucket up from the old stone well |
| 4 | What the viewer must notice first, or feel | The bucket; busy and cheerful |
| 5 | What you already have | An approved picture, a saved Element (its name) |

**Good:** "Dreamina prompt for Mosswell: Steam main capsule. Two foxes haul a bucket up from the old stone well by the windmill, late afternoon. The eye goes to the bucket. I have no approved picture yet."

**Weak:** "Make a cool capsule for my game." It works, but I must guess the moment, and the moment is what makes a picture good. Style words do not rescue a dull moment.

If you leave something out, I pick it and show it on the **ASSUMED** line. Correct that line if my guess is wrong.

**Describe what is seen, not how it should feel.** "Epic" and "cinematic" give the model nothing. "A small fox in front of a windmill ten times its height, seen from below" gives it everything.

**You may name another game or film to me** ("the mood of ..."). I turn it into qualities in words and show you my reading. The name itself never goes into a prompt: it pulls the result toward a copy.

---

## 2. What you get back

```
SETTINGS   model, ratio, resolution, pictures a run, Background, duration and mode, and any Element to mention with @
UPLOAD     which picture to attach, and what it is for
ASSUMED    what I chose for you
PROMPT     one block: copy all of it
IF IT COMES OUT WRONG    the likely problems and the one line to change, or the Dreamina tool to use
```

- Copy the whole prompt block. Do not shorten or reword it: the card text inside is what keeps your pictures matching.
- Set SETTINGS and UPLOAD by hand in Dreamina before generating. **Background: Transparent** (Seedream 5.5 only) is how you get a cut-out; the word "transparent" is never in the prompt.
- **Seedream 5.5** (6 credits a picture, 4 a run, up to 2K) is for tries and cut-outs. **Seedream 5.0 Pro** (9 credits a picture, 2 a run, up to 4K) is for a final at the largest size. Keep one model for one series.
- One good picture out of four means the prompt is right.
- For video, test on **Seedance 2.5 Draft** (480p, cheaper). When the draft is right, run the same prompt on the full model.

---

## 3. Telling me how it came out

This is where prompts get good. Three parts:

1. **Verdict:** kept / close / wrong.
2. **What is right**, so I keep it: "the well and the light are right".
3. **What is wrong, as you see it:** "the fox looks like a shiny 3D toy", "one fox has two tails", "the foxes are too small".

**Paste the picture into the chat.** I can look at it, and I find more than a description gives me. For a clip, paste a frame or two.

| Say this | Not this |
|---|---|
| "close: the fox looks 3D and shiny; the well and light are right" | "make it better" |
| "wrong: too busy, I can't find the bucket" | "more epic" |
| "the character's scarf changed from green to blue" | "the character is off" |
| "the camera spins, I asked for a slow push-in" | "the video is bad" |

Name the **one or two biggest problems**, not ten. I change one thing per round and tell you which line changed, so you can see what each change does. If three rounds do not help, I stop tweaking and change the method.

When a result is right, say **"kept"**. I log it, and what fixed it becomes a lesson for next time.

---

## 4. Phrases the skill understands

| You say | You get |
|---|---|
| "Dreamina prompt for ..." | One prompt |
| "three variants" | Three complete prompts that differ in moment, angle or mood |
| "new character: a fox scout, three poses, transparent" | One picture per pose or side, each made from the first approved one, with Background: Transparent on Seedream 5.5 |
| "same picture as a vertical capsule" / "change the sky to dusk" | An edit prompt: one change, everything else pinned (or Expand image, when only the shape changes) |
| "fix just the tail" / "it's cropped" / "make it bigger" / "show it from the side" | The Dreamina tool to use: Smart edit, Expand image, Creative upscale, Angles |
| "series: all the upgrade cards" | An anchor prompt first, then a sheet with one prompt per card |
| "animate this still: the bucket comes up and splashes" | A video prompt that uses your picture as the first frame |
| "make it 25 seconds" | The clip split into segments that extend each other |
| "new character card for the miller" | A Character Card for your approval |
| "update the style card: darker, less red" | A new card version; old pictures are noted as made under the old one |
| "my Dreamina shows: Seedance 2.5, up to 15 s, ratios ..." | The skill's model notes corrected, plans adjusted |
| "kept" / "that fixed it" / "log it" | The round logged |
| "shorter" | The same prompt with fewer clauses; subject, counts and card stay |
| "voice lines for the fox: excited, whispering, tired" | A voice script with delivery tags in the model's brackets, one voice per character |
| "narration for the trailer" | A narration script with a tone tag per sentence |
| "menu music, calm, loopable" | A music description, Style chips and settings |
| "trailer shot, 8 seconds, cut on the music" | The director's block: references, timed shots, audio, locks |
| "what can Seedance 2.5 do?" | The live limits from Dreamina's CLI, when it is installed |
| "put it in Dreamina" | The prompt saved as a card on your Dreamina canvas (no credits) |
| "run it" | The price first; it runs only after your yes, with that credit limit |

---

## 5. The right order of work

For a new project or a new look, this order saves the most generations:

1. **Setup (once).** The models, sizes, credits per picture, video modes and Elements were read from Dreamina's screen on 2026-11-20 (MODEL-NOTES.md). Tell me what your plan adds: free or unlimited models and until when, and the Elements you save.
2. **Cards.** I draft the Style Card and the Character Cards from the project's art docs. You approve or correct them. They are then pasted unchanged into every prompt.
3. **One anchor picture.** We work on one typical picture until you are happy. This picture defines the look better than any words. Save it as an Element.
4. **Everything else from the anchor.** Series, capsule shapes and social posts attach the anchor or mention its Element.
5. **Video last, from approved stills.** A clip that starts from your picture keeps your look. A clip from text alone drifts.

---

## 6. Habits that give better results

- **Approve cards before a series.** Changing the style after 40 cards means redoing 40 cards.
- **One change per round.** Two changes at once and nobody knows which one worked.
- **Always say what to keep.** What is not pinned may change.
- **Attach a picture when identity matters.** A reference beats any description of a character.
- **One picture per pose or side.** Approve the first picture of a character, then make every other pose or side as its own picture with the first one attached. Never several in one picture: each would be too small, and side views for 3D must be separate files. For transparent pictures, use Seedream 5.5 with Background set to Transparent, or generate on a plain background and use Remove BG. For a new camera angle, try the Angles tool first.
- **Save what you approve as an Element** (Assets & Elements): a short name (up to 20 characters), the type (Character, Scene, Prop, Product, Style, Other), the approved pictures. Then type @ and its name in any prompt, so every later picture and video starts from the same design.
- **Fix small flaws with a tool, not a new generation:** Smart edit for one region ("the fox has one bushy tail"), Expand image for a crop, Creative upscale for size, Remove BG for the background.
- **Visual to prompt** shows which words Dreamina reads from an approved picture. Bring its output to me to check against the card; do not paste it unchecked.
- **Keep text short.** Up to five words can be generated. A logo is always placed in an editor.
- **Judge cards at their real size.** A card picture that reads at 128 px is right; a pretty one that does not is wrong.
- **One piece of work per chat.** The cards and the log live in the project's folder, so a new chat continues where the last one stopped.

---

## 7. When something keeps going wrong

| Problem | Tell me | What I will do |
|---|---|---|
| Every picture looks like a photo or 3D | "looks 3D" | Take out camera words, put the medium first, attach the anchor |
| The style drifts across a series | "card 12 does not match" + both pictures | Fix the frame once, not card by card; mention the Style Element |
| The character changes | "the character looks different" + the picture | Attach the primary picture or its Element, repeat the fixed marks |
| The clip morphs or melts | "it melts when they move" | Smaller, slower motion, closer shot |
| Prompts feel too long | "shorter" | Cut secondary detail first |
| Dreamina refuses or lacks a setting | "my Dreamina shows ..." | Replan inside what it offers |

---

## 8. What the skill does not do

- It never draws anything itself: pictures, clips, voices and music are made by Dreamina on your account.
- Without Dreamina's CLI it does not operate Dreamina. With the CLI it places a prompt on your canvas when you ask, and runs one only after you approve its price, every time (CLI.md).
- It knows your Dreamina's limits only as far as MODEL-NOTES.md records them. Until your screen shows more, it plans inside the smaller numbers.
- It never puts artists, studios, films or other games into a prompt, and never uploads a reference picture you shared only for reading a look, unless you say so.
- Steam screenshots must be real gameplay, so it writes no prompts for those.

---

## Where things live

- The skill: its own folder in your Claude skills folder (for example `~/.claude/skills/dreamina-prompt/`).
- Your own project rules, if you keep any: `PROJECT-NOTES.md` beside the skill's files. It is personal and wins over the skill's defaults.
- Per project, created on first use: `docs/dreamina/cards.md` (approved cards and Element names), `docs/dreamina/prompt-log.md` (rounds and lessons), and prompt sheets for series.

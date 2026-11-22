# Worked examples

Complete answers in the skill's output format. The project ("Mosswell", a cosy village-building game), its cards and its colours are made up for the examples: real ones come from the project's `docs/dreamina/cards.md`.

Example cards used below:

```
STYLE CARD - Mosswell - v1
Medium: flat storybook illustration in flat gouache colour. Line: dark brown ink outlines of varying weight on characters and the main object only.
Colour: #C8553D brick red (ACCENT), #F2E8CF cream, #6A8D73 sage green, #3D3B30 dark umber; everything else muted.
Light: low warm sun from the left, one flat shadow tone. Detail: sharp at the focal point, plain shapes at the edges.
Surface: fine paper grain over everything.

CHARACTER CARD - Fox scout - v1
Shape: small upright fox, large head, bushy tail, small against the well and the windmill.
Counts: two arms, two legs, one bushy tail, two pointed ears.
Colour: #D9813B fox orange fur, #6A8D73 sage green scarf.
Marks: a sage green scarf, a leather satchel on the left hip, a white tip on the tail.
Primary picture: not yet approved · Element: none yet
Voice: ElevenLabs v4 · a young-adult voice picked in the Voice library · quick and bright, a little breathless; [excited], [whispering]
```

---

## 1. Main capsule key art - Mosswell - Image

SETTINGS  Model: Seedream 5.5 · Ratio: 16:9 (target 1232 x 706) · Resolution: 2K · Pictures: 4 · Background: Opaque · Mode: text · Element: none
UPLOAD    nothing
ASSUMED   two foxes at the well; late afternoon; title space top left

PROMPT
```
Key art for a village-building game's store capsule, 16:9, must read as a small thumbnail.

Two small upright foxes, each with two arms, two legs and one bushy tail, wearing sage green scarves, haul a dripping brick red bucket up from an old stone well by its rope, mid-effort.

The well stands on a grassy rise at the edge of a fantasy village, a tall wooden windmill turning behind it, at late afternoon.

Composition: low viewpoint at knee height looking up, the well and the foxes fill the right two thirds, the windmill rises behind them, a calm empty band of sky across the top left.

Light: low warm sun from the left, long flat shadows. Mood: busy and cheerful.

Style: flat storybook illustration in flat gouache colour; dark brown ink outlines of varying weight on the foxes and the well only; #C8553D brick red as the single accent, #F2E8CF cream, #6A8D73 sage green, #3D3B30 dark umber, everything else muted; one flat shadow tone; sharp detail at the bucket, plain shapes at the edges; fine paper grain over everything.
```

IF IT COMES OUT WRONG
- A fox has extra arms or looks like a dog on all fours -> move the count sentence to the very start of the subject paragraph and cut to one fox
- Looks soft-shaded or 3D -> start the Style paragraph with "Flat colour shapes with no gradients"
- Foxes too small in a thumbnail -> "the well and the foxes fill three quarters of the frame", the windmill only a shape at the edge
- Right, but the store needs a larger file -> Creative upscale on the kept picture, not a new run on another model

The logo goes in the empty band in an editor. When a picture is kept, save it as an Element (Style: "MosswellStyle"; Character: "FoxScout").

---

## 2. Vertical capsule - Mosswell - Edit

SETTINGS  Model: Seedream 5.5 (same as the key art) · Ratio: 3:4, crop to 748 x 896 · Resolution: 2K · Pictures: 4 · Background: Opaque · Mode: reference · Element: none
UPLOAD    the approved main capsule -> the picture to re-frame

PROMPT
```
Using the picture as reference: re-frame it as a tall 3:4 composition, the well and the two foxes in the lower two thirds, more sky and the top of the windmill above for a title.

Keep exactly: the two foxes, their poses, the bucket, the well, the drawing style, line weight, palette and light direction.
```

IF IT COMES OUT WRONG
- The foxes are redrawn differently -> skip the prompt: run Expand image on the approved picture, adding sky above; it extends the canvas without redrawing what is there

---

## 3. Teaser shot "The bucket comes up" - Mosswell - Video (still first)

SETTINGS  Model: Seedance 2.5 Draft for the test, then Seedance 2.5 with the same prompt and upload · Ratio: 9:16 · Resolution: 480p (Draft), then the model's default · Duration: 8 s · Mode: First and last frames (first frame only) · Element: none
UPLOAD    the approved 9:16 still of the foxes at the well -> first frame (@Image 1)

PROMPT
```
8 seconds, 9:16, single take. @Image 1 is the first frame.

The two foxes from the frame pull the rope hand over hand; the brick red bucket rises over the rim of the well, tips, and splashes water across the stones. The foxes lean back and grin.

Small motion: the windmill's sails turn slowly, the grass sways, water drops sparkle where the bucket tips.

Camera: wide shot at knee height, slow push-in toward the well, drawn animation with held poses.

Timing: 0-3s: the pull, the rope tightens. 3-5s: the bucket rises over the rim and tips. 5-8s: the foxes lean back, the frame holds still.

Sound: wind and birdsong, a wooden creak on each pull, a bright splash when the bucket tips, no music.

Keep the flat drawn style, palette and line of the first frame; two foxes, each with one bushy tail; no cuts; no captions.
```

IF IT COMES OUT WRONG
- It turns 3D or photographic -> add "flat colour shapes, no shading changes" to the camera line
- Arms melt during the pull -> smaller motion: "the foxes give the rope two short pulls"
- The bucket never tips -> give the tip its own beat: "3-5s: the bucket rises over the rim. 5-6s: it tips and water splashes the stones"
- The Draft is right -> run the same prompt and upload on Seedance 2.5; change nothing else

---

## 4. Series: a frame and three slots

SETTINGS  Model: Seedream 5.5 for the whole series · Ratio: 1:1 (target 1024 x 1024) · Resolution: 2K · Pictures: 4 · Background: Opaque · Mode: text · Element: @MosswellStyle

`frame.txt`:
```
Square upgrade-card picture for a village-building game, shown at 128 px, must read in silhouette.
Match the drawing style, line weight, palette and background of @MosswellStyle.
New subject: {subject}.
Composition: centred, the subject fills about 70% of the frame, flat #F2E8CF cream background, no ground line.
Light: one soft light from the upper left. Mood: clear and sturdy.
Style: flat storybook illustration, dark brown ink outlines of varying weight, #C8553D brick red as the single accent, fine paper grain.
```
`items.csv`:
```
id,name,subject
sturdy_walls,Sturdy walls,a short dry-stone wall three stones high with one brick red stone in the middle
lucky_harvest,Lucky harvest,a wicker basket of golden wheat with a brick red ribbon on the handle
swift_boots,Swift boots,a pair of brown leather boots with small white wings at the heels
```
@MosswellStyle is the Style Element saved from the approved anchor picture (13 characters; names are up to 20). Without the Element, upload the anchor as the style reference for every item and write "of the reference picture" in the frame.

---

## 5. A result round

The user: "close, but the fox looks like a shiny 3D toy and one has two tails. The well and the light are right."

Answer:

Two things are off: the medium (3D shine) and one tail count. Changing the medium first, because it is the bigger miss and needs a new generation. The second tail is a local flaw: if it is still there in a picture that is otherwise right, it is fixed with Smart edit, not another round.

Changed line (Style, now opening with the medium):
```
Style: flat colour shapes with no gradients and no shine, a storybook illustration; dark brown ink outlines ...
```
Kept: the well, the composition and the light, exactly as before.
If the second tail comes back: Smart edit on that fox's tail, one line: "the fox has one bushy tail".

Logged in `docs/dreamina/prompt-log.md`: main capsule, round 2, "close", medium first in Style.

---

## 6. Fox scout side view, cut-out - Mosswell - Character set

SETTINGS  Model: Seedream 5.5 · Ratio: 2:3 (target 1024 x 1536) · Resolution: 2K · Pictures: 4 · Background: Transparent · Mode: reference · Element: @FoxScout
UPLOAD    nothing (the Character Element carries the approved front view)

PROMPT
```
Character picture for a game's character screen, 2:3, the full figure must read at small size.

@FoxScout seen from the left side, standing still, arms relaxed, the whole body in the frame from the ears to the feet, the same size in the frame as the front view. One character only, on a plain empty background, no ground line, no cast shadow.

Keep exactly: the design, the proportions, the colours and every mark: the sage green scarf, the leather satchel on the left hip, the white tip on the tail.
```

IF IT COMES OUT WRONG
- The edge is ragged or bits of background stay -> Background: Opaque with "flat white background", then Remove BG
- The design drifts from the front view -> also upload the approved front view as the reference, and keep the @ mention
- A three-quarter or back view is needed -> Angles on the approved front view first; this prompt is the fallback

The word "transparent" is not in the prompt: the Background setting does it. When the side view is approved, add it to the @FoxScout Element's references.

---

## 7. Fox scout voice lines - Mosswell - Voice

SETTINGS  Mode: Voiceover · Model: ElevenLabs v4 · Voice: <the name on the Character Card>
UPLOAD    nothing

SCRIPT
```
Fox Scout
[excited, a little breathless] The well's working again! Come and see!

Fox Scout
[whispering] Shh. Something's moving behind the windmill.

Fox Scout
[curious] [slowly] Huh. That bucket wasn't there yesterday.

Fox Scout
[tired] [sighing] One more trip to the river... then supper.
```

IF IT COMES OUT WRONG
- Lines sound alike -> one stronger tag per line, and a short free phrase: [hushed, glancing over a shoulder]
- The voice is too old or too deep -> pick another voice with the Age filter on Young adult; record it on the Character Card
- A tag is spoken aloud -> check the model: square brackets are for ElevenLabs only

Each line is its own file for the game (one generation per line), so barks can be triggered one by one.

---

## 8. Village theme - Mosswell - Music

SETTINGS  Mode: AI Music · Model: MiniMax Music 3.0 · Instrumental: on · Style: Indie Folk, Peaceful Relief, Nylon Guitar, Felt Piano, Airy Highs
UPLOAD    nothing

PROMPT
```
Gentle instrumental village theme for a cosy building game menu, about 90 BPM. Nylon guitar picks a warm, simple melody over soft felt piano chords, a light shaker joins halfway. Peaceful and hopeful, unhurried, sparse enough to sit under a voice. A steady loopable groove that ends where it began.
```

IF IT COMES OUT WRONG
- Too busy -> drop to two instruments and add "Sparse" from the Texture chips
- Feels sad -> swap the mood chip to Peaceful Relief or Quirky; "bright major key"
- The end does not loop -> trim the loop in an editor at a bar line; the model does not promise a seamless loop

---

## 9. Trailer beat - Mosswell - Video (the director's block)

SETTINGS  Model: Seedance 2.5 · Ratio: 16:9 · Resolution: 720P (free with Unlimited) · Duration: 8 s · Mode: Omni reference · Element: @FoxScout
UPLOAD    @Image 1: the approved key art of the well (the place) · @Audio 1: the village theme from example 8

PROMPT
```
An 8-second 16:9 trailer beat in the flat storybook look of @Image 1, warm and playful.

ACTIVE REFERENCES
@FoxScout: the fox scout. 100% matches the reference.
@Image 1: the stone well and the windmill. Keep its drawing style, palette and paper grain.
@Audio 1: the music. Cut on its beats.

SHOTS
0.0-3.0s - wide: @FoxScout runs in from the left and skids to a stop at the well, dust puffing at each step. Slow slide right.
3.0s HARD CUT. 3.0-5.5s - close-up: the fox hauls the rope, ears flat with effort; the bucket rises into view, dripping.
5.5-8.0s - medium: the fox lifts the full bucket overhead, water sparkling; hold on this pose.
Cuts only at the specified points.

AUDIO: @Audio 1 as the music; a rope creak on each pull; one splash at 5.5s. No voice-over.
OUTPUT: 16:9, 8 seconds.

POSITIVE LOCKS: @FoxScout looks the same in every shot: the sage green scarf, the satchel, the white tail tip.
Avoid: lens or photo look, extra characters, a second scarf, text, logos, watermarks.
```

IF IT COMES OUT WRONG
- It looks like a 3D render -> remove "trailer" energy words; repeat "keep the flat drawing style of @Image 1" in POSITIVE LOCKS
- The cut misses the beat -> give the beat grid in AUDIO ("one beat every 0.67 s from 0.0 s") and land the cut on a beat time
- Test first on Seedance 2.5 Draft with the same prompt; run the keeper only when the draft is right

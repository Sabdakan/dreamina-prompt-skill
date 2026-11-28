# Video: Seedance

Built from Dreamina's Seedance 2.5 page and its examples, CapCut's Seedance 2.0 Mini formula, a community Seedance 2.0 skill, and, on 2026-11-22, a paid account's screen, Dreamina's own "Try it" video prompts and its CLI's live model list. Limits change; see MODEL-NOTES.md and use what the user's Dreamina shows.

## Still first, then motion

The strongest way to keep a clip on the project's look:

1. Make the opening frame as a Seedream picture (IMAGE.md) with the Style and Character Cards. The user approves it.
2. Give that picture to Seedance as the first frame (First and last frames mode; add a last frame when the ending matters).
3. The video prompt then says only what moves, how the camera moves, the timing and the sound. It does not describe the look again: the frame carries it, and a second description invites drift.

Write a text-only video prompt (all eight parts, Style Card included) only when there is no frame to start from.

## Assets first (every clip with characters or a set)

Everything a clip shows is made and approved before any motion. A clip asked to invent its own set or restyle a character comes out mixed: flat shapes around one detailed character.

1. **Script and shot list:** the lines, the seconds for each shot, what each shot shows.
2. **Look frame:** one still in the chosen look, a character standing in the set. It is approved before anything else.
3. **Asset kit,** each item approved and saved as an Element:
   - the set as an empty background plate in the clip's ratio, plus one edit of the same plate for each change of light;
   - every character in the look, in each pose the script needs;
   - the props.
4. **Key frames:** one still for each shot, made from the plate and the Elements. Approved.
5. **Voice,** approved (AUDIO.md).
6. **Motion:** each key frame opens its own short clip (First and last frames, Draft first).
7. **Assembly in an editor:** the clips, the voice, the music, the titles and captions. Text is set as editor or code text, never drawn by a model.

Motion Studio is for flat graphic pieces (titles, maps, charts). It does not keep a character's look (MODEL-NOTES.md, "Motion Studio").

## Which video model

Seen on a paid plan, 2026-11-22 (prices are credits for 5 s unless noted; "Unlimited" = free with the plan's Unlimited switch).

| Use | Model | Length, sizes | References | Credits |
|---|---|---|---|---|
| Testing the idea, timing and camera | **Seedance 2.5 Draft** | 4-30 s, 480P | up to 50 | 0 with Unlimited (85 list) |
| Many quick clips | **Seedance 2.5 Flash** | 4-30 s, 480P, 720P | up to 20 (CLI: 10 images, 5 clips, 5 audio) | 0 with Unlimited (55-120 list) |
| The keeper | **Seedance 2.5** | 4-30 s, 480P, 720P, 1080P, 4K | up to 50 (CLI: 30 images, 10 clips, 10 audio) | 480P, 720P 0 with Unlimited; 1080P 455 |
| A short clip at 1080P-4K | **Seedance 2.0 / 2.0 Fast** | 4-15 s, 720P-4K | up to 12 (9 images, 3 clips, 3 audio) | 2.0: 1080P 205, 4K 490; Fast: 1080P 70, 4K 110 |
| Cheap 720P | **Seedance 2.0 Mini** | 4-15 s; 720P (screen also lists 1080P-4K) | up to 12 | 1080P 55, 4K 95 |
| A moving copy of a reference clip (motion transfer, object swap) | **Dreamina Recreate / Recreate Lite** | up to 30 s / 15 s, 720P | the clip | 29 / 17 |
| Fixed 8 s clip with native sound, 16:9 or 9:16 only | **Veo 3.1 / Fast / Lite** | 8 s | up to 3 images | 800 / 200-240 / 104-160 |

- Test on Draft first. When the draft is right, run the keeper with nothing changed but the model, so the test tells the truth about the keeper.
- The prompt limit is 15,000 characters on Seedance 2.5 and 4,000 on 2.0: room for the director's block below.
- Many other models are listed (Wan 3.0, Grok Imagine, FLUX 3 Video, Vidu Q4, LTX 2.5, PixVerse, Luma Ray 3.2, HappyHorse, Gemini Omni). Most cost far more than Seedance on this plan; use one only for a reason it names (Vidu Q4: image and audio references; FLUX 3 Video: keyframes up to 20 s).

## Modes

| Mode (seen 2026-11-22) | Use it for | Note |
|---|---|---|
| Omni reference (the default) | Several references, each with a role: a character, a place, a camera move to copy, music | Up to 50 on Seedance 2.5 |
| First and last frames | Still first, then motion: the approved still opens the clip; a second still can end it | The first frame sets the ratio; two frames must share one ratio |
| Multiframes | Several approved stills as key moments, in order: "Upload frames to generate a continuous video" | **Switches the model to Seedance 1.0 Fast**; the length is the sum of the segments |
| Smart edit | One change in a clip that is nearly right: "replace Character A with Character B"; "Edit with marks" for a region | **Switches to Seedance 2.5 Flash** |
| Long video | A clip longer than a normal generation | Seedance 2.5, 30 s by default |
| Video recreator | Motion transfer or an object swap from a reference clip | **Switches to Recreate Lite** |

Switching the mode can switch the model: name both in SETTINGS, and tell the user to check the model after choosing the mode. An Element always goes in through Omni reference, never into a frame slot.

## The eight parts, in this order

| # | Part | What goes in it |
|---|---|---|
| 1 | Format | Duration, ratio, shot structure: "10 seconds, 9:16, single take" |
| 2 | Subject | Who or what, bound to its picture: "the fox scout from the first frame", or its Element: "@FoxScout" |
| 3 | Action | Visible movement with a start and a finish |
| 4 | Environment | Place, time, weather (skip what the first frame already shows) |
| 5 | Camera | Shot size, one move, focus |
| 6 | Look | The Style Card (text-only prompts), or "keep the drawing style of the first frame" |
| 7 | Timing | Timecoded shots or beats and the transitions between them |
| 8 | Sound and keep-lines | Ambience, effects tied to actions, music; "Keep ..." lines; spoken words in quotes |

Write what the viewer can see, not feelings. The shortest prompt that fully specifies the shot wins.

## Templates

From a first frame:
```
<Duration>, <ratio>, <single take | N shots>. @Image 1 is the first frame.
<Subject from the frame> <action, start -> finish>. <Secondary motion: dust, petals, cloth, leaves.>
Camera: <shot size> + <one move>.
Timing: 0-3s: <beat>. 3-7s: <beat>. 7-10s: <end state, held>.
Sound: <ambience>, <effect on an action>, <music or "no music">.
Keep: the drawing style, palette and line of the first frame; <character traits>; <no cuts, if single take>.
```

Text only: the same, with "Use <reference> as <character>" plus the Character Card (or the character's @Element) after the format line, and "Look: <Style Card>" after the camera line.

### The director's block (several references, shots, dialogue or a beat-synced cut)

Dreamina's own "Try it" video prompts (2026-11-22) are written as one block of labelled sections. Use this form for anything with more than one shot, a speaking character, or music the cuts must follow:

```
<One line: what it is, length, ratio, look and energy>.

ACTIVE REFERENCES
@Image 1: <the character>. 100% matches the reference.
@Image 2: <the prop or place>. 100% matches the reference.

KEEP: <what must not change: the exact stack of parts, the count, the outfit; what must not be added>.

SHOTS
0.0-3.0s - <shot size>: <action, start -> finish>. <camera move>.
3.0s HARD CUT. 3.0-5.0s - <shot size>: <action>. <Character> says: "<the line>".
5.0-7.0s - <shot size>: <end state, held>.
Cuts only at the specified points.

AUDIO: <music: genre, tempo in BPM, the beat the cuts land on ("one beat every 0.4 s from 0.0 s"), what syncs to it>; <effects tied to actions>; <voice: who speaks, "(playful, unhurried)" delivery notes>, or "No vocals, no voice-over".
LIGHTING: <source, direction, colour temperature>.
OUTPUT: <ratio>, <length> seconds.

POSITIVE LOCKS: @Image 1 looks the same in every shot. <Lip sync matches the spoken lines.> <The final frame shows ...>.
Avoid: <concrete defects: extra people or hands, changed outfit, deformed parts, text, logos, watermarks>.
```

- "100% matches the reference" after each reference, and POSITIVE LOCKS at the end, are how Dreamina's own prompts hold identity across shots.
- Shot sizes as letters are fine (WS, MS, MCU, CU, ECU). Lens or field-of-view numbers ("MS, 47 deg FOV") belong only to a photographic or live-action look, never to an inked or painted one (STYLE-BRIDGE.md).
- A beat grid makes edits land on the music: state the tempo, the start and the spacing, and name what lands on a beat.

## One job per shot

One subject action, one camera move, one place. Two events or two places are two shots. For Seedance 2.0 Mini and other short generations: concrete subject + one visible action + framing with at most one move + one proof detail (dust at each step, a drop of water falling).

## Camera

- Sizes: extreme wide, wide, medium, medium close-up, close-up, extreme close-up.
- Moves: static, push-in, pull-out, slide left/right, follow, orbit, rise, whip pan, focus shift.
- Camera line before the look line; one move per shot.
- For inked and painted looks use the drawn-animation words of STYLE-BRIDGE.md (slide across layered flat planes, held poses), not lens words.
- A small character in a big world feels big from a low viewpoint: "at knee height, looking up at the windmill".

## Timing

- Seedance 2.5's own examples write timecoded shots: "0-4s: ... 4-10s: ...". Use that form for every clip of two or more beats.
- Under 8 s: one or two beats. 9-12 s: two or three beats. 13-15 s: three or four beats. 16-30 s (Seedance 2.5 only): five to eight beats, each with its own time range.
- Vertical social clips: something moves or changes in the first 2 s.
- Trailer beats: wide opener -> medium development -> moving shot for escalation -> close payoff.
- Name transitions: match cut, whip pan, cut to black on a sound. Plant a detail early and return to it at the end.
- End card: a locked last 3-4 s, gentle push-in, clean space for the logo (added in an editor).

## References

- Type @ in the prompt box to tag an uploaded asset or a saved Element. Name each one the way Seedance 2.5's examples do (@Image 1, @Video 1, @Audio 1, or the Element's name) and give every tag its role in words: "@Image 1 is the first frame; @Video 1 lends its camera move; @Audio 1 is the music".
- Limits (2026-11-22): Seedance 2.5 and 2.5 Draft up to 50 references (30 images, 10 clips, 10 audio), 2.5 Flash up to 20, Seedance 2.0, 2.0 Fast and 2.0 Mini up to 12 (9 images, 3 clips, 3 audio), Veo 3.1 up to 3 images. Saved Elements count as references and are mentioned with @.
- A reference audio file can carry the music or a voice the clip follows: "@Audio 1 is the music; cut on its beats".
- A reference video can lend its camera move or rhythm: "copy the camera move of @Video 1". Use only the user's own footage or clips they may use.
- Per character: one primary picture or one Character Element, fixed traits named once and repeated at the beat where they matter.
- Few references that agree beat many. Uploads of realistic human faces may be blocked.

## Longer clips

One generation is up to 30 s on the Seedance 2.5 family and 15 s on Seedance 2.0 (seen 2026-11-22). For more:

1. Split the story into segments of one generation each. Write each segment's end state exactly; it is the next segment's opening.
2. Segment 1 is a normal generation.
3. Each next segment extends the previous clip, with the Extend video tool or the Long video mode: "Extend the clip by 10 seconds. <timed beats>". The duration picked is the added part only.
4. Above about a minute, make separate scenes and join them in an editor.

## When it comes out wrong (one layer at a time: references -> structure -> camera -> look, sound)

| Symptom | Change |
|---|---|
| Character or style drifts | Start from a first frame; one primary reference or the character's @Element; repeat fixed traits at the beat |
| Looks 3D or photographic | Remove lens words; "keep the flat drawn look of the first frame, drawn animation" |
| Random extra cuts | "single take, no cuts", or the exact shot count with time ranges |
| Camera ignores the move | Camera line earlier; one move only |
| Action rushed or mushy | Fewer actions; lengthen the beat; give the action a start and a finish |
| Limbs multiply or melt in motion | Smaller, slower movement; closer shot; fewer characters moving at once |
| Unwanted captions or logos | "no captions, no lettering" |
| Sound out of step | Tie each sound to a timecode or an action |
| One thing wrong in a clip that is otherwise right | Smart edit mode on that clip, not a new generation; Edit segment to retake only a stretch of it |
| Lips out of step with the line | The line in quotes inside its shot, its delivery in brackets, "Lip sync matches the spoken lines" in POSITIVE LOCKS; fewer words per shot |
| The look changed after picking a mode | The mode switched the model: set the model back (Multiframes, Smart edit and Video recreator each pick their own) |
| Right clip, wrong frame size or too soft | Reframe video (1:1, 3:4, 4:3, 16:9, 9:16, 21:9); Creative upscale (video to 4K) |

Never ask for opposites in one beat: static and handheld, one take and five cuts, soft daylight and hard neon.

## Where generated video may go

Social teasers, mood pieces and devlog clips. A Steam trailer should show the real game, and Steam screenshots must be real gameplay (FORMATS.md).

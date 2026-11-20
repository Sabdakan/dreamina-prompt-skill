# Video: Seedance

Built from Dreamina's Seedance 2.5 page and its examples, CapCut's Seedance 2.0 Mini formula and a community Seedance 2.0 skill written for the Chinese platform. Limits differ between them; see MODEL-NOTES.md and use what the user's Dreamina shows.

## Still first, then motion

The strongest way to keep a clip on the project's look:

1. Make the opening frame as a Seedream picture (IMAGE.md) with the Style and Character Cards. The user approves it.
2. Give that picture to Seedance as the first frame (First and last frames mode; add a last frame when the ending matters).
3. The video prompt then says only what moves, how the camera moves, the timing and the sound. It does not describe the look again: the frame carries it, and a second description invites drift.

Write a text-only video prompt (all eight parts, Style Card included) only when there is no frame to start from.

## Which video model

| Use | Model (seen 2026-11-20) |
|---|---|
| Testing an idea, the timing, the camera | **Seedance 2.5 Draft**: 480p drafts, fewer credits |
| The keeper | The full model, with the same prompt and uploads: **Seedance 2.5** ("up to 50 references" on its page) or **Seedance 2.0 Mini** (the default: up to 12 references, up to 15 s, 720P, 25 credits for 5 s) |
| Many quick clips | **Seedance 2.5 Flash** (faster, fewer credits) |

Test on Draft first. When the draft is right, run the keeper with nothing changed but the model, so the test tells the truth about the keeper.

## Modes

| Mode (seen 2026-11-20) | Use it for |
|---|---|
| Omni reference (the default) | Several references, each with a role: a character, a place, a camera move to copy, music |
| First and last frames | Still first, then motion: the approved still opens the clip; a second still can end it |
| Multiframes | Several approved stills as key moments in order (read from its name; check its tooltip on the screen) |
| Smart edit | One change in a clip that is nearly right |
| Long video | A clip longer than one generation (see "Longer clips") |
| Video recreate | Motion transfer or an object swap from a reference clip (the Recreate models) |

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
- Under 8 s: one or two beats. 9-12 s: two or three beats. 13-15 s: three or four beats.
- Vertical social clips: something moves or changes in the first 2 s.
- Trailer beats: wide opener -> medium development -> moving shot for escalation -> close payoff.
- Name transitions: match cut, whip pan, cut to black on a sound. Plant a detail early and return to it at the end.
- End card: a locked last 3-4 s, gentle push-in, clean space for the logo (added in an editor).

## References

- Type @ in the prompt box to tag an uploaded asset or a saved Element. Name each one the way Seedance 2.5's examples do (@Image 1, @Video 1, @Audio 1, or the Element's name) and give every tag its role in words: "@Image 1 is the first frame; @Video 1 lends its camera move; @Audio 1 is the music".
- Seedance 2.0 Mini takes up to 12 references (images, videos, audio) in Omni reference mode, or @ mentions of saved Elements (seen 2026-11-20). Plan for no more than 12 until the screen shows more.
- A reference video can lend its camera move or rhythm: "copy the camera move of @Video 1". Use only the user's own footage or clips they may use.
- Per character: one primary picture or one Character Element, fixed traits named once and repeated at the beat where they matter.
- Few references that agree beat many. Uploads of realistic human faces may be blocked.

## Longer clips

One generation is short (2.0 Mini: up to 15 s on the screen; up to 30 s claimed on the 2.5 page). For more:

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
| One thing wrong in a clip that is otherwise right | Smart edit mode on that clip, not a new generation |

Never ask for opposites in one beat: static and handheld, one take and five cuts, soft daylight and hard neon.

## Where generated video may go

Social teasers, mood pieces and devlog clips. A Steam trailer should show the real game, and Steam screenshots must be real gameplay (FORMATS.md).

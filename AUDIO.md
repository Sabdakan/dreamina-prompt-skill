# Audio: voices, sound scenes and music

Built from a paid account's AI Audio and AI Music screens, Dreamina's own audio "Try it" examples and the CLI's live model and voice lists (all 2026-11-22). See MODEL-NOTES.md; run `scripts/catalog.py audio voices` for the current list.

## Pick the tool

| The user needs | Mode | Model (screen description) |
|---|---|---|
| Character lines with emotion, several speakers in one script | AI Audio, **Voiceover** | **ElevenLabs v4** ("supports multi-speaker dialogue with more nuance and smoother flow") or **v3** ("rich emotional range for character dialogue and story narration") |
| Narration for a trailer, a devlog, a story | AI Audio, Voiceover | ElevenLabs v4 or v3, a voice tagged for narration |
| Quick, cheap voice-over (ads, social) | AI Audio, Voiceover | **MiniMax Speech 2.8 Turbo** ("fast, cost-effective for voiceovers"); **HD** for cleaner voices |
| Plain reading of a text | AI Audio, Voiceover | **Seed TTS** (no tags, short texts) |
| A whole sound scene: voices, effects, ambience and music placed by time | AI Audio, **Omni audio** | **SeedAudio 1.0** ("create rich audio with voices, sound effects, ambience, and music") |
| Music: a song, a theme, a bed under a voice | **AI Music** | **MiniMax Music 3.0** ("natural sound with strong arrangement capabilities") |
| Sound that must match a clip's picture | The clip's own AUDIO section | Seedance or another model with native audio (VIDEO.md) |
| A finished clip in other languages | Video dubbing tool | Chinese, English, Japanese, Korean, Spanish (Mexico), German, French, Portuguese (Brazil), Thai, more |

Limits (CLI, 2026-11-22): text up to 10,000 characters on ElevenLabs v4 and MiniMax, 2,000 on ElevenLabs v3, 3,000 on SeedAudio, 600 on Seed TTS. Speech is priced by text length (Dreamina's own short scripts on ElevenLabs v4: 8 to 14 credits); a music track showed 35 credits.

## Voices

- Pick from the **Voice library**: filters Gender, Age (Child, Teen, Young adult, Adult, Senior), Language, Use case (Dialogue, Expressive, Ads & promo, Character voices). ElevenLabs has the largest library (about 105 English voices, 2026-11-22); MiniMax and SeedAudio share 13 character voices; Seed TTS has 24. Name the voice exactly as the library spells it.
- **One voice per character for the whole project.** Add a `Voice:` line to the Character Card (STYLE-BRIDGE.md) with the model and the exact voice name, and reuse it.
- One voice can speak several languages in one script: Dreamina's own multilingual example switches English, French and Korean in the same voice.
- **Create voice** (in the library) designs or clones a voice. Clone only the user's own voice or one with the speaker's written consent; never a real person's or a famous voice.

## Writing a voice script

ElevenLabs v3 and v4 (square brackets; "Add speaker" for several voices):
```
<Speaker name>
[<delivery>] <line>
[<delivery>] <line>

<Second speaker name>
[<delivery>] <line>
```
- A tag in square brackets shapes the words after it. Free phrases work and can be stacked, as in Dreamina's own example: `[shaky breathing, terrified whisper]`, `[elderly voice] [firm, full voice]`.
- Its tag list (2026-11-22): emotion `[angry] [bored] [curious] [excited] [menacing] [playful] [tired] [weak] [crying]`; sounds `[clears throat] [coughing] [chuckling] [laughing] [sighing] [gasping] [panting] [humming] [sharp exhale] [scoffing] [sniffling] [yawning]`; delivery `[whispering] [softly] [slowly] [pause] [voice breaking] [singing]`; character `[sleepy drowsy voice] [witch voice] [drunken voice]`; effects `[knocking on door] [bell ringing] [phone ringing] [dog barking] [crowd cheering] [applause] [rain falling] [drum roll] [heartbeat] [engine starting] [keyboard typing] [echoing]`.
- Pace with `[pause]`, `[long pause]`, `[short pause]` and punctuation; shouting with `[shouting]` and a few capitals, sparingly.
- Narration reads best with a tag per sentence that names tone and pace: `[low and unhurried]`, `[grave and measured]`, `[with rising weight]`, `[softly, with warmth]`.

MiniMax Speech 2.8 (round brackets, vocal sounds only): `(laughs) (chuckle) (sighs) (breath) (inhale) (exhale) (gasps) (sniffs) (coughs) (clear-throat) (groans) (pant) (humming) (emm)`. Emotion comes from the words and punctuation; a square-bracket tag would be read aloud.

Seed TTS: plain text; commas, full stops and line breaks carry the pace.

For every model:
- Write how a line is said, not what it means.
- Spell names and numbers as they are spoken ("twenty-four", "Moss-well").
- Social voice-over: about 2.5 words a second; the first line lands in the first 2 seconds.
- Game lines (barks): short, 3 to 6 variants per action, the same voice and tags, one file each.

## A timed sound scene (SeedAudio 1.0, Omni audio)

The screen says: "Enter your dialogue and describe the voice you want. Upload an audio reference or use @ to mention a saved voice. Add timestamps to set when speech, sound effects, or background music should play." References: up to 3 audio files, or 1 image, not both (CLI).

```
0-2s: ambience: <place and its sounds>.
2-6s: <voice description or @SavedVoice>: "<line>" (<delivery>). Effect at 4.5s: <sound>.
6-10s: music: <genre>, <tempo> BPM, <two instruments>, low under the voice; fades out by 10s.
```
How strictly it keeps the timestamps is not yet tested: log the first results (FEEDBACK.md).

## Music (AI Music, MiniMax Music 3.0)

Controls (2026-11-22): **Music description**, **Lyrics** (optional, with section tags), **Style** chips, **Choose vocal type** (Auto, Male, Female), an **Instrumental music** switch. No length control on the screen; the CLI's music mode takes a duration (30 s by default).

- **Description:** use, genre, mood, tempo in BPM, two or three instruments, vocal style, the energy over time. Dreamina's own example is one line: "Dreamy rock with a romantic, hazy feel and electric guitar".
- **Style chips** are the words the model knows; build the description from them. Genre: Pop Rock, Dance Pop, Indie Folk, Post-Rock, Jazz Hip-Hop, Neo-Soul, Bossa Nova, Synthwave, Electronica, Neoclassical. Mood: Romance, Mellow Buzz, Bittersweet, Soft Melancholy, Aloof, Unease, Trippy Haze, Peaceful Relief, Resolute, Quirky. Instrument: Felt Piano, Rhodes, Nylon Guitar, Slide Guitar, Fretless Bass, Muted Trumpet, Handpan, Vibraphone, Pizzicato Strings, Analog Synth. Vocal: Breathy, Laid-Back, Smoky, Cool, Warm, Airy Falsetto, Soulful Runs, Stacked Harmonies, Vocoder, Reverb-Soaked. Texture: Granular Delay, Tape Saturation, Lo-Fi Grain, Vintage Distortion, Wide Stereo, Long Reverb, Vinyl Crackle, Deep Bass, Airy Highs, Sparse.
- **Instrumental** for anything under a voice, game menus and loops.
- **Lyrics:** `[Verse]`, `[Chorus]`, `[Bridge]`, `[Outro]`; short lines with an even syllable count; the user's own words only.
- **Loops:** ask for "a steady loopable groove that ends where it began", then trim the loop in an editor; a seamless loop is not promised.
- **A trailer:** make the music first; its tempo sets the clip's beat grid (VIDEO.md, "The director's block").
- No names of artists, bands or songs: describe their qualities (the standing rule).

## Output format

```
## <what it is> - <project> - Voice | Sound scene | Music
SETTINGS  Mode: <Voiceover | Omni audio | AI Music> · Model: <...> · Voice: <exact library name, per speaker> (music: Vocal type <Auto/Male/Female>, Instrumental <on/off>, Style: <chips>)
UPLOAD    <reference audio or picture -> its role>, or "nothing"

SCRIPT    (or PROMPT for music)
<one code block to copy whole>

LYRICS    (music with vocals only)
<one code block>

IF IT COMES OUT WRONG
- <likely problem> -> <the one change>
```

## When it comes out wrong

| Symptom | Change |
|---|---|
| Flat, robotic delivery | A delivery tag on every line; shorter sentences; ElevenLabs v3 for a wider emotional range |
| Wrong emotion | Put the tag right before the words; one emotion per line |
| A tag is read aloud | The model's brackets: ElevenLabs `[ ]`; MiniMax `( )` and only its sound list; Seed TTS none |
| A name is mispronounced | Spell it as spoken, with hyphens |
| Rushed | `[pause]` or `[slowly]`; split the line; fewer words |
| The voice changes between lines | One voice name per speaker, the same model for the whole script |
| Music too busy under a voice | Instrumental on; "sparse", fewer instruments; "sits under a voice" |
| Wrong genre or feel | Pick Style chips instead of free words |

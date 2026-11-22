# dreamina-prompt

A Claude skill that writes prompts and settings for Dreamina (by CapCut): pictures (Seedream, GPT Image, Nano Banana and more), videos (Seedance, with a director's block for shots, dialogue and beat-synced cuts), voice-overs and character dialogue (ElevenLabs, MiniMax, SeedAudio) and music (MiniMax Music). It keeps one style and one voice per character across a whole project, picks the cheapest model and tool for each job, and reads results to fix the next try. With Dreamina's own CLI installed it reads the live model catalog, places prompts on your Dreamina canvas, or runs them after you approve the credits.

It writes prompts and settings only; you run them in the tool yourself.

## Install in Claude Code

macOS or Linux:

```
git clone https://github.com/Sabdakan/dreamina-prompt-skill.git ~/.claude/skills/dreamina-prompt
```

Windows (PowerShell):

```
git clone https://github.com/Sabdakan/dreamina-prompt-skill.git "$env:USERPROFILE\.claude\skills\dreamina-prompt"
```

**Update** to the newest version at any time:

```
git -C ~/.claude/skills/dreamina-prompt pull
```

(on Windows: `git -C "$env:USERPROFILE\.claude\skills\dreamina-prompt" pull`)

## Install in the Claude app

Download [dreamina-prompt.zip](https://github.com/Sabdakan/dreamina-prompt-skill/releases/latest/download/dreamina-prompt.zip) and add it in the app's Skills settings. The link always gives the newest version: download it again and replace the skill to update.

## Your own project's rules

Write them in a file named `PROJECT-NOTES.md` beside `SKILL.md`: your style, your characters, sizes, who makes what. The skill reads it first, and its rules win over the skill's defaults. Git ignores the file, so updates never touch it.

## Start here

Read [MANUAL.md](MANUAL.md): how to talk to the skill and what each answer contains.

Works well with [tripo-prompt](https://github.com/Sabdakan/tripo-prompt-skill).

# dreamina-prompt

A Claude skill that writes prompts for Dreamina (by CapCut): pictures with the Seedream models and videos with the Seedance models. It keeps one style across a whole series, makes character sets one picture per pose, plans social posts, store art and clips, and reads results to fix the next try.

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

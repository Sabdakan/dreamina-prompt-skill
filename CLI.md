# Dreamina's CLI: reading the catalog, placing prompts, running them

Dreamina has its own command-line tool, `dreamina-canvas` (Dreamina's "Plugins & CLI" page; the screen marks it "Private beta · Advanced subscribers only", 2026-11-22). Signed in to the user's account, it can do three things for this skill. Each needs a different level of the user's permission.

| What | Spends credits | Changes the account | Needs |
|---|---|---|---|
| **Read the catalog**: models, their limits, voices | no | no | the CLI installed and signed in |
| **Way 1: place a prompt** as a card on the user's Dreamina canvas; the user presses Generate | no | adds a canvas and cards | the user asked for this way |
| **Way 2: run it**, then show and save the results | **yes** | adds cards and results | the user's yes to the price, every run |

## Setup (once, by the user)

1. Install from Dreamina's "Plugins & CLI" page. Read the installer before running it: it downloads the CLI program and Dreamina's own agent skill, and adds the program's folder to the user's PATH.
2. Sign in: `dreamina-canvas auth login` gives a link and a code. The user opens it, signs in to their own Dreamina account and confirms; then `dreamina-canvas auth wait --device-code <code> --timeout 5m`. The sign-in grants the CLI access to that account and its credits.
3. Check: `dreamina-canvas auth status` shows `"loggedIn": true`.

The CLI ships its own skill, written for agents that generate by default and start sign-in on their own. Where it and this skill differ, this skill's approval rule below wins.

## Read the catalog (any time, read-only)

```
python "<skill folder>/scripts/catalog.py"              all models and voices
python "<skill folder>/scripts/catalog.py" video        one type: image, video, audio, voices
```
The script runs only `auth status`, `model list` and `voice list`, and prints each model's modes, ratios, resolutions, lengths, prompt limit and reference limits. Use it before SETTINGS when a limit matters, and to refresh MODEL-NOTES.md. Model names for commands are the canonical ones it prints in brackets (`seedream_5.5`, `seedance_2.5`), never the display names.

## Way 1: place the prompt on the canvas

```
dreamina-canvas canvas create "<canvas name>" --use
dreamina-canvas resource upload --file "<path to an approved reference picture>"
dreamina-canvas node create image --mode i2i --model seedream_5.5 --ratio 1:1 --resolution 2K --count 4 \
  --ref res:<resource id> --prompt "<the prompt; {{res:<resource id>}} where the reference is named>" \
  --title "<short title>"
```
- Without `--run` the card is only saved: it costs nothing. Send the user the canvas link (`dreamina-canvas canvas current` returns `webUrl`); they check the card and press Generate in Dreamina.
- Video: `node create video --mode t2v | first_last_frame | m2v --model <...> --ratio <...> --resolution <...> --duration <seconds>`. An Element or several mixed references use `m2v`; one image as the first frame uses `first_last_frame`.
- Voice: `node create audio --mode tts --model <...> --voice-name "<exact name>" --prompt "<script>"`. Music: `node create audio --mode music --model <...> --duration <seconds> --prompt "<description>"`.
- One card per picture or clip the user asked for, so each can be compared and edited on its own.
- A reference sits in the prompt where it is meant: `{{res:<id>}}` or `{{node:<id>}}`. Typing "@name" in a command does not link anything.
- Check flags with `dreamina-canvas <command> --help` and `--dry-run`; the installed version is the truth.

## Way 2: run it (credits)

When the user has chosen Way 2 as their default (PROJECT-NOTES.md says so), the skill goes straight from the prompt to the quote, with no Way 1 card step for them to press. The price approval below still happens for every run, or once for a batch whose items and total ceiling are listed before it runs.

1. Save the card as in Way 1, then get its price: `dreamina-canvas node quote` (see its `--help`). The quote is the list price even on an Unlimited model (the CLI cannot switch Unlimited on); a free run is pressed on Dreamina's own screen (see "Unlimited, the watermark and Elements" below).
2. **Ask the user**, every time: what will run, the price, and the most credits it may use. Wait for a clear yes. For a batch (a series, several variants), list every item with its price and the total, and ask once for the whole batch; a run that is not on the approved list needs its own yes. A free Unlimited run still gets a one-line notice before it is pressed.
3. Run with that ceiling: `... --run --credit-ceiling <approved amount> --wait`. The CLI stops if the price is higher. Never run without `--credit-ceiling`: small runs may need no confirmation from Dreamina's server, so the ceiling is the only guard. Never use `--yes` for a run.
4. Look at the result before calling it done. Download images with `dreamina-canvas resource download <resource id>` into the project's folder; videos and audio are opened on the canvas.
5. A result that missed: change one thing (FEEDBACK.md), and ask again before the next run.

### Unlimited, the watermark and Elements (seen 2026-11-22, CLI 1.4.0)

- **Unlimited is not in the CLI.** `node quote` and `--credit-ceiling` see the list price even on an Unlimited model, and no flag sets the Unlimited switch. A free run is started on Dreamina's own screen: on the canvas card, switch Unlimited on, read the price as 0, press Generate. The CLI still saves the cards, waits (`node show`) and downloads.
- **Unlimited is one task at a time per account, in a slower lane** (the switch's own line: "Turn off to use credits for faster generation"; at peak times a run can wait an hour). While one task waits, the other cards show the list price and no switch: do not press them. Never start a run while the user's own runs wait.
- **Cancel a waiting run from its own card** ("Cancel generation"). After the card is deleted the run keeps going on the server, and neither the CLI (it has no cancel for image runs) nor the History panel can stop it.
- **The visible "AI" mark is added at export.** After the user switches on "Remove watermarks" (account menu), download again any picture downloaded before: it comes clean, the same pixels otherwise.
- **Element cards** made with `node create element` (a main picture, extra pictures, a description) stay on that canvas; they do not appear in Assets & Elements. They work as a reference: `--ref node:<element node id>` with `{{node:<id>}}` in the prompt. An account Element needs the user's file upload in Assets & Elements.
- **A connected card** (`--ref node:<id>`) uses the shown picture of that card. A model may return the reference nearly unchanged when asked for a new view of the same object (MODEL-NOTES.md).

## Rules

- Nothing is deleted (cards, canvases, resources) without the user's word.
- Upload only pictures and audio the user owns or may use.
- A run whose outcome is unknown (timeout, lost connection) is checked with `dreamina-canvas operation status`, never submitted again with a new identity: that could pay twice.
- Keep the CLI's sign-in out of project files and logs; never print or store tokens.

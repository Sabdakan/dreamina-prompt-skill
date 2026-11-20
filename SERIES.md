# Series: many pictures that must match

For four or more pictures of one kind: upgrade cards, item icons, character portraits, a run of social posts. PROJECT-NOTES.md may name a project's own list of pictures and its file names.

## Method

1. **Anchor.** Write full prompts (IMAGE.md) for two or three typical items. The user generates until one is right. That picture is the anchor: it defines line, palette, background and scale better than any text. Ask the user to save it as a **Style Element** (a name of up to 20 characters) and record the name in `docs/dreamina/cards.md`.
2. **Frame.** Split the anchor's prompt in two:
   - the **frame**: format and purpose, composition, light, Style Card. Fixed for the whole series.
   - the **slot**: one subject line per item. The only thing that changes.
3. **Sheet.** Put the frame in a text file with `{subject}` where the slot goes, and the items in a CSV with columns `id,name,subject`. Then:
   ```
   python "<skill folder>/scripts/expand_series.py" frame.txt items.csv "<project folder>/docs/dreamina/series-<name>.md"
   ```
   The sheet has one ready-to-copy prompt per item with a status box. Keep frame.txt and items.csv next to it.
4. **Generate with the anchor attached, or its Style Element mentioned with @.** The frame says so: "Match the drawing style, line weight, palette and background of @<StyleElement>. New subject: {subject}" (or "of the reference picture", with the anchor uploaded for every item). Keep one model for the whole series (IMAGE.md, "Which image model").
5. **Review in batches of 8-10**, side by side at the in-game or in-feed size. A flaw across the batch is fixed once in the frame, never item by item. One flaw in one picture is Smart edit (FEEDBACK.md, "The cheapest fix first"). Log the change in `prompt-log.md`.

## Writing subject lines

Most card names are ideas ("Lucky harvest", "Good neighbours"), and a model cannot draw an idea.

- Turn each into **one object or one small action** a player would recognise: Lucky harvest -> "a wicker basket of golden wheat with a red ribbon on the handle".
- One subject per picture, the same viewpoint and scale as the anchor, filling the same share of the frame.
- Tell siblings apart by **shape first**, colour second: a 128 px card is read by its silhouette.
- Related items share a base and differ by one feature (level 1 to 3 of a windmill: taller, never wider), so the set reads as a family.
- No lettering in the picture; names are drawn by the game or the layout.
- State counts positively when a creature appears (four legs, one tail).

## Frame example (shape to copy)

```
Square upgrade-card picture for a strategy game, shown at 128 px, must read in silhouette.
Match the drawing style, line weight, palette and background of @<StyleElement>.
New subject: {subject}.
Composition: centred, the subject fills about 70% of the frame, flat single-tone background, no ground line.
Light: one soft light from the upper left. Mood: clear and sturdy.
Style: <Style Card>.
```

## Keeping the series honest

- Do not reword the frame between sessions; read it back from frame.txt.
- When the Style Card or the Style Element changes version, note which items were made under the old one in the sheet.
- Follow any series rule in PROJECT-NOTES.md (for example, a project where every generated draft is logged, or repainted before it ships).

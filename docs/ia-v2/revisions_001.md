# revisions_001.md — Home Screen Iteration 1

## Overall

Excellent first pass. Layout, design system adherence, anti-pattern avoidance, and bottom navigation are all production-quality. One critical issue blocks acceptance.

## REQUIRED FIX (Priority 1)

### Pomu Avatar is Broken

**Problem**: The current implementation uses the full character sheet (`references/pomu_character_sheet.png`) as a CSS background-image, scaled to 206×154 within a 48×48 avatar. This shrinks all 7 Pomu expressions into the avatar space and only renders a corner sliver — visually only the tip of a pineapple is visible. Pomu's body, face, and personality are completely lost.

**Fix**: 

1. Use a Python script to **extract just the first Pomu expression** (the top-left one — front-facing with both eyes open and a small smile) from `references/pomu_character_sheet.png` and save it as `references/pomu_avatar.png`.
   - The character sheet has 4 Pomus on the top row and 3 on the bottom row.
   - Crop a clean square containing the top-left Pomu (estimate ~340×340 region from the sheet, then resize to 256×256 for the avatar source).
   - Preserve transparency if possible (the original is on white background, so for now keeping white is acceptable; later we'll cut to transparent PNG).

2. Update the `.pomu-avatar::before` rule in `home.html`:

```css
.pomu-avatar::before {
  content: "";
  position: absolute;
  inset: 1px;
  border-radius: inherit;
  background-image: url("references/pomu_avatar.png");
  background-size: cover;
  background-position: center 30%;  /* slightly above center to feature the face */
  background-repeat: no-repeat;
}
```

3. Verify in browser at 393×852 viewport: Pomu's face (eyes, beak, pineapple) should be the primary subject of the avatar circle. The teal border should frame the face nicely.

## REFINEMENT (Priority 2, optional)

### Decorative Signs Could Be Slightly More Present

The CHAIPO / POKER BRAIN / LEVEL UP signs in the corners are barely visible at z-index -1 with rgba(26,32,44,0.32) text color. They're meant to be atmospheric, not invisible.

**Suggested**: Increase the text color opacity from `0.32` to `0.48`, and the border from `0.24` to `0.36`. Keep the dashed inner border subtle. Do NOT make them compete with the foreground cards — just slightly more visible as world texture.

If this is too risky, leave as-is and we'll revisit later.

## DO NOT CHANGE

Everything else is working well. Specifically:

- Bottom navigation: locked in
- Hero CTA design: locked in  
- Mission card structure: locked in
- Daily bonus card: locked in
- Background world layers (clouds, buildings, paint splatters, street perspective): locked in
- Design tokens: do not modify
- Mode card emoji icons (😄👥🤖): acceptable for prototype, no need to change yet
- Overall layout and spacing: locked in

## Validation

After fixes:

1. Open `home.html` in a 393×852 browser viewport.
2. Confirm Pomu's face is clearly visible in the header avatar.
3. Take a new screenshot and save as `home_393x852_v2.png`.
4. Report "完成 v2" when done.

## Notes for Next Round

If v2 looks good, we will proceed to:
- Round 2: 対戦タブ (battle hub) using the same design system
- Round 3: Settings + Stats light-tone remake
- Round 4: Asset polish (proper SVG icons replacing emojis)

# CODEX_PROMPT.md — Paste this into ChatGPT Codex

Below is the exact prompt to copy-paste into ChatGPT (Codex mode) to start the first round of UI generation.

---

## How to Use

1. Open ChatGPT (Pro account).
2. Switch to **Codex** mode (the coding agent surface).
3. In the same conversation, upload these 3 files as attachments:
   - `AGENTS.md`
   - `DESIGN_TOKENS.md`
   - `HOME_SCREEN_SPEC.md`
4. Also attach these 10 images:
   - IMG_2200.PNG — title screen (preserve aesthetic)
   - IMG_2201.PNG — current mode select (REPLACE this with new home)
   - IMG_2202.PNG — AI battle select (tone reference)
   - IMG_2203.PNG — FL practice (tone reference)
   - IMG_2204.PNG — friend match (tone reference)
   - IMG_2205.PNG — online match (tone reference)
   - IMG_2206.PNG — stats screen (TO BE REMADE in light tone later)
   - IMG_2207.PNG — shop screen (tone reference)
   - IMG_2208.PNG — settings screen (TO BE REMADE in light tone later)
   - Pomu character sheet (the 7-expression image)
5. Paste the prompt below.

---

## Prompt to Paste

```
I'm redesigning the home screen of an iOS mobile poker app called Chaipo Neighbors (チャイポネイバーズ). I need you to generate a single standalone home.html file based on the attached specifications.

**Critical context first — please read these three documents fully before starting:**

1. AGENTS.md — project rules, visual direction, anti-patterns
2. DESIGN_TOKENS.md — the complete design system (colors, typography, spacing, components)
3. HOME_SCREEN_SPEC.md — the exact layout and component specs for this screen

**Visual references (the 10 attached images):**

- IMG_2200 shows the existing title screen — match this tone (light, blue sky, Shibuya grunge aesthetic).
- IMG_2201 shows the CURRENT home/mode-select screen — this is what we're replacing. The new design must be cleaner and use the bottom tab pattern.
- IMG_2202 through IMG_2205 are existing sub-screens — these establish the visual world (Shibuya backgrounds, signage style, Pomu mascot).
- IMG_2206 and IMG_2208 are DARK screens that we will remake light-toned later — note their tonal mismatch as something to avoid.
- IMG_2207 is the shop screen — note the cream tone.
- The character sheet shows Pomu — the white fluffy bird with pineapple mascot. This is the only character used in the app.

**Your task:**

1. Read all three .md files carefully. Internalize the design tokens before writing any code.
2. Generate a single home.html file that implements the home screen exactly as specified in HOME_SCREEN_SPEC.md.
3. Use vanilla HTML/CSS/JS — no frameworks, no external dependencies.
4. Inline all CSS and JS within the HTML file.
5. The output should render correctly at 393×852 viewport (iPhone Pro mobile).
6. Include comments in the HTML so a human reviewer can navigate the sections.

**Important rules:**

- Stay strictly within the design tokens defined in DESIGN_TOKENS.md.
- Do NOT use purple gradients, generic shadcn cards, lorem ipsum, or material design icons.
- All Japanese text must match the spec exactly.
- The bottom navigation must be fixed at the bottom and visible from all screens (this is the most important pattern in the entire app — we will reuse it everywhere).
- Pomu must be visible somewhere on the screen (avatar in header).
- Use inline SVG for icons. Lucide icons are a good reference. Stroke width 1.75px.

**Before you write code, briefly tell me:**

1. Your one-sentence "visual thesis" for this screen (mood, energy, what it should evoke).
2. The three biggest design decisions you're going to make.
3. Any spec ambiguity you noticed and how you'll resolve it.

Then write the code.

After delivering the code, open the file in a Playwright browser at 393×852 viewport, take a screenshot, and show me the result. If anything looks off compared to the tone references, iterate before showing me.
```

---

## What to Expect

Codex will likely:
1. Reply with the visual thesis and design decisions (per the prompt request).
2. Generate `home.html` as code in the chat.
3. If you have the Playwright skill enabled, it will render and screenshot.
4. You can then ask for revisions ("make the sky more vivid", "the Pomu avatar feels too small", etc.).

## What to Send Back to Me

Once you're satisfied (or stuck), send me:
- The generated `home.html` (paste contents or upload file)
- The screenshot Codex produced
- Any notes on what felt off

I'll then:
1. Review the design against our spec.
2. Suggest revisions if needed.
3. Plan the integration into `index_backup.html` via Python patch.
4. Move to the next screen (likely the 対戦 tab or the settings light-tone remake).

## Tips for the Codex Session

- **Be specific in revisions.** "Make it more premium" is too vague. "Increase the Pomu avatar from 48px to 64px and add a subtle teal glow" is actionable.
- **Don't over-iterate in one session.** If after 3-4 rounds it's still off, send what you have to me and we'll regroup.
- **Save intermediate versions.** Use `Save as` in your browser to keep working snapshots.
- **If Codex insists on a different design choice**, ask it to justify against the design tokens. The tokens are non-negotiable.

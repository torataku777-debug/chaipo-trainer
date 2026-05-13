# AGENTS.md — Chaipo Neighbors Design Prototype

This file establishes ground rules for AI coding agents (Codex, Claude Code, etc.) working on the Chaipo Neighbors UI redesign.

## Project Overview

**Chaipo Neighbors** (チャイポネイバーズ) is an iOS mobile app for **Joker Ultimate Pineapple Open Face Chinese Poker** — a card game with AI matches, Fantasy Land (FL) practice, friend matches, and online play.

This prototype is **isolated standalone HTML/CSS/JS for design exploration only**. It is NOT integrated with the main app. The main app is a single large HTML file (`index_backup.html`, ~755KB) that uses Capacitor for iOS packaging — but Codex should treat that as out of scope. Generate clean, well-organized standalone files. The human PM will manually integrate accepted designs into the monolith later.

## Visual Direction

The app's brand is set: **Shibuya street + grunge + signage aesthetic** with a **blue sky background** and a **mascot character named Pomu (ぽむ)** — a round white fluffy bird with a pineapple on its head.

Existing screens use a mix of light and dark trees that creates visual fragmentation. The new design must:

1. **Stay 100% in light tone** — no dark backgrounds, no black surfaces.
2. **Background = world** (Shibuya street, blue sky, decorative signage) — these are atmospheric, not interactive.
3. **UI components = clean frosted-glass cards** floating above the world — these are interactive.
4. **Pomu is the only character** — no human characters, no other mascots.
5. **Tone reference**: think "Pokemon TCG Pocket meets street art" — playful but premium, never cartoonish or cluttered.

## Working Rules

- **No invented features.** Build exactly what the spec describes. If anything is ambiguous, choose the simplest interpretation and add a one-line note.
- **No new dependencies unless explicitly requested.** Use vanilla HTML/CSS/JS or React + Tailwind only.
- **Mobile-first**, target iPhone 15/16 Pro viewport (393×852pt, ~430×932px in pixels with 3x scaling).
- **Test in browser at 393×852.** Use Chrome DevTools mobile emulation.
- **Component naming**: kebab-case for HTML/CSS classes, PascalCase for React components.
- **All Japanese text must be preserved exactly as specified.**
- **Preserve all existing colors, typography, and texture tokens defined in DESIGN_TOKENS.md.**

## Anti-Patterns to Avoid

These are common AI-generated UI mistakes that will get the work rejected:

- ❌ Purple/violet gradients (default LLM choice — looks generic AI)
- ❌ Generic shadcn/ui card components without customization
- ❌ Overuse of `backdrop-blur` (only use on bottom nav and key cards)
- ❌ Centering everything (mobile UI needs strong asymmetry and hierarchy)
- ❌ Tiny touch targets (<44px height violates iOS HIG)
- ❌ Lorem ipsum or English placeholder text — use the actual Japanese copy from the spec
- ❌ Stock illustrations or icons that don't match the grunge aesthetic
- ❌ Making decorative signs (CHAIPO, POKER BRAIN, LEVEL UP) compete with functional buttons

## Done Definition

A screen is "done" when:

1. It renders correctly at 393×852 viewport.
2. All Japanese copy matches the spec exactly.
3. Bottom navigation is fixed and accessible from all screens.
4. Pomu's avatar is visible somewhere in the layout.
5. The screen integrates the Shibuya/blue-sky world without feeling like a generic app.
6. No console errors.

## Reference Materials Provided

- `HOME_SCREEN_SPEC.md` — what to build for this round
- `DESIGN_TOKENS.md` — colors, typography, spacing, components
- 9 screenshot references of the existing app (IMG_2200 — IMG_2208)
- 1 character sheet of Pomu showing 7 expressions

## Validation Loop

After generating the first pass:
1. Open the HTML in a browser at iPhone Pro viewport.
2. Compare visually against the screenshot references for tone and atmosphere.
3. Identify any element that "looks generic AI" and revise.
4. Verify all 5 bottom-nav tabs are clearly identifiable.
5. Verify Pomu's presence and personality come through.

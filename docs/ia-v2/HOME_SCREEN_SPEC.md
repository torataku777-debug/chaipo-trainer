# HOME_SCREEN_SPEC.md — Round 1: Home Tab + Bottom Navigation

## Goal

Build a single, standalone HTML file (`home.html`) that renders:
1. **The Home tab content** — the screen users land on after pressing PLAY NOW on the title screen
2. **The bottom navigation** — fixed at the bottom, visible on this screen (and all future screens)

This screen replaces the current "CHAIPO TOWN" mode-selection screen (IMG_2201) and the various sub-mode screens (IMG_2202-2205).

## Layout (top to bottom)

```
┌─────────────────────────────────────┐
│  [Status bar — iOS native]          │
├─────────────────────────────────────┤
│  HEADER STRIP (64px)                │
│  ┌──────┐                  🔔 🎁   │
│  │ Pomu │ プラチナ 3        (icons) │
│  │ Avtr │ レート 1,247                │
│  └──────┘                            │
├─────────────────────────────────────┤
│  HERO CTA (170px)                   │
│  ┌─────────────────────────────┐   │
│  │  ⚔️                          │   │
│  │  ランクマッチ                  │   │
│  │  シーズン1・残り12日             │   │
│  └─────────────────────────────┘   │
│                                     │
│  3 SECONDARY ACTIONS (96px)          │
│  ┌────────┐ ┌────────┐ ┌────────┐ │
│  │カジュアル│ │フレンド │ │  AI   │ │
│  │  😄    │ │  👥    │ │  🤖   │ │
│  └────────┘ └────────┘ └────────┘ │
├─────────────────────────────────────┤
│  MISSIONS CARD (variable)            │
│  📅 今日のミッション      (1/3)        │
│  ─────────────────────────           │
│  ✅ 対戦を1回プレイする                 │
│  ☐ 1勝する                          │
│  ☐ FLに到達する                      │
├─────────────────────────────────────┤
│  DAILY BONUS CARD (88px)             │
│  🎁 ログインボーナス 5日目              │
│  「受け取る」 button                    │
├─────────────────────────────────────┤
│  [spacing 100px to clear bottom nav]│
├─────────────────────────────────────┤
│  BOTTOM NAV (64px + safe area)       │
│  🏠     ⚔️     👥     👑     ☰    │
│ ホーム  対戦  フレンド ランキング その他│
└─────────────────────────────────────┘
```

## Detailed Specifications

### Background

Full-screen background with two layers:
1. **Sky gradient**: `linear-gradient(180deg, var(--bg-sky-top) 0%, var(--bg-sky-bottom) 100%)`
2. **Shibuya building silhouettes**: SVG silhouettes of urban buildings along the bottom 40% of the screen, at 20% opacity. (For prototype: use a simple geometric building silhouette in CSS, no actual image needed.)

Optionally scatter 2-3 small decorative signs (CHAIPO, POKER BRAIN labels) at ~30% opacity in the upper-left and upper-right corners — these are atmospheric, never clickable.

### Header Strip

- Height: 64px
- Padding: `0 var(--space-4)`
- Layout: horizontal flex, items vertically centered
- **Left section** (tap → opens Profile in その他 tab):
  - Pomu avatar circle (48px diameter, white circle with Pomu illustration centered)
  - Two stacked text lines to the right of avatar:
    - Line 1: 段位 — `プラチナ 3` (font-display, 16px, weight 700)
    - Line 2: レート — `レート 1,247` (font-body, 12px, weight 500, text-secondary)
- **Right section**:
  - Bell icon (24px) with red dot badge if notifications exist
  - Gift icon (24px) with red dot badge if daily bonus unclaimed
  - 12px gap between icons

### Hero CTA — ランクマッチ Button

- Width: full (with `var(--space-4)` margins left/right)
- Height: 140px
- Background: orange gradient `linear-gradient(135deg, #F97316 0%, #FB923C 100%)`
- Border-radius: `var(--radius-lg)` (24px)
- Inner padding: `var(--space-5)`
- Shadow: `var(--shadow-md)`
- Content:
  - Top-left small label: `RANK MATCH` in white, 11px, weight 700, letter-spacing 0.15em
  - Center large text: `ランクマッチ` in white, 28px, font-display, weight 800
  - Bottom-left subtitle: `シーズン1・残り12日` in white 80% opacity, 12px
  - Bottom-right: stylized chevron/arrow icon, white
- On active/press: scale to 0.97, brightness 95%

### Secondary Actions Row

- 3 equal-width cards in a horizontal flex with `var(--space-3)` gaps
- Container has `var(--space-4)` left/right margins, `var(--space-4)` top margin
- Each card:
  - Height: 96px
  - Background: `var(--surface-primary)` with backdrop-blur(12px)
  - Border: `1px solid var(--border-subtle)`
  - Border-radius: `var(--radius-md)`
  - Layout: vertical, centered
  - Top: 32px emoji icon (use Unicode emoji for prototype)
  - Bottom: label in 13px, weight 600
- Labels: `カジュアル` / `フレンド` / `AI`
- Icons: `😄` / `👥` / `🤖` (replace with proper SVG later)

### Missions Card

- Margin: `var(--space-4)` left/right, `var(--space-6)` top
- Padding: `var(--space-4)`
- Background: `var(--surface-primary)` with backdrop-blur
- Border-radius: `var(--radius-md)`
- Border: `1px solid var(--border-subtle)`
- Header row (flex, space-between):
  - Left: `📅 今日のミッション` (font-headline, 16px, weight 700)
  - Right: `1/3` badge in pill shape, `var(--accent-warning)` background, white text, 12px
- Divider: `1px solid var(--border-subtle)` with `var(--space-3)` top/bottom margin
- 3 mission rows (vertical stack with `var(--space-3)` gap):
  - Row layout: checkbox (24px) — text (flex 1) — reward badge (right)
  - Mission 1: ✅ `対戦を1回プレイする` `+10 XP` (completed, line-through, text-tertiary)
  - Mission 2: ☐ `1勝する` `+30 XP`
  - Mission 3: ☐ `FLに到達する` `+50 XP`
- Checkboxes: completed = green filled circle with white checkmark; active = empty circle with `var(--border-strong)` border

### Daily Bonus Card

- Same margins/padding pattern as Missions Card
- Margin top: `var(--space-3)` (closer to missions)
- Background: warm gradient `linear-gradient(135deg, rgba(255, 248, 230, 0.9) 0%, rgba(255, 237, 213, 0.9) 100%)`
- Layout: horizontal flex, space-between
  - Left: gift icon (32px) + two lines stacked
    - Line 1: `ログインボーナス` (14px, weight 600)
    - Line 2: `5日連続!` (12px, text-secondary)
  - Right: `受け取る` button — orange pill (`var(--accent-primary)` background, white text, 14px weight 700, padding `var(--space-2) var(--space-4)`, border-radius pill)

### Bottom Navigation (CRITICAL — appears on all screens)

- Position: fixed bottom, full width
- Height: 64px + env(safe-area-inset-bottom)
- Background: `var(--surface-elevated)` with `backdrop-filter: blur(20px)`
- Top border: `1px solid var(--border-subtle)`
- Z-index: 100
- 5 tabs in equal-width flex
- Each tab content:
  - Vertical stack, centered
  - Icon (24px line icon)
  - Label below (10px, weight 600)
  - 4px gap between icon and label
- 5 tabs in order (left to right):
  1. `ホーム` — house icon — ACTIVE state on home screen
  2. `対戦` — crossed swords icon
  3. `フレンド` — two people icon
  4. `ランキング` — trophy/crown icon
  5. `その他` — three horizontal lines icon
- Active tab indicator:
  - Icon stroke color: `var(--accent-primary)`
  - Label color: `var(--accent-primary)`
  - 3px wide × 3px tall orange dot 4px above the icon (or below the bottom-edge — your choice, pick what looks better)
- Inactive tabs:
  - Stroke + label color: `var(--text-tertiary)`
- Tap states: brightness 90% on press

For icons, use inline SVG line icons (1.5-2px stroke), or import Lucide icon SVGs and inline them. Do NOT use icon fonts.

## Pomu Avatar Placeholder

For this prototype, use a CSS-drawn circle with a yellow rounded rectangle (the pineapple) on top, or a placeholder image. The actual Pomu artwork will be inserted later. Important: the avatar should be a circle with a 2px border in `var(--accent-secondary)` (teal), signaling that it's interactive.

## Interactivity (for prototype)

- All buttons should have a subtle press animation (scale 0.97, brightness 95%, 100ms transition).
- Tapping a bottom-nav tab switches the active state visually (no actual page change, since this is one HTML file).
- Tapping `ランクマッチ` shows a console.log message — no navigation.

## Deliverable

A single `home.html` file containing:
- `<!DOCTYPE html>`, full HTML5 structure
- Inline `<style>` with all CSS using the design tokens
- Inline `<script>` for the tap interactions
- Comments explaining each section
- Designed for 393×852 viewport, but responsive in spirit (don't break on slightly larger or smaller widths)

Once `home.html` looks right, we'll proceed to other tabs (対戦, フレンド, ランキング, その他) using this same design system.

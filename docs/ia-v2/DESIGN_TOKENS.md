# DESIGN_TOKENS.md — Chaipo Neighbors Design System

All colors, typography, and spacing should reference these tokens. Do not introduce new values without documenting them here.

## Color Tokens

### Background (atmospheric, the "world")
- `--bg-sky-top`: `#87CEEB` (light sky blue, top of gradient)
- `--bg-sky-bottom`: `#E0F2FE` (paler blue, bottom of gradient)
- `--bg-cloud`: `#FFFFFF` (with 40-60% opacity for cloud overlay)

Use this gradient on the home screen full background. Decorative Shibuya building silhouettes can be placed as low-opacity SVG overlays (~15-25% opacity) so they don't compete with the foreground.

### Surface (UI cards, floating above the world)
- `--surface-primary`: `rgba(255, 255, 255, 0.85)` — main cards, frosted glass
- `--surface-elevated`: `rgba(255, 255, 255, 0.95)` — modal/important cards
- `--surface-muted`: `rgba(255, 248, 230, 0.75)` — secondary cards (warm cream)

Apply `backdrop-filter: blur(12px)` to surfaces over the sky background to create the frosted glass effect.

### Text
- `--text-primary`: `#1A202C` (near-black, never pure black)
- `--text-secondary`: `#4A5568` (muted body text)
- `--text-tertiary`: `#A0AEC0` (captions, hints)
- `--text-inverse`: `#FFFFFF` (text on colored buttons)

### Accent Colors (use sparingly, max 2 per screen)
- `--accent-primary`: `#F97316` (orange — main CTA, e.g. "ランクマッチ" button)
- `--accent-secondary`: `#14B8A6` (teal — secondary actions, matches existing chip color)
- `--accent-success`: `#22C55E` (green — completed missions, wins)
- `--accent-warning`: `#EAB308` (amber — daily bonus, attention)
- `--accent-danger`: `#EF4444` (red — foul, errors)

### Borders & Dividers
- `--border-subtle`: `rgba(0, 0, 0, 0.06)` — card edges
- `--border-strong`: `rgba(0, 0, 0, 0.12)` — separators

## Typography

### Font Families
- `--font-display`: `'Orbitron', 'Noto Sans JP', sans-serif` — titles, numbers, brand
- `--font-body`: `'Noto Sans JP', 'Helvetica Neue', sans-serif` — body, UI text
- `--font-mono`: `'JetBrains Mono', monospace` — codes, timers

### Type Scale (mobile-first)
- `--text-display`: `28px / 36px` (line-height), weight 800 — page titles
- `--text-headline`: `20px / 28px`, weight 700 — section headers
- `--text-body-lg`: `16px / 24px`, weight 500 — primary body
- `--text-body`: `14px / 20px`, weight 400 — secondary body
- `--text-caption`: `12px / 16px`, weight 500 — labels, captions
- `--text-tab-label`: `10px / 14px`, weight 600 — bottom nav labels

Japanese text should have `letter-spacing: 0.02em` and English/numeric titles `letter-spacing: -0.01em`.

## Spacing Scale (4px base)

- `--space-1`: `4px`
- `--space-2`: `8px`
- `--space-3`: `12px`
- `--space-4`: `16px`
- `--space-5`: `20px`
- `--space-6`: `24px`
- `--space-8`: `32px`
- `--space-10`: `40px`
- `--space-12`: `48px`
- `--space-16`: `64px`

## Border Radius

- `--radius-sm`: `8px` — small badges, chips
- `--radius-md`: `16px` — cards, buttons
- `--radius-lg`: `24px` — hero cards
- `--radius-full`: `9999px` — pills, avatars

## Shadows

Use sparingly. The frosted glass effect is the primary depth cue.

- `--shadow-sm`: `0 1px 2px rgba(0,0,0,0.04), 0 1px 1px rgba(0,0,0,0.04)`
- `--shadow-md`: `0 4px 12px rgba(0,0,0,0.06), 0 2px 4px rgba(0,0,0,0.04)`
- `--shadow-lg`: `0 12px 32px rgba(0,0,0,0.08), 0 4px 8px rgba(0,0,0,0.06)`

## Component Patterns

### Bottom Navigation
- Height: `64px` + safe-area-inset-bottom
- Background: `var(--surface-elevated)` with `backdrop-filter: blur(20px)`
- Top border: `1px solid var(--border-subtle)`
- 5 equal-width tabs
- Each tab: vertical stack — icon (24px) + label (text-tab-label)
- Selected state: icon and label use `var(--accent-primary)`, 3px orange dot under icon
- Non-selected: `var(--text-tertiary)`
- Touch target: full tab area, minimum 48×48px

### Primary CTA Button
- Background: `var(--accent-primary)`
- Text: `var(--text-inverse)`, `text-headline` size
- Padding: `var(--space-4) var(--space-6)`
- Border-radius: `var(--radius-md)`
- Min height: `56px` (large, thumb-friendly)
- Active state: 96% scale, brightness 90%

### Secondary Action Card (mode buttons)
- Background: `var(--surface-primary)` with backdrop-blur
- Border: `1px solid var(--border-subtle)`
- Padding: `var(--space-4)`
- Border-radius: `var(--radius-md)`
- Min height: `80px`
- Icon at top, label below

### Mission Item
- Row layout: checkbox (left) + text (center) + reward badge (right)
- Completed: line-through text, green checkmark
- Active: empty circle, primary text color

## Brand Assets to Reference

- **Pomu mascot**: white round fluffy bird with pineapple on head. 7 expression variants exist (smile, neutral, side-view, back, small, eye-closed).
- **Pineapple icon**: simple cartoon pineapple, yellow body + green leaves.
- **Chaipo chip**: teal/white casino chip with pineapple inside.
- **Decorative signs**: grunge urban signage style — "CHAIPO", "POKER BRAIN", "LEVEL UP", "TRAIN SMART". Use as low-opacity background decoration ONLY, not as functional buttons.

## Don'ts (Recap)

- Don't invent a 6th accent color
- Don't use pure black (#000) anywhere
- Don't use Material Design icons (looks generic) — use Lucide line icons or custom
- Don't use Open Sans, Roboto, or Inter — stick to Noto Sans JP + Orbitron
- Don't add shadow + border + backdrop-blur all at once on the same element

---
name: classic-visual-parity
description: >-
  [MM] Classic-site visual CSS ကို SPFx module.scss ထဲ pixel-level clone:
  font-size, font-weight, font color, BG, spacing, Gap, margin, padding,
  break line, letter spacing, line height, hover, animation, @media။
  Trigger: classic ASPX → SPFx, classic နဲ့ မတူ, font-weight ပါး/ထူ, menu underline,
  style.css, OpenSans, UIKit, Bootstrap, hover, animation, mobile/tablet,
  DBS-FFW-classicsite responsive layout.
source: _cursor/skills/classic-visual-parity/SKILL.md
---

# Classic Visual Parity (blocking)

ဤ repo = **visual clone** — Fluent redesign မဟုတ်။

**Visual source of truth** = classic CSS — Fluent defaults / SharePoint theme slots / glassmorphism မဟုတ်။

| Source | Path |
|--------|------|
| Primary CSS | `DBS-FFW-classicsite/2025/style.css` |
| SASS sources | `DBS-FFW-classicsite/2025/sass/` (`style.sass`, `_home`, `_fonts`) |
| Page markup | `DBS-FFW-classicsite/2025/*.aspx` (chrome = inline `header.page-banner`) |
| Vendor layout | `2025/public/css/vendor/uikit.min.css` + Swiper + hamburgers **page က သုံးသည့် classes သာ** — `uk-*` leftover အတွက် `uikit-to-spfx-visual-parity` load |
| Motion / carousel | Swiper → `swiper-to-spfx-carousel` (init + scoped nav); lottie, anime, FullCalendar (သုံးသည့် rules သာ) |
| Fonts | `DBS-FFW-classicsite/2025/public/Fonts/opensans-condensed/` (OpenSans-Condensed-ExtraBold / Bold / Regular / Light) |
| Target | `DBS-FFW-SPFX/src/webparts/**/*.module.scss` နှင့် `src/shared/**` |

rem / Fluent density / theme tokens **မမှန်း**။ Classic values ကူး။

## Conflict overrides (ဤ repo)

Classic → SPFx UI မှာ ဤ skill က အောက်ပါတို့ကို နိုင်:

- `spfx-enterprise-design-core` “do not rely on pixel-perfect” / 480–1024 heuristics → **classic နဲ့ pixel-perfect required**; classic `@media` px ကူး
- `06-surface-quality` no-px / Fluent breakpoints → **classic `px` / hex / `@media` widths required**
- `spfx-theme-and-brand-integration` semantic slots / no hardcoded color → **classic hex hardcode**
- `spfx/references/react-design.md` Fluent v9 / inherit host theme → **control လိုမှ Fluent v8; visual values = classic**
- glassmorphism / Fluent glass tokens → DBS-FFW-classicsite page chrome သို့ body UI မှာ **မသုံး**
- `07-testing-gate` gulp/list smoke → **မလုံလောက်**; အထက် visual rows = blocking

ထား: CSS modules (documented host-gap paints မှလွဲ global chrome မယို), keyboard/focus names, classic animation ကို `prefers-reduced-motion` wrap (reduced-motion မဟုတ်သူများအတွက် effect **မဖြုတ်**)။

## When (ဤ tasks မှာ အမြဲ)

- Classic page / web part migrate သို့ visual tweak မဆို
- User ပြော: font-size, **font-weight**, font color, BG color, spacing, Gap, margin, padding, break line, letter spacing, line height, hover effect, animation effect, responsive, @media, mobile, tablet, breakpoint, **ထူ**, **ပါး**, **bold**, **underline**, OpenSans
- “classic နဲ့ မတူ” / look & feel / spacing mismatch / mobile မတူ

## Workflow (page ပြီးဟု မကြေညာမီ)

### 1) CSS inventory (SCSS မတိုင်မီ ကုဒ်)

ပြင်နေသော slice အတွက် classic `style.css` + ကိုက်ညီ `sass/` partials + ASPX classes + သုံးသည့် UIKit/Bootstrap classes ဖတ်။ Token table ဆောက်။ အောက် rows **မဖြစ်မနေ** — ကျော်မရ:

- font-size
- font-weight
- font color
- BG color
- spacing
- Gap
- margin
- padding
- break line
- letter spacing
- line height
- hover effect
- animation effect
- responsive / @media (slice သက်ရောက်သည့် classic query တိုင်း — `max-width` px တူကူး; ဤ repo = 1200, 1024, 959, 768, 640, 480)

ထပ်ဖမ်း: `font-family` (year-correct OpenSans named faces — [visual-typography.md](../classic-to-spfx-migration/references/visual-typography.md)), `border` / `border-radius`, `box-shadow`, `background-image` / gradient, ASPX က သုံးသည့် Swiper/hamburgers နှင့် UIKit `uk-*`။

Fluent 480 / 1024 heuristics **မအစား**။ Classic breakpoints အများကြီးကို တစ်ခုတည်း **မပေါင်း**။

Class toggle လုပ်သော controller JS (active tab, hover class, uk-active) = **class semantics တူ** ထားမှ CSS သက်ရောက်ဆက်ရှိ။

### 2) Port exact values

- `*.module.scss` ထဲရေး။ Tailwind / SPA routers မထည့်။
- ရှိပြီး OpenSans-Condensed `@font-face` ပြန်သုံး (classic `DBS-FFW-classicsite/2025/public/Fonts/opensans-condensed/`)။ ဒုတိယ font stack မတီထွင် (`Segoe UI` = OpenSans-Condensed နောက် fallback သာ)။
- `DBS-FFW-SPFX/src/shared/` မှာ shared tokens partial ရှိရင် ပြန်သုံး။ Package အသစ် **မဖန်**။ Shared partial မရှိမှသာ web part တိုင်း `@font-face` duplicate။
- `:global` host paints (`#FFFFFF` on canvas) = classic `body`/`html` background က Modern chrome gaps ဖြည့်မှသာ — suite nav / command bar **မပြန် style**။
- `br` / `white-space` / empty paragraph spacing: classic break line ထိန်း; Fluent Text spacing သို့ **မပေါင်း**။
- Hover / animation: `:hover`, `transition`, `@keyframes`, UIKit hover classes ပို့။ Hover ဖြုတ်ပြီး Fluent hover-only-avoidance **မလုပ်**။
- Responsive: ကိုက်ညီ `@media screen and (max-width: Npx)` (classic မှာ `min-width` ရှိရင်ပါ) **N တူ** ပို့။ Query အတွင်း stack / wrap / hide / width / font-size / spacing ပြောင်းလဲမှု တူကူး။ Host canvas က classic full page ထက် ကျဉ်းနိုင် — classic queries ဆက်သုံး; Modern chrome “ပြင်” ရန် extra breakpoints မတီထွင်။

### 2b) Typography self-check (blocking — parity PASS မတိုင်မီ)

[visual-typography.md](../classic-to-spfx-migration/references/visual-typography.md) **ဖတ်**ပြီး UI slice တိုင်း mandatory self-check:

1. Classic `font-family` / `font-weight` / menu `text-decoration` vs `*.module.scss` Grep
2. Named-face rule: `OpenSans-Bold` / SemiBold / Condensed-Bold → **`font-weight: 400`**
3. Menu/nav `<a>`: classic မှာ underline မရှိရင် `text-decoration: none` (SharePoint host)
4. တိုတောင်း **Typography self-check** table ထုတ် (selector · family · weight · link deco · OK/FIX)

ဤ table မရှိဘဲ parity PASS / visual typography task ပိတ် **မလုပ်**။

### 3) Blocking gate

Inventory row တစ်ခုခု classic နဲ့ ကွာနေသေးရင် (value မှား, hover ပျောက်, animation ပျောက်, Fluent gap အစားထိုး, `@media` width မှား/ပျောက်, classic အစား Fluent 480px) migrate သို့ visual update **မပြီး**။

“looks close” / “Fluent-aligned is enough” / “desktop is fine, mobile later” **မပြော**။

## Validation (manual smoke — visual)

Classic page vs SPFx workbench/served page ဘေးချင်း၊ breakpoint တူ:

1. font-size, font-weight, font color, BG color
2. spacing, Gap, margin, padding, break line
3. letter spacing, line height
4. hover effect, animation effect
5. **Responsive (blocking):** slice ၏ classic `@media` တိုင်း — breakpoint px တူ; stack / wrap / hide / width ကိုက်။ Classic widths မှာ spot-check — 480px သာ မဟုတ်။

ပြီးမှ Testing Gate (`gulp bundle` / ရှိပြီး tests) + controls keyboard/focus။

## Anti-patterns

- Data/React ပြီးသော် SCSS Fluent defaults ဆက်ရှိ WP ကို ပြီးဟု သတ်
- Classic Bold/SemiBold selectors မှာ SPFx `font-weight: 400` မရှိဘဲ typography self-check ကျော်
- Menu links classic CSS ကူးပြီး SharePoint host underline `<a>` မှာ ကျန်
- Classic hex ကို `[theme:..., default: ...]` သို့ glassmorphism CSS variables အစား
- ဤ clone မှာ a11y အတွက် classic px → rem (user က classic match တောင်း)
- ဤ pages မှာ glassmorphism / Fluent glass tokens
- `uikit.min.css` အားလုံး SPFx ထဲ ကူး — page သုံးသည့် classes သာ module ထဲ inline
- Classic `@media` widths ကို Fluent 480 / 1024 heuristics အစား
- Desktop-only SCSS ပို့ပြီး mobile နောက်မှ

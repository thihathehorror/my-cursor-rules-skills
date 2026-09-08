---
name: uikit-to-spfx-visual-parity
description: >-
  [MM] UIKit (uikit.css / uk-* classes) visual values ကို SPFx module.scss ထဲ ပို့ —
  gap, padding, margin, font-size, animation မကျန်စေ။ Trigger: DBS-FFW-classicsite
  UIKit classic → SPFx, spacing/type classic နဲ့ မှား, UIKit, uk-grid, uk-margin,
  uk-modal, uk-sticky, uk-animation, leftover gap/padding/margin/font-size/animation.
source: _cursor/skills/uikit-to-spfx-visual-parity/SKILL.md
---

# UIKit → SPFx visual parity (ဤ repo)

Classic UIKit pages = **page CSS + UIKit + Bootstrap**။ `style.css` သာ `*.module.scss` ထဲ ကူးရင် `uikit.min.css` / `uikit.min.js` / Bootstrap ထဲရှိသမျှ ကျန်။

Vendor ဖိုင်အပြည့် SPFx ထဲ **မload**။ Page က အစစ်သုံး `uk-*` rules **သာ** inline။

`classic-visual-parity` နဲ့တွဲ load (paths + mandatory token rows)။ ဤ skill = ထို rows မကြာခဏ လွတ်သည့် **UIKit leftover layer**။

| Role | Path |
|------|------|
| UIKit CSS | `DBS-FFW-classicsite/2025/public/css/vendor/uikit.min.css` |
| UIKit JS | `DBS-FFW-classicsite/2025/public/js/vendor/uikit.min.js` |
| Markup | `DBS-FFW-classicsite/2025/*.aspx` (inline `header.page-banner`) |
| Page CSS | `DBS-FFW-classicsite/2025/style.css` + `sass/` |
| Target | `DBS-FFW-SPFX/src/webparts/**/*.module.scss` နှင့် `src/shared/**` |

## Failure mode (မျှော်လင့်)

| Left behind | Why |
|---|---|
| Gap | `uk-grid` / `uk-grid-*` = CSS `gap` **မဟုတ်**။ Negative `margin-left` + child `padding-left` (row `margin-top`)။ `gap: Npx` ခန့်မှန်းရင် container-edge alignment မကြာခဏ လွတ်။ |
| Padding | `.uk-modal-body`, `.uk-offcanvas-bar`, `.uk-padding-*` = UIKit ထဲ၊ page CSS မဟုတ်။ |
| Margin | `.uk-margin` / `.uk-margin-*` (form fields မှာ 20px stack မကြာခဏ)။ |
| Font-size | UIKit က `html { font-size: 16px }` + utilities အများ `rem`။ SPFx host root font ကွာ → rem drift။ |
| **Line-height (headings)** | UIKit `h2 { line-height: 1.3 }` (`h1` 1.2, `h3` 1.4)။ Page `style.css` က `h2` **font-size** သာ override မကြာခဏ — live classic title height = UIKit line-height × page font-size။ SPFx root `line-height: 28px` က titles ကို **28px** inherit စေ — မပို့ရင်။ |
| Animation | `.uk-animation-*` = `@keyframes` + duration။ UIKit JS က modal/offcanvas animate။ `transition` တစ်ခုတည်း မလုံလောက်။ |

မပို့ရင် ကျန်: `uk-hidden@*` / `uk-visible@*` (UIKit breakpoints မှာ show/hide), `uk-child-width-*`, `uk-flex*`, `uk-width-*`, `uk-sticky`, `uk-table`။

CSS Modules က class names hash။ JSX မှာ `uk-grid` ထည့်ရုံ **ဘာမှမဖြစ်** — rule က module ထဲရှိမှ (သို့ `:global` = အများအားဖြင့် မှားသော ပြင်ချက်)။

ဤ site သုံး (ASPX မှာ အတည်ပြုပြီးမှ ပို့): `uk-container`, `uk-img`, `uk-grid`, `uk-flex`။ Slice ASPX ပြန်ဖတ် — InsightsBank modal/sticky classes **မယူဆ**။

## When

- ဤ site classic → SPFx UI migrate သို့ visual tweak မဆို
- SPFx clone က classic ထက် တင်း/လျော့/static
- User က leftover **gap, padding, margin, font-size, animation** / UIKit / `uk-*` ပြော

## Workflow

### 1) သုံးသည့် `uk-*` သာ inventory

Slice ASPX မှ `uk-*` class တိုင်း + UIKit component attribute (`uk-grid`, `uk-container`, `uk-img`, `uk-flex`) စာရင်း။ တစ်ခုချင်း **computed rule** ကို `DBS-FFW-classicsite/2025/public/css/vendor/uikit.min.css` မှ ထုတ် (အခြား UIKit version မယူဆ)။

Mandatory token rows (ကျော်မရ) — `classic-visual-parity` နဲ့တူ:

- font-size / font-weight / font color / BG color
- spacing / **Gap** / **margin** / **padding** / break line
- letter-spacing / line-height
- hover / **animation** (`:hover`, `transition`, `@keyframes`)
- responsive `@media` — classic/UIKit **px တူ** ကူး; ဤ repo = 1200, 1024, 959, 768, 640, 480။ Fluent-only 480/1024 **မအစား**

### 2) `*.module.scss` ထဲ ပို့

- React/CSS-module classes ပေါ် equivalent selectors (`uk-*` → module classes ပြောင်းအမည်)။
- **px / hex / duration တိကျ** ကူး။ a11y အတွက် rem မပြောင်း။ Fluent density / theme slots ကို look **မသုံး**။
- Grid: negative-margin + child padding မော်ဒယ်တူ ဦးစားပေး။ CSS `gap` = ဘေးချင်း proof ပြီး edges/gutters တူမှ။
- Animation: slice သုံး `@keyframes` ပို့။ `prefers-reduced-motion` wrap (လူတိုင်းအတွက် effect **မဖြုတ်**)။
- Responsive: `uk-hidden@m` / `uk-visible@m` = ဤ UIKit ဖိုင်၏ `min-width` / `max-width` px တူ (`@m` = 960px)။
- Host: SharePoint `ControlZone` padding/margin reset က spacing စားနိုင် — web part root မှာ ပြန်ဖြည့်; suite nav **မပြန် style**။

ဤ repo `uikit.css` **UIKit 3** defaults (ဖိုင်ပြောင်းရင် ပြန်ဖတ်):

| Class / component | Value in this vendor file |
|---|---|
| `html` | `font-size: 16px`; `line-height: 1.5` |
| **`h2`, `.uk-h2`** | **`line-height: 1.3`** (page CSS က `font-size` သာ override နိုင် — ဤတန်ဖိုး ဆက်ပို့) |
| `h1`, `.uk-h1` | `line-height: 1.2` |
| `h3`, `.uk-h3` | `line-height: 1.4` |
| `.uk-grid` | `display: flex; flex-wrap: wrap; margin-left: -30px` + `> * { padding-left: 30px }` |
| `.uk-grid-medium` | 30px gutter; row `margin-top: 30px` |
| `.uk-margin` | `margin-bottom: 20px`; `* + .uk-margin { margin-top: 20px }` |
| `.uk-modal-body` | `padding: 30px` |
| `.uk-modal-dialog` | `width: 600px`; open: `opacity` + `translateY(-100px)` → `0` over `.3s linear` |
| `.uk-offcanvas-bar` | `width: 270px`; `padding: 20px` |
| `[class*=uk-animation-]` | `animation-duration: .5s`; `ease-out`; `both` |
| `.uk-animation-slide-top-small` | `@keyframes` `opacity: 0` + `translateY(-10px)` |
| `@s` / `@m` / `@l` / `@xl` | 640 / 960 / 1200 / 1600 |

`uk-grid` JS က wrapped rows ပေါ် `uk-grid-margin` ထည့်။ JS ကျော်ရင် row gap ကို SCSS မှာ ဆက်ပြန်ထုတ်ရ။ `uk-sticky` / `uk-modal` / `uk-toggle` = React state + CSS — `uikit.js` **မကူး**။

### 3) Blocking gate

Inventory row ကွာနေ၊ `uk-*` class name ကျန်ပြီး module rule မရှိ၊ `uikit.css` အပြည့် bundle၊ Fluent `gap`/480px အစားထိုး — **မပြီး**။

**UIKit section titles (`h2` / `.main-title` inside `uk-container`):** `h2` ပေါ် **`line-height: 1.3`** ပို့ — slice ASPX မှာ `h2` titles မရှိမှလွဲ — [visual-typography.md](../classic-to-spfx-migration/references/visual-typography.md) Step 3b။ Headings ပေါ် WP root `line-height: 28px` **မထား**။

**UIKit body copy (`p` in `.card-wrap` / `uk-container`):** classic က `OpenSans-Regular` သုံးရင် WP root + `p` ပေါ် **`font-weight: 400`** — visual-typography Step 3c။ Card paragraphs ပေါ် host-inherited light weight **မထား**။

“looks close” သို့ “desktop is fine, mobile later” **မပြော**။

## Validation

Slice သုံးသည့် classic/UIKit breakpoint **တိုင်း** မှာ classic vs SPFx ဘေးချင်း:

1. font-size, weight, color, BG
2. gap/gutter, margin, padding, break line
3. letter-spacing, line-height
4. hover + animation (keyframes, modal/sticky motion)
5. `uk-hidden@*` / `uk-visible@*` show-hide နှင့် child widths

ပြီး `DBS-FFW-SPFX` မှာ `gulp bundle`။ Bundle အောင်ရုံ visual match **blocking**။

## Anti-patterns

- `uikit.css` / `uikit.js` အားလုံး SPFx ထဲ ကူး
- `style.css` သာ ပို့ပြီး UIKit/Bootstrap ကို unused vendor သတ်
- `uk-grid` ကို စိတ်ကြိုက် CSS `gap` အစား
- CSS Modules အောက် `uk-*` class names ထားပြီး rules မပို့
- Classic/UIKit `@media` px ကို Fluent 480 / 1024 အစား
- `@keyframes` ဖြုတ်ပြီး hover-only သို့ motion မရှိ ပို့
- UIKit `px`/`rem` ကို theme tokens သို့ glassmorphism ပြောင်း

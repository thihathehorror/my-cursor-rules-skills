---
name: spfx-enterprise-ux-hub
description: >-
  [MM] Generic (non-clone) SPFx UX skills index။ DBS-FFW-classicsite classic →
  SPFx page clones အတွက် ပထမ skill မဟုတ် — classic-to-spfx-migration,
  classic-visual-parity, uikit-to-spfx-visual-parity သုံး။
source: _cursor/skills/spfx-enterprise-ux-hub/SKILL.md
---

# SPFx Enterprise UX Hub

**ဤ repo (DBS-FFW-classicsite):** classic → SPFx အတွက် ဤနေရာမှ **မစ**။ `classic-to-spfx-migration` + `classic-visual-parity` + `uikit-to-spfx-visual-parity` မှ စ။ Gulp 1.20 သာ။ Glassmorphism မရှိ။ Heft မရှိ။

ဤ skill = generic (non-clone) SPFx UX အတွက် **global index**။ ထို tasks အတွက်:

1. သက်ဆိုင်သော **specialized SPFx skills** ဆုံးဖြတ်။
2. Context ပါးရန် ထို skills သာ load။

Classic `style.css` clone **မဟုတ်**သော SharePoint Framework UX အတွက် ဤ hub သုံး။

---

## 1. Skill map (ဘယ်အခါ ဘယ် skill)

### 1.1 Design & content (ဦးစားပေး)

- **`spfx-enterprise-design-core`**  
  သုံးရန်: layout, information hierarchy, web part levels, titles/descriptions, commanding, placeholders, empty/loading/error states, responsive design။

- **`spfx-accessibility-and-content-quality`**  
  သုံးရန်: keyboard/focus patterns, screen-reader semantics, empty/error text quality, recovery paths, overall UX text tone။

### 1.2 Theme, brand, and styling

- **`spfx-theme-and-brand-integration`**  
  သုံးရန်: theme tokens, semantic slots, high-contrast နှင့် dark mode, Brand Center fonts, tenant-safe branding။

- **`spfx-css-and-styling-governance`**  
  သုံးရန်: SCSS module structure, selector scoping, naming conventions, web parts ကြား style leakage တား။

- **`classic-visual-parity`**  
  သုံးရန်: **ဤ repo** classic → SPFx page clone (font-size, color, spacing, hover, animation, `@media` / responsive)။ Visual SoT = `DBS-FFW-classicsite/2025/style.css`။ Theme-slot / glassmorphism / Fluent 480 defaults အစား ဤ skill။

- **`uikit-to-spfx-visual-parity`**  
  သုံးရန်: UIKit leftover layer (`uk-grid` gutter, `uk-margin`, modal/offcanvas padding, rem font-size, `@keyframes`)။ Classic UI migrate တိုင်း `classic-visual-parity` နဲ့တွဲ load။

### 1.3 Behavior & configuration

- **`spfx-property-pane-reactivity`**  
  သုံးရန်: reactive vs non-reactive property pane ရွေးခြင်း၊ performance မထိခိုက်သော property editing UX။

- **`spfx-extensions-enterprise-patterns`**  
  သုံးရန်: Application Customizers, Field Customizers, Command Sets; dialog patterns; host page context လေးစား။

### 1.4 Data, implementation, and performance

- **`spfx-enterprise-code-and-performance`**  
  သုံးရန်: code structure, data access patterns (REST, Graph, PnPjs), performance optimization, recommended npm packages။

- **`spfx-enterprise-implementation-core`**  
  သုံးရန်: service boundaries, typed interfaces, error/loading handling, module structure, maintainability။

- **`spfx-image-and-media-optimization`**  
  သုံးရန်: image sizing, lazy loading, responsive media, performance-aware image handling။

### 1.5 Release, packaging, and toolchain

- **`spfx-release-and-package-quality`**  
  သုံးရန်: package-solution configuration, versioning, app catalog readiness, release checklists။ ဤ repo: gulp (`gulp bundle` / `gulp serve`), Heft မဟုတ်။

---

## 2. AI editor က ဤ hub သုံးပုံ

SPFx task ကိုင်သည့်အခါ:

1. **Task အမျိုးအစား ခွဲ**
   - Classic site visual clone (DBS-FFW-classicsite pages)? → ရပ်; `classic-to-spfx-migration` + `classic-visual-parity` + `uikit-to-spfx-visual-parity` (ဤ hub မဟုတ်၊ glassmorphism မဟုတ်၊ Fluent density မဟုတ်၊ Heft မဟုတ်)။
   - Pure UX/design (non-clone)? → `spfx-enterprise-design-core`, `spfx-accessibility-and-content-quality`။
   - Theming/visual alignment (non-clone)? → `spfx-theme-and-brand-integration`, `spfx-css-and-styling-governance`။ ဤ repo မှာ glassmorphism မဟုတ်။
   - Configuration/behavior? → `spfx-property-pane-reactivity`, `spfx-extensions-enterprise-patterns`။
   - Data & implementation? → `spfx-enterprise-implementation-core`, `spfx-image-and-media-optimization`။
   - Release/build? → `spfx-release-and-package-quality` + gulp (`gulp bundle` / `gulp serve`)။ Heft မဟုတ်။

2. **သက်ဆိုင် skills သာ load**  
  SPFx skills အားလုံး တစ်ခါတည်း **မload**။ အနည်းဆုံး set ရွေး။

3. **Microsoft guidance သုံး**  
  Specialized skill တိုင်း Microsoft docs နဲ့ ကိုက် patterns encode (design, theming, image helper API, စသည်)။ User အတိအလင်း override မခိုင်းလျှင် ထို patterns default။ ဤ repo = gulp 1.20။

4. **Enterprise-grade UX ပန်းတိုင်**  
  SPFx ပြောင်းလဲမှုတိုင်း:
   - Accessible (keyboard, screen reader, color contrast)
   - Performance-aware (UI သို့ property pane မှာ heavy blocking မရှိ)
   - Theme- နှင့် tenant-safe (semantic slots, hard-coded brand colors မရှိ) — **ခြွင်းချက်** ဤ repo classic clone: `DBS-FFW-classicsite/2025/style.css` မှ classic CSS hard-code
   - Classic visual clone: page ပြီးဟု မကြေညာမီ `style.css` pixel match
   - Maintainable (module boundaries ရှင်း၊ typed APIs၊ toolchain hacks အနည်းဆုံး)

---

## 3. Quick decision checklist

SPFx task တိုင်း အမြန်ဖြေ:

1. **ဤပြောင်းလဲမှု UI/UX ထိသလား?**  
   - Classic clone (ဤ repo)? → `classic-to-spfx-migration` + `classic-visual-parity` + `uikit-to-spfx-visual-parity` + a11y names သာ။
   - Other SPFx → `spfx-enterprise-design-core` နှင့် `spfx-accessibility-and-content-quality`။

2. **Colors, fonts, visual style, responsive layout ထိသလား?**  
   - Classic clone (ဤ repo pages) → `classic-visual-parity` + `uikit-to-spfx-visual-parity` ထည့် (classic `@media` px, theme slots / glassmorphism / Fluent 480 မဟုတ်)။
   - Other SPFx → `spfx-theme-and-brand-integration` နှင့် `spfx-css-and-styling-governance` ထည့်။

3. **Configuration / property panes ထည့်/ပြင်သလား?**  
   - Yes → `spfx-property-pane-reactivity` ထည့်။

4. **Images/media ထည့်/ပြင်သလား?**  
   - Yes → `spfx-image-and-media-optimization` ထည့်။

5. **Release သို့ pipeline အလုပ်လား?**  
   - Yes → `spfx-release-and-package-quality` ထည့်။ ဤ repo: gulp, Heft မဟုတ်။

**ဤ repo** classic migrate အတွက် ဤ hub ကို ပထမမှတ် **မသုံး**။

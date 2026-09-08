---
name: classic-to-spfx-migration
description: >-
  [MM] SharePoint Classic (ASPX/CEWP/JSOM/jQuery) ကို SPFx web parts/extensions သို့
  style.css pixel-level visual parity ဖြင့် ပြောင်း။ Trigger: classic site migration,
  ASPX to SPFx, CEWP/SEWP, JSOM to PnPjs, Style Library, DBS-FFW-classicsite
  (FFW / LFC home, past-events, back-door), bulk scaffold / baseline wave,
  classic look (font, color, spacing, hover, animation, @media) SPFx နဲ့ မတူ။
---

# Classic Site → SPFx Migration

**DBS-FFW** classic → SPFx အတွက် ပရောဂျက် playbook။

## Repo layout (path မမှန်းဆရ)

| Role | Path |
|------|------|
| Classic source | `DBS-FFW-classicsite/` — year folders `2023/` `2024/` `2025/` (`.aspx`, `style.css`, `sass/`, `public/`) |
| Visual SoT (လက်ရှိ) | `DBS-FFW-classicsite/2025/` (`index.aspx`, `past-events.aspx`, `style.css`, `sass/`) |
| SPFx target | `DBS-FFW-SPFX/` (**Ffw** web part scaffold ပြီး) |

User က year အမည်မခေါ်လျှင် `2023/` / `2024/` ကို live migrate target **မသတ်မှတ်**။

## Project pins (အမြဲလိုက်နာ)

Scaffold / upgrade မပြောမီ `DBS-FFW-SPFX/package.json` ဖတ်။

| Concern | This repo |
|---------|-----------|
| SPFx | **1.20.x** |
| Toolchain | **gulp** (`gulp bundle` / `gulp serve` / `gulp test`) — Heft မဟုတ် |
| React | **17** |
| UI | **Fluent UI v8** (`@fluentui/react`) — user upgrade မခိုင်းလျှင် Fluent v9 မဟုတ် |
| Node | engines in package.json (`>=18.17.1 <19.0.0`) |

`spfx` skill load သည့်အခါ **gulp** path သုံး — Heft/Fluent v9 default **မတွန်း**။

**Load order (ဤ repo):** ဤဖိုင် (appendix အပါ) → `classic-visual-parity` → **[visual-typography.md](./references/visual-typography.md) (UI migrate မှာ required — typography self-check)** → `uikit-to-spfx-visual-parity` → data ရှိရင် `spfx`/`pnpjs.md` → a11y skill = names သာ။ `spfx-enterprise-ux-hub` မှ **မစ**။ glassmorphism / Heft skills **မထည့်**။

**Bulk baseline (all pages / scaffold together):** `bulk-classic-to-spfx-baseline` **အရင်** + `docs/migration/PARITY.md`။ Wave 1–3 = wired / baseline သာ; Wave 4 parity slices အတွက် ဤနေရာ ပြန်။

Related skills (လိုအပ်သည်သာ load):

0. `bulk-classic-to-spfx-baseline` — **user က bulk / all WPs at once တောင်းမှ** (wired / baseline; parity PASS မကြေညာ)
1. `classic-visual-parity` — **UI migrate / visual tweak တိုင်း required** (classic CSS = SoT)
2. **[visual-typography.md](./references/visual-typography.md)** — **UI migrate တိုင်း required** — named-face `font-weight: 400`, menu link underline, typography self-check table (parity PASS မတိုင်မီ blocking)
3. `uikit-to-spfx-visual-parity` — **UI migrate မှာ required** — UIKit/Swiper gap/padding/margin/font-size/animation မကျန်စေ (`style.css` တစ်ခုတည်း မလုံလောက်)
4. `swiper-to-spfx-carousel` — slice မှာ `.winner-slider` / `.gallery-slider` ရှိရင် (wire init + scoped nav; vendor bundle မဟုတ်)
5. `spfx` — scaffold / toolchain (`react-design.md` Fluent v9 / host-theme ကို page look အတွက် **မလိုက်**)
6. `spfx-accessibility-and-content-quality` — keyboard/focus/names သာ; Fluent သို့ restyle မလုပ်
7. Project rules: `.cursor/rules/04-sharepoint-standards.mdc` · `17-classic-host-and-assets.mdc`

ဤ skill ၏ references (UI migrate မှာ typography ကျော်မရ):

- Segoe inherit / font-weight / link underline self-check → [visual-typography.md](./references/visual-typography.md) **(required)**
- Full-width / SPA / 450px clip → [host-modes.md](./references/host-modes.md)
- Site Pages chrome hide (user တောင်းမှသာ) → [site-chrome.md](./references/site-chrome.md)
- Images / CSP / remount → [siteassets-gotchas.md](./references/siteassets-gotchas.md)
- Inventory templates → [templates/](./templates/)
- Live inventory SoT → [docs/migration/PARITY.md](../../../docs/migration/PARITY.md) (`progress.md` နဲ့ sync)

glassmorphism look / Fluent density / theme slots ကို visual target **မသတ်**။ `classic-spfx-migration` အမည်ရှိ ဒုတိယ playbook **မload**။

## Workflow

### 0) Migration waves (overview)

| Wave | Skill | Status |
|------|-------|--------|
| PREP + bulk scaffold + baseline + host | `bulk-classic-to-spfx-baseline` | wired / baseline |
| Parity per slice | ဤဖိုင် + `classic-visual-parity` + `visual-typography` self-check | parity PASS |

User က bulk baseline အတိအလင်း တောင်းရင် Wave 0–3 တစ် PR OK။ **Parity PASS** = feature-by-feature။

### 1) Inventory classic surface

`DBS-FFW-classicsite/2025/` စစ်ပြီး [docs/migration/PARITY.md](../../../docs/migration/PARITY.md) sync:

- Live pages: `2025/index.aspx`, `2025/past-events.aspx`
- Admin / defer: `2025/back-door.aspx`
- Shared chrome: ASPX တိုင်း **inline** (`header.page-banner`) — `components/header.aspx` မရှိ
- Visual CSS: `2025/style.css` (compiled SoT), `2025/sass/` (`style.sass`, `_home`, `_fonts`), ASPX က သုံးသည့် UIKit + Swiper + hamburgers classes
- Scripts: `2025/public/js/controller/indexController.js`, `indexControllerPastEvent.js`, `winnerController.js`, `home.js`, `common.js`, `lib/common-lib.js`, `lib/lib.js`
- SP helpers: `2025/public/js/spbase/sprestlib-php.js`, `config.js`, `jquery.SPServices.min.js`
- Vendors: jQuery, UIKit (`public/css/vendor/uikit.min.css`, `public/js/vendor/uikit.min.js`), Swiper, FullCalendar (`index.global*.js`), lottie, anime, ical, papaparse, moment
- Data JSON: `events.json`, `events-current.json`, `post-event.json`, `participants.json`, `winnerlists.json`
- Cut / defer: `2024/index-old.aspx`, `2024/index-current.aspx`, `2023/clickr-test.aspx`, `*-bk.js` / `testController.js`; user မခေါ်လျှင် prior-year trees

Feature တိုင်း ခွဲ:

| Target | When |
|--------|------|
| **Web Part** | Page body / list UI / feature island |
| **Application Customizer** | Header/footer/chrome across pages |
| **Command Set / Field Customizer** | List toolbar သို့ field render |
| **Stay list/out-of-box** | custom code မလို |
| **Defer / cut** | Dead pages (`*-old.aspx`, test pages) သို့ unused scripts |

Classic master pages / `_layouts` system files **မပြင်**။ Repo ထဲရှိ Site Assets / Style Library ပုံစံ ဦးစားပေး။

### 2) Map data access

ဤ repo classic → SPFx:

| Classic | SPFx |
|---------|------|
| `loadJson('events.json')` / participants / winnerlists | SiteAssets / property-pane URL မှ fetch၊ သို့ small JSON bundle — source ပြောင်းမည်ဆို **အရင်မေး** |
| jQuery / SPServices / string REST | PnPjs (`@pnp/sp`) ဦးစားပေး၊ သို့ ရှိပြီး `SPHttpClient` |
| Controllers ထဲ hardcoded list URLs | Service module + property pane မှ list titles/IDs |
| Digest မသိသော writes | PnPjs က digest ကိုင်; raw REST = `X-RequestDigest` လို |
| CAML/SQL string concat | Typed filters / parameterized queries သာ |

AuthZ: list/item permissions စစ် — AuthN အောင်ရုံ မလုံလောက် (IDOR)။

XSS: sanitize မပါဘဲ CEWP/SEWP raw HTML ကို `dangerouslySetInnerHTML` ထဲ **မပို့**။

ဤ site lists/fields/i18n/PHP map = အောက် **This site appendix** — extra lists မတီထွင်။

### 3) Map UI + visual parity (blocking)

- Feature UI ကို `DBS-FFW-SPFX/src/webparts/...` React web part components ထဲ ပို့
- jQuery DOM hacks → React state; SharePoint chrome selectors မထိ
- List-driven UI = empty / loading / error states မဖြစ်မနေ (classic page မှာ ရှိရင် copy/spacing ကူး)
- **Visual SoT** = ထို slice ၏ year `style.css` (+ `sass/` + ASPX / သုံးသည့် UIKit + Swiper)။ SCSS မရေးမီ `classic-visual-parity` load; [visual-typography.md](./references/visual-typography.md) **self-check before parity PASS**
- `*.module.scss` ဖြင့် style။ Classic မှာ ယှဉ်နိုင်သော control ရှိမှ Fluent v8 — classic type/color/spacing ကို Fluent tokens **မအစား**
- Tailwind / SPA routers **မထည့်**
- မဖြစ်မနေ clone (ကျော်မရ): font-size, font-weight, font color, BG color, spacing, Gap, margin, padding, break line, letter spacing, line height, hover effect, animation effect, responsive `@media` (classic breakpoint px — Fluent-only 480/1024 မဟုတ်)
- ထို page သုံးသည့် classic breakpoint **တိုင်း** မှာ classic နဲ့ တူမှ slice migrated ဟု သတ်

### 4) Implement in SPFx target only

- ကုဒ်အသစ် = `DBS-FFW-SPFX/` — user က classic ပြင်ခိုင်းမှ parity testing အတွက် classic ပြင်
- Web part ပါးအောင်ထား; REST/Graph/JSON loaders = services
- Property pane = JSON/asset URLs, page URLs, feature flags
- Packaging: `config/package-solution.json` ပုံစံ ထိန်း; secrets/tenant IDs hard-code မလုပ်

### 5) Validate

Testing Gate အတိုင်း:

```bash
cd DBS-FFW-SPFX
gulp bundle
gulp test   # if present / meaningful
```

Manual smoke (workbench သို့ served page):

1. Script/web part console errors မရှိ load
2. ခွင့်ရှိ user အတွက် JSON / list read အောင်
3. Write path (ရှိရင်) အောင် + permission မရှိရင် သန့်စင် fail
4. Interactive controls မှာ keyboard focus + control names
5. **Visual vs classic (blocking):** font-size, font-weight, font color, BG color, spacing, Gap, margin, padding, break line, letter spacing, line height, hover effect, animation effect, responsive `@media` (classic widths တူ; stack/wrap/hide)

## Anti-patterns

- SPFx 1.20 / Fluent v8 မှာ Heft သို့ Fluent v9 အကြံပေး
- တစ် PR မှာ classic site အားလုံး **parity PASS** အတွက် ပြန်ရေး — scaffold/baseline သာ `bulk-classic-to-spfx-baseline`; parity = feature-by-feature
- Fluent/PnP က ဖုံးနိုင်သေး vendor minified bundles ကို SPFx ထဲ ကူး (deps အသစ် = အရင်မေး)
- `~/.cursor/skills` သို့ user-global skills မှာ packages install
- SPFx host lifecycle ကို လျစ်လျူရှုသော React (web) generic app patterns
- classic `style.css` အစား Fluent / theme-token / glassmorphism look ပို့
- Data အလုပ်လုပ်ရုံနဲ့ migrate ပြီးဟု ကြေညာ — type, color, spacing, hover, animation, `@media` classic နဲ့ ကွာနေသေးရင် မပြီး
- `2023/clickr-test.aspx` / `*-old.aspx` / `testController.js` ကို live features အဖြစ် ပို့
- User မတောင်းဘဲ year folder တိုင်း သီးခြား WP scaffold

## Output expectations

Migrate တောင်းရင် ပြန်ဖြေ:

1. Inventory summary (pages/scripts → target type) + CSS sources (`2025/style.css` / `sass/` / သုံးသည့် UIKit+Swiper)
2. ဤ slice အတွက် Selected Path (feature တစ်ခု)
3. Visual token table (`classic-visual-parity` mandatory rows)
4. `DBS-FFW-SPFX/` တွင် ထည့်/ပြင်မည့် ဖိုင်များ
5. Validation commands + manual smoke checklist (visual parity rows အပါ)

## This site appendix (DBS-FFW-classicsite)

Lists, fields, languages မတီထွင်။ Dead scripts / `config.js` debug dumps မပို့။

### Suggested web part map

| Classic surface | Script(s) | SPFx target |
|-----------------|-----------|-------------|
| `2025/index.aspx` | `indexController.js`, `winnerController.js`, `home.js`, `common.js` | Web Part **Ffw** (ရှိပြီး) |
| `2025/past-events.aspx` | `indexControllerPastEvent.js` | Web Part **PastEvents** / scaffold |
| `2025/back-door.aspx` | inline admin date override | Web Part **BackDoor** / defer |
| Inline `header.page-banner` | — | in-page ထား (Application Customizer = user တောင်းမှ နောက်မှ) |
| `2024/*`, `2023/*` | prior-year copies | cut / defer unless user names that year |
| `2024/index-old.aspx`, `2023/clickr-test.aspx` | — | cut |

### Data (property pane — defaults)

Primary data plane = **ASPX ဘေး year JSON** — InsightsBank-style SharePoint lists မဟုတ်။ List titles မတီထွင်။

| Use | Classic source |
|---|---|
| Events | `2025/events.json` / `events-current.json` |
| Post-event | `2025/post-event.json` |
| Participants | `2025/participants.json` |
| Winners | `2025/winnerlists.json` |

`sprLibPhp` (`public/js/spbase/sprestlib-php.js`) + `CommonLib` = optional SP list CRUD။ SPFx: PnPjs (`@pnp/sp`) typed object — **package မထည့်မီ မေး**။ PHP `db.php` **မခေါ်**။ `config.baseSpUrl` **မကူး** — `this.context.pageContext.web` သုံး။ Columns/list names မတီထွင်မီ slice script ဖတ်။

| Classic | SPFx |
|---|---|
| `commonLib.loadJson('events.json')` | `SPHttpClient` / SiteAssets သို့ property-pane URL မှ fetch |
| `sprLibPhp.items` / `itemsCAML` | PnP `items.filter(...).orderBy(...).top(n)` — `queryLimit: 5000` ကို default page size **မကူး** |
| `sprLibPhp.create` / `update` | `items.add({ ... })` / `items.getById(id).update({ ... })` |
| Current user helper | `pageContext.user` (extra fields လိုမှသာ profile) |

dbs-Insights-Bank / project-saral / change-management-learning field names **မယူဆ**။

### i18n

ဤ classic tree မှာ locale folder copies (`zh/` `sc/` `id/`) မရှိ။ Slice မှာ translations အစစ်ရှိမှသာ SPFx `loc/` ဖြင့် page copy ပို့။

### Do not port

- `2023/clickr-test.aspx`, `2024/index-old.aspx`, `testController.js`, `indexController-bk.js`
- `config.js` `console.log` / `userStaticDebug` / `userStaticProfile` dumps
- Hardcoded `/sites/ClassicSite/dbs-ffw` (`pageContext` သုံး)
- Vendor minified jQuery / UIKit / Swiper / FullCalendar / SPServices bundles as-is

`DBS-FFW-SPFX/` မှာ **Ffw** web part ရှိပြီး။ Upgrade မပြောမီ `package.json` pins အတည်ပြု။ Tenant သို့ `gulp serve` မတိုင်မီ `config/serve.json` `initialPage` = အစစ် workbench/site URL။

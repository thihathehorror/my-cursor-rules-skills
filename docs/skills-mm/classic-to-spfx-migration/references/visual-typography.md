# Visual typography — font-weight, links & host inherit (self-check)

**Companion to** `classic-visual-parity` — UI migrate / visual parity slice **တိုင်း** parity PASS မကြေညာမီ / typography fix မပိတ်မီ ဤ **mandatory self-check** မောင်း။

Visual PASS မတိုင်မီ Fluent tokens **မနိုင်**။

## Per-year font SoT (years မရော)

| Year folder | Named `@font-face` families | Classic font path |
|-------------|----------------------------|-------------------|
| `2023/` · `2024/` | `OpenSans-Bold`, `OpenSans-SemiBold`, `OpenSans-Medium`, `OpenSans-Regular`, `OpenSans-Light` | `{year}/public/fonts/opensans/` · `{year}/sass/_fonts.sass` |
| `2025/` | `OpenSans-Condensed-ExtraBold`, `OpenSans-Condensed-Bold`, `OpenSans-Condensed-Regular`, `OpenSans-Condensed-Light` | `2025/public/Fonts/opensans-condensed/` |

Visual SoT = **ထို slice ၏ year** `style.css` + `sass/_fonts.sass` — `2023/index.aspx` migrate သည့်အခါ 2025-only မဟုတ်။

## SPFx က classic ထက် “ပါး” မြင်ရသည့် အကြောင်း

1. **SP canvas inherit** — ancestors က **Segoe UI** အတင်း; classic named faces WP root ပေါ် မသက်ရောက်။
2. **Named face + missing weight** — classic = သီးခြား families (`OpenSans-Bold`)၊ `font-weight: 700` မဟုတ်။ Named Bold/SemiBold face သုံးသည့် selector တိုင်း SPFx မှာ **`font-weight: 400`** မထားရင် face က ပျော့/မှား။
3. **Root baseline ပျောက်** — `.ffw2023Root` (သို့ slice root) က `font-family: OpenSans-Regular` ထားသော် Bold faces သုံးသည့် headings/menu/links ပေါ် `font-weight: 400` ချန်။
4. **Font files မload** — `@font-face` ပျောက် သို့ classic bundled fonts နဲ့ path မှား။
5. **Selector က host ကို ရှုံး** — SharePoint / Fluent link rules က cloned classes override (အထူးသဖြင့် `<a>`)။
6. **Link underline (classic CSS မှာ မရှိ)** — host က `<a>` ပေါ် `text-decoration: underline` ထည့်; classic pill nav မှာ underline **မမြင်**။
7. **Remount** — canvas inject ပြီး computed weight drift။

## Named-face rule table (blocking)

Classic CSS မှာ `font-family: 'OpenSans-Bold'` (သို့ SemiBold / Condensed-Bold / စသည်) ရှိရင်:

| Classic | SPFx module.scss (selector တူ) |
|---------|----------------------------------|
| `font-family: 'OpenSans-Bold'` | Family တူ + **`font-weight: 400`** |
| `font-family: 'OpenSans-SemiBold'` | တူ + **`font-weight: 400`** |
| `font-family: 'OpenSans-Regular'` | တူ + WP root နှင့် `p` ပေါ် **`font-weight: 400`** (UIKit `html` default) — host က body copy ကို classic ထက် ပေါ့စေနိုင် |
| `h2` + Bold face | Classic မကြာခဏ `font-weight: 400` အတိအလင်း — ပို့ |
| Nav / menu `<a>` + Bold face | **`font-weight: 400`** + အောက် link rule |

Named Bold faces အစား `font-weight: 700` + Segoe **မအစား**။

## Link / menu rule (SharePoint host)

Classic desktop menu က base state မှာ `text-decoration: none` မကြာခဏ ချန် (host underline မရှိ)။ SPFx က nav/menu anchors ပေါ် **မဖြစ်မနေ** ထည့်:

```scss
.menu ul li a,
.page-menu li a {
  text-decoration: none;
  border-bottom: none;
}
/* + :hover, :focus, :visited as needed */
```

Menu/nav selectors သာ scope — `.sub-description a` နှင့် ရည်ရွယ် content links မှ underline **မဖြုတ်**။

## Mandatory self-check (agent — UI slice တိုင်း)

Parity PASS မတိုင်မီ၊ SCSS port ပြီး၊ သို့ user က font “ပါး” / “ထူ” / “light” ပြောရင်:

### Step 1 — Classic vs SPFx Grep

Slice အတွက် classic `{year}/style.css` မှာ ပို့ထားသော selectors ၏ `font-family`, `font-weight`, `text-decoration` Grep။ `*.module.scss` နဲ့ diff။ Classic `OpenSans-*Bold*` / `SemiBold` ရှိပြီး SPFx မှာ `font-weight: 400` မရှိရင် flag။

### Step 2 — Rule table သုံး

Named Bold/SemiBold selector တိုင်း ပြင်။ Classic မှာ underline မရှိရင် menu/link `text-decoration: none` ထည့်။

### Step 3 — Output checklist (chat သို့ handoff)

တိုတောင်း table **မကျော်ရ**:

| Selector / surface | Classic family | SPFx family | SPFx weight | Link deco | Status |
|--------------------|----------------|-------------|-------------|-----------|--------|
| e.g. `.menu ul li a` | OpenSans-Bold | OpenSans-Bold | 400 | none | OK / FIX |

ရှိရင် အမြဲထည့်: **root**, **`p` / card-wrap body copy**, **h2/main-title**, **page-banner date/description**, **post-event menu**, **mobile `.page-menu`**, Bold face သုံး **buttons/CTAs**။

### Step 3b — UIKit heading line-height (`uk-container` + `h2` သုံးရင် blocking)

Classic pages က page CSS မတိုင်မီ UIKit load။ Page `style.css` က `h2 { font-size: … }` ထားသော် **line-height မထား** မကြာခဏ — computed title line-height = UIKit:

| UIKit selector | `line-height` (ဤ repo vendor) |
|--------------|----------------------------------|
| `h2`, `.uk-h2` | **`1.3`** |
| `h1`, `.uk-h1` | `1.2` |
| `h3`, `.uk-h3` | `1.4` |

SPFx WP root က root/body clone ပေါ် `line-height: 28px` မကြာခဏ။ UIKit `h2 { line-height: 1.3 }` မပို့ရင် section titles (`.main-title`) က **1.3** အစား **28px** inherit → title box တင်းလွန်း၊ star pseudo-elements လွဲ၊ title→card gap မှား။

**Agent rule (user ထပ်မပြောစေနှင့်):**

1. ASPX က `uk-container` (သို့ UIKit layout) သုံးပြီး section titles = `h2` / `.main-title` → `*.module.scss` မှာ `h2` ပေါ် **`line-height: 1.3`** ပို့ (slice မှာ အခြား `h2` မရှိရင် `.main-title`)။
2. Classic `{year}/public/css/vendor/uikit.min.css` မှာ `h2{` / `line-height` Grep — မမှန်း။
3. Typography checklist မှာ row ထည့်:

| Selector | Classic/UIKit | SPFx | Status |
|----------|---------------|------|--------|
| `h2` / `.main-title` | `line-height: 1.3` | must match | OK / FIX |

`uikit-to-spfx-visual-parity` UIKit heading defaults table ကိုလည်း ကြည့်။

### Step 3c — Body copy / card-wrap `p` weight (`uk-container` သုံးရင် blocking)

Classic `style.css` က `p { font-family: OpenSans-Regular; font-size: 17px; line-height: 28px }` — `font-weight` အတိအလင်း **မရှိ** မကြာခဏ။ Live classic = UIKit `html { font-weight: 400 }` + Regular face → body copy = **normal weight**။

SPFx WP root က `font-family: OpenSans-Regular` ထားသော် root နှင့် `p` ပေါ် `font-weight: 400` **ချန်**နိုင်။ SharePoint canvas inherit က card copy (`section .card-wrap .card-content p`, `.main-sub-title`, highlights intro `p`) ကို classic ထက် **ပေါ့/ပါး** စေ (“classicsite ထူ · SPFx ပါး”)။

**Agent rule (user ထပ်မပြောစေနှင့်):**

1. Slice WP root (ဥပမာ `.ffw2023Root`) နှင့် classic body copy က `OpenSans-Regular` သုံးရင် **`:global p`** ပေါ် **`font-weight: 400`** ထား။
2. Typography checklist row:

| Selector | Classic/UIKit | SPFx | Status |
|----------|---------------|------|--------|
| WP root + `p` / `.card-wrap p` | `font-weight: 400` + OpenSans-Regular | must match | OK / FIX |

3. Weight ပြင်ပြီး ပေါ့နေသေးရင်: Network tab — OpenSans `.woff2` → 200 (font မload = Segoe fallback)။

### Step 4 — Manual QA (serve ပြီး)

DevTools computed — SPFx vs classic breakpoint တူ:

- [ ] `font-family` = classic named face (Segoe primary မဟုတ်)
- [ ] Named Bold/SemiBold selectors ပေါ် `font-weight` = `400`
- [ ] Menu/nav links: host underline မရှိ
- [ ] Network: font `.woff2` / `.woff` → 200

## Win order (ပြင်)

1. Classic selectors inventory (`classic-visual-parity`) — ကျော်မရ
2. px/hex/family တိကျ `*.module.scss` ထဲ ပို့
3. Bold/SemiBold selector တိုင်း **named-face rule table** သုံး
4. Classic မှာ underline မရှိရင် menu/nav `text-decoration: none`
5. WP root: classic `font-family` stack + Bold headings ပေါ့နေသေးရင် `font-weight: 400` baseline
6. Classic fonts folder မှ year-correct `@font-face` ပြန်သုံး (sppkg ထဲ bundle)
7. `!important` မထည့်မီ တိုက်နေသော `style={{}}` / theme slots ပြင်

## Repo examples (Ffw2023 — ပုံစံကူး)

| Issue | Classic | SPFx fix |
|-------|---------|----------|
| Menu ပေါ့လွန်း | `.menu ul li a { font-family: OpenSans-Bold }` | + `font-weight: 400` |
| Menu underline | visually underline မရှိ | menu `<a>` ပေါ် + `text-decoration: none; border-bottom: none` |
| Date bold ပျော့ | `.date { OpenSans-Bold }` | + `font-weight: 400` |
| h2 ပျော့ | `h2 { OpenSans-Bold; font-weight: 400 }` | နှစ်ခုလုံး ပို့ |
| Card copy ပေါ့ | `#post-about` / `.card-wrap` ထဲ `p` — Regular, implicit 400 | root + `p` ပေါ် + `font-weight: 400` |

Files: `Ffw2023.module.scss` · `PageBanner.tsx` menu markup.

## Reject

- Typography self-check table မရှိဘဲ parity PASS ကြေညာ
- “CSS copied from classic” ဟုဆိုသော် named Bold selectors မှာ `font-weight: 400` မရှိ
- PASS မတိုင်မီ Fluent tokens / Segoe ကို primary stack
- Content underlines ချိုးသော global `a { text-decoration: none }`
- Named OpenSans-Bold face အစား `font-weight: 700`

---
name: swiper-to-spfx-carousel
description: >-
  [MM] Classic Swiper carousels (winner-slider, gallery-slider) ကို SPFx React 17
  ထဲ classic config parity, scoped navigation, module.scss nav styles ဖြင့် wire —
  vendor CSS bundles မဟုတ်။ Trigger: Swiper, carousel, slider, gallery slider,
  winner-slider, swiper-button, slidesPerView, SPFx မှာ gallery/winner swipe မရ။
source: _cursor/skills/swiper-to-spfx-carousel/SKILL.md
---

# Swiper → SPFx carousel (DBS-FFW)

Classic pages = **Swiper bundle** (`swiper-bundle.min.js` + CSS) + `public/js/common.js` init။ SPFx က vendor bundle **မပို့** — user-approved `swiper` npm + year `style.css` မှ nav/slide CSS ကို `*.module.scss` ထဲ clone။

Nav button / slide visuals အတွက် `classic-visual-parity` တွဲ load။ Gallery grid spacing drift ရင် `uikit-to-spfx-visual-parity`။

| Role | Path |
|------|------|
| Init configs | `DBS-FFW-classicsite/{year}/public/js/common.js` |
| Nav / slide CSS | `DBS-FFW-classicsite/{year}/style.css` (+ `sass/_home.sass`) |
| Markup | slice ASPX — `.winner-slider`, `.gallery-wrap.gallery-slider` |
| Vendor (reference only) | `{year}/public/css/vendor/swiper-bundle.min.css` — SPFx ထဲ **မimport** |
| Target | `DBS-FFW-SPFX/src/webparts/**` |

Classic configs (years အားလုံး — ကူးမီ slice အတည်ပြု): [classic-configs.md](./references/classic-configs.md)။

## When

- SPFx မှာ gallery သို့ game-show winner section slides static
- User က Swiper, carousel, slider, `swiper-button`, `slidesPerView` ပြော
- `.winner-slider` / `.gallery-slider` ရှိသော sections ၏ Wave 4 parity

## Reject

- sppkg ထဲ `swiper-bundle.min.js` / `swiper-bundle.min.css`
- `import 'swiper/css/bundle'` (module CSS အားလုံး — bloat + classic overrides နဲ့ တိုက်)
- စာမျက်နှာမှာ sliders အများရှိရင် global `navigation.nextEl: '.swiper-button-next'` (classic pattern — SPFx မှာ **instance တိုင်း scope**)
- Visual clone slices အတွက် Fluent carousel / `@fluentui/react` အစား
- User approval မရှိ `npm i swiper` (`00` Dependencies)
- Slides swipe မရ သို့ breakpoints classic နဲ့ ကွာနေရင် parity PASS

## Workflow

### 1) Inventory slice

ASPX + `common.js` မှ:

- ဘယ် sliders? (`.winner-slider`, `.gallery-slider`, `.mySwiper1`, …)
- Selector တိုင်း init options (navigation, `slidesPerView`, `spaceBetween`, `breakpoints`, `loop`, …)
- Markup မှာ nav buttons ရှိသလား? (container ထဲ `swiper-button-prev` / `swiper-button-next`)
- Dynamic slide injection? (ဥပမာ `testController.js` က `.winner-slider .swiper-wrapper` mutate — React state မှာ ပြန်ထုတ်)

SPFx stubs ယနေ့ (အတည်ပြု): `GallerySection.tsx`, `GameShowWinnersSection.tsx` — markup သာ၊ **init မရှိ**, **nav buttons မရှိ**။

### 2) Dependency (ask-first)

ခွင့်ရရင်:

```bash
cd DBS-FFW-SPFX
npm i swiper
```

- Current stable `swiper` (12.x) ဦးစားပေး — known vulnerable 8.x transitive pins ရှောင်
- React 17 + SPFx 1.20: `swiper/react` (`Swiper`, `SwiperSlide`) — user မတောင်းလျှင် Swiper Element web components မဟုတ်
- လိုအပ်သော module CSS သာ import — ဥပမာ `swiper/css` + `swiper/css/navigation` — bundle မဟုတ်

### 3) Shared component pattern

WP တစ်ခုမှာ reusable wrapper တစ်ခု (WPs အများလိုရင် `src/shared/`):

```tsx
import { Navigation } from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/react';
import type { SwiperOptions } from 'swiper/types';
import 'swiper/css';
import 'swiper/css/navigation';

// modules={[Navigation]} navigation onSwiper destroy on unmount (useEffect cleanup)
```

**SPFx / bundle size** (MS Learn dynamic loading): section mount မှသာ optional `import()` — heavy vendors ပုံစံတူ; baseline ကို ဤအချက်ကြောင့် မပိတ်။

**Scoped navigation** (စာမျက်နှာမှာ sliders ၂+ ရှိရင် required):

- `swiper-button-prev` / `swiper-button-next` ကို `Swiper` **အတွင်း** ထား (React က elements ဖန်)
- သို့ `navigation={{ nextEl: nextRef.current, prevEl: prevRef.current }}` — ထို instance ၏ buttons refs
- Classic global selectors ကို instances ကြား **မပြန်သုံး**

**Lifecycle:**

- `onSwiper` မှာ instance သိမ်း; `useEffect` return → unmount မှာ `swiper.destroy(true, true)`
- Slide list length ပြောင်းရင် re-init (country ပြောင်းပြီး winner slides ပြန်ဖြည့်)

**A11y** (swiper docs + enterprise):

- ခွင့်ရရင် `modules={[Navigation, A11y]}` — keyboard + slide labels
- Informative slide images: `<img>` `alt`; background-only slides: slide `aria-label` သို့ purely visual tiles `aria-hidden`
- `prefers-reduced-motion`: autoplay မလုပ်; classic မှာ ဤ sliders autoplay မရှိ

### 4) Port classic options

| Selector | Classic (`common.js`) |
|----------|------------------------|
| `.winner-slider` | `navigation` သာ (default `slidesPerView: 1`) |
| `.gallery-slider` | `slidesPerView: 1`, `spaceBetween: 10`, `breakpoints: { 640: { slidesPerView: 2 }, 768: { slidesPerView: 3 } }` |

`Swiper` props / `breakpoints` object — numeric keys classic တူ (640, 768), Fluent 480 မဟုတ်။

### 5) CSS (visual parity — vendor ဖိုင်မဟုတ်)

Year `style.css` မှ web part module ထဲ clone (`Ffw2023.module.scss` မှာ တစ်စိတ်တစ်ပိုင်း ရှိပြီး):

- `.winner-slider .team-photo` / `.gallery-slider` heights (500px winner, 220px gallery tile)
- Nav: `background-color`, hover flip to white/`#707070`, `padding: 32px`, `:after { font-size: 35px }`, `left: 0` / `right: 0`
- `.gallery-wrap .swiper-slide { overflow: hidden }`, gallery hover `transform: scale(1.03)`

**Mobile fallback:** အချို့ modules မှာ `.swiper-wrapper { display:flex; overflow-x:auto; scroll-snap-type:x mandatory }` `@media` ရှိ — classic year CSS မှာ ရှိရင် ထား; JS load ရင် Swiper init ဆက်မောင်း။

Swiper default arrow colors **မယုံ** — classic က page CSS မှာ override။

### 6) Markup parity

Ported CSS သက်ရောက်အောင် classic structure တူ:

```html
<div class="swiper winner-slider">
  <div class="swiper-wrapper">…</div>
  <div class="swiper-button-prev"></div>
  <div class="swiper-button-next"></div>
</div>
```

Gallery: `swiper gallery-wrap gallery-slider` (classes နှစ်ခုလုံး)။

### 7) Validation (slider sections parity PASS မတိုင်မီ blocking)

Classic နဲ့ breakpoint တူ manual smoke:

- [ ] Prev/next မြင်ရ + styled (dark overlay → white hover)
- [ ] Winner: view တစ်ခုမှာ slide တစ်ခု; swipe / arrows အလုပ်လုပ်
- [ ] Gallery: mobile / 640+ / 768+ မှာ 1 / 2 / 3 columns + ~10px gap
- [ ] Horizontal page jitter မရှိ; WP unmount မှာ destroy သန့် (duplicate listeners မရှိ)
- [ ] Dep ထည့်ပြီး `gulp bundle` အောင်

## Cross-skill

| Need | Skill |
|------|--------|
| Nav colors, hover, slide heights | `classic-visual-parity` |
| Gallery grid edge alignment | `uikit-to-spfx-visual-parity` |
| Bundle / dynamic import | `spfx-enterprise-code-and-performance` |
| Image paths | `classic-to-spfx-migration` + asset map pattern |

## Anti-patterns

- Swiper init မရှိ markup-only `swiper-slide` divs (လက်ရှိ Ffw2023 state)
- CSS က `.swiper-button-prev` ပစ်မှတ်ထားသော် JSX မှာ nav buttons ပျောက်
- ASPX ထဲ `<script>new Swiper(...)</script>` ကို SPFx ထဲ ကူး
- Slides အတွက် jQuery post-init DOM hacks — React props/state သုံး

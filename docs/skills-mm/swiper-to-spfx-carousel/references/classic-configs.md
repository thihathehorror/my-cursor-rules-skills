# Classic Swiper configs (DBS-FFW)

Source: `public/js/common.js` (2023 / 2024 / 2025 — main sliders တူ)။

## `.winner-slider`

```js
new Swiper(".winner-slider", {
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});
```

- Default `slidesPerView: 1`
- `spaceBetween` မရှိ၊ `loop` မရှိ၊ autoplay မရှိ
- Markup: `.swiper-slide` > `.team-photo` (background-image) ထဲ team photos
- Dynamic slides: အချို့ controllers က country ပြောင်းရင် `.winner-slider .swiper-wrapper` children အစားထိုး — SPFx က slides ပြန် render + `swiper.update()` သို့ remount

## `.gallery-slider`

```js
new Swiper(".gallery-slider", {
  slidesPerView: 1,
  spaceBetween: 10,
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    640: { slidesPerView: 2 },
    768: { slidesPerView: 3 },
  },
});
```

- Container classes: `swiper gallery-wrap gallery-slider`
- Slide content: `background-image` ပါ `.gallery` div (CSS မှာ height ~220px)
- Gallery hover: `transform: scale(1.03)` — page CSS ထဲ၊ Swiper မဟုတ်

## `.mySwiper1` (inline ASPX — winner/gallery မဟုတ်)

အချို့ pages က ASPX foot script မှာ သီးခြား init — slice တိုင်း inventory; past-events / team carousel သာ မကြာခဏ။

## React `Swiper` prop mapping

| Classic | `swiper/react` |
|---------|----------------|
| `slidesPerView: 1` | `slidesPerView={1}` |
| `spaceBetween: 10` | `spaceBetween={10}` |
| `breakpoints` | `Swiper` ပေါ် object တူ |
| `navigation` | `modules={[Navigation]}` + `navigation` prop သို့ default generated buttons |
| `modules` | `swiper/modules` မှ import |

## SPFx scoped navigation ဥပမာ

စာမျက်နှာမှာ sliders နှစ်ခုရှိရင် classic global selectors **မသုံး**:

```tsx
<Swiper modules={[Navigation]} navigation className="swiper winner-slider">
  {slides.map(...)}
  {/* React Swiper creates prev/next when navigation=true */}
</Swiper>
```

သို့ buttons nest + refs bind — instance တိုင်း သီးခြား။

## ပို့ရမည့် CSS selectors (year `style.css` စစ်)

- `.winner-slider .team-photo`, `.gallery-slider .team-photo` — `height: 500px`, cover center
- `.winner-slider .swiper-button-prev`, `.gallery-slider .swiper-button-prev` — `left: 0`
- `.winner-slider .swiper-button-next`, `.gallery-slider .swiper-button-next` — `right: 0`
- Shared nav — `background-color: rgba(0,0,0,0.5)`, `color: #fff`, `padding: 32px`
- Hover — `background: #fff`, `color: #707070`, `transition: .3s ease-out`
- `:after` — `font-size: 35px`
- `.gallery-wrap .swiper-slide` — `overflow: hidden`
- Mobile `@media` — `.swiper-wrapper` ပေါ် optional `scroll-snap` flex fallback (`Ffw2023.module.scss` ကြည့်)

## Vendor version မှတ်ချက်

Classic = `swiper-bundle.min.js` (bundled modules)။ SPFx က `Navigation` module + minimal CSS သာ import။ **Behavior** ကိုက် — vendor file shape မဟုတ်။

## Security / deps

- Vulnerable Swiper 8.x **မcommit** — dep ထည့်ရင် user-approved `swiper@12+`
- Sanitize မပါ user-controlled slide HTML မသုံး — winner prizes JSON HTML ရှိနိုင်; ရှိပြီး `dangerouslySetInnerHTML` paths ကို slide images နဲ့ မရော

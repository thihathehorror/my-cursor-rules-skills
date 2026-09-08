# Site assets (DBS-FFW)

> Docs ဘာသာပြန် — live fill-in = `docs/migration/SITEASSETS.md`။ Tree / filenames = English။

Hardcoded site path မရှိ။ Classic vs SPFx trees ကွာ။ Visual SoT year = **2025**။

## Classic

```
DBS-FFW-classicsite/
  2025/                  current live year (SoT)
    index.aspx
    past-events.aspx
    back-door.aspx
    style.css
    events.json / events-current.json / post-event.json
    participants.json / winnerlists.json
    sass/                style.sass, _home, _fonts
    public/
      css/vendor/        uikit.min.css, swiper*.css
      css/               hamburgers.min.css
      js/controller/     indexController.js, indexControllerPastEvent.js, winnerController.js
      js/lib/            common-lib.js, lib.js
      js/spbase/         sprestlib-php.js, config.js, jquery.SPServices.min.js
      js/vendor/         uikit, swiper, jquery, fullcalendar, lottie, anime, ical, papaparse, moment
      Fonts/opensans-condensed/
      images/
  2024/ · 2023/          prior-year copies — user မခေါ်လျှင် မပြောင်း
```

## SPFx

- Page UI → `*.module.scss` (classic values clone; `uikit.min.css` သို့ Swiper CSS အပြည့် **မထည့်**)
- Small thumbs → ရှိပြီး bundled ဖြစ်ရင် WP `assets/`
- Optional SiteAssets: `pageContext` + `assetsBaseUrl` မှ `{web.serverRelativeUrl}/SiteAssets/...`

အသေးစိတ်: `references/host-modes.md` · `references/siteassets-gotchas.md`။

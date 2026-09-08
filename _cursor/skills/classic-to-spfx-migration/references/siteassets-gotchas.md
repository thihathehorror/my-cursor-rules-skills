# SiteAssets + runtime gotchas

Classic assets = `DBS-FFW-classicsite/2025/` — compiled CSS = `style.css`, vendor/fonts = `public/`, app scripts = `public/js/`။ SPFx က page CSS/JS/thumbs ကို web part ထဲ **bundle** နိုင်; rebuild မလိုဘဲ ပြင်ရမည့် large vendor / fonts / images = SiteAssets။

## Typical split (ဤ repo)

| Where | What |
|-------|------|
| sppkg / WP `assets/` | Page SCSS, React, ရှိပြီး bundled small thumbs |
| Property pane URLs | Optional large images / downloads — slice မလိုလျှင် **မbundle** |
| SiteAssets (optional) | Shared images, မbundle သေး UIKit/fonts; `pageContext` မှ `{web.serverRelativeUrl}/SiteAssets/...` သာ |

## Resolvers

- Base = `this.context.pageContext.web.serverRelativeUrl` — hardcoded `/sites/…` မရှိ
- SiteAssets (သို့ CDN) သုံးရင် `assetsBaseUrl` property pane
- Classic `config.baseSpUrl` (`/sites/ClassicSite/dbs-ffw`) **မကူး**

## CSP

- Classic JS ကို `blob:` + `createObjectURL` ဖြင့် **မboot** — SP `script-src` ပိတ်
- WP ထဲ webpack chunks / React ဦးစားပေး

## Remount / UIKit

Slice က WP ထဲ UIKit ဆက်သုံးရင် (React က ဖုံးနိုင်ရင် ရှောင်):

- DOM inject ပြီး hover / modal / offcanvas ပြန်ချိတ်; unmount မှာ listeners dispose
- UIKit `uk-*` visual values → `uikit-to-spfx-visual-parity` (`uikit.min.css` အပြည့် **မload**)

## Flash / blank

| Symptom | Fix |
|---------|-----|
| Flash then empty | Host height/overflow unlock + minHeight sync (`host-modes.md`) |
| ~450px မှာ content clip | `.ms-SPLegacyFabricBlock` overflow unlock |
| Mobile offcanvas သေ | Overflow/transform parents unlock; လိုရင် `body` သို့ portal |

## Smoke (အနည်းဆုံး)

- [ ] Images resolve (bundled, SiteAssets, သို့ property-pane URL)
- [ ] Blob CSP errors မရှိ
- [ ] Full-width section: 450px clip မရှိ
- [ ] Navigation ပြီး hover / modal ဆက်အလုပ်လုပ်

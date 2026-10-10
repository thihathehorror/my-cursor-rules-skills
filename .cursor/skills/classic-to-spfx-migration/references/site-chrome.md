# Site Pages chrome On/Off

ဤ PJ ၏ classic chrome = **`.aspx` တိုင်း inline** (header/footer ASPX သီးခြားမရှိ၊ `ui-loader.js` မရှိ)။ User မတောင်းလျှင် dbs-mtj PortalShell Application Customizer / `__OMT_*` globals **မကူး**။

Full-bleed သို့ SPA web part ပတ်လည် SharePoint chrome (header/footer/banner) ဖျောက်ရန် **modern host page** လိုမှသာ Site Pages Yes/No columns သုံး။

## Columns (Site Pages library) — user တောင်းမှသာ

| Display | Internal name (exact) | Default |
|---------|----------------------|---------|
| Show Header | `ShowHeader` | Yes |
| Show Footer | `ShowFooter` | Yes |
| Show Banner | `ShowBanner` | Yes |

- **Yes/No** အဖြစ် ထည့်။ Internal names အတည်ပြု (spaces မရှိ)။
- ထို surface မရှိရင် column ချန်။

## Semantics (fail-open)

| Value | Effect |
|-------|--------|
| Yes / blank / column missing / REST fail / timeout | ထို chrome **Show** |
| Explicit `false` / No သာ | **Hide** |

## Runtime (columns ရှိရင်)

1. Web part `onInit` → **`SPHttpClient`** ဖြင့် fetch (host Site Pages item)
2. Paint မတိုင်မီ hide/show။ Seed/REST ပျောက်ရင် fail-open
3. Columns = **host Site Page** item — in-WP routes မဟုတ်

User အတိအလင်း မတောင်းဘဲ list columns **မတီထွင်**။

## Smoke (columns ရှိပြီးမှသာ)

1. Defaults Yes → SP chrome မြင်ရ
2. `ShowHeader=No` → suite/page header ဒီဇိုင်းအတိုင်း ပုန်း
3. Column ပျောက် → chrome ဆက်မြင် (fail-open)

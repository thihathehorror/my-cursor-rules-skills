# Host modes — Full Width WP + Single-page app

ဤ repo = **classic page တစ်ခု = web part တစ်ခု** (Home, Step1, Reporting, …) — `pageKey` ပါ hub တစ်ခုမဟုတ်။ Classic page width ကိုက်ရမည့် WP တိုင်း host contract တူသုံး။

## Manifest (Step1 / Reporting / Home shipped အတိုင်း)

```json
"supportedHosts": ["SharePointWebPart", "SharePointFullPage"],
"supportsFullBleed": true
```

Clone WP မှ `supportsFullBleed` **မဖြုတ်**။ Workbench-only width = Visual PASS မဟုတ်။

## A — Single Web Part (Site Page)

1. Editor: part ကို **full-width** section ထဲ ထား (fullBleed-capable canvas)။
2. Runtime: canvas **ancestors** unlock:
   - **width** (canvas max-width / padding)
   - **height + overflow** (`.ms-SPLegacyFabricBlock` ~450px clip → flash-then-blank / clipped scroll)
3. `ResizeObserver` → content root height ကို host `minHeight` sync။ Unmount မှာ dispose။
4. Unlock က ancestors **မတွေ့မှသာ** CSS `width:100%; max-width:none` — unlock ပေါ် `100vw` ±50% breakout **မထပ်**။
5. Dispose: unlock attributes / inline overrides ရှင်း။

## B — Single-page app (Full Page)

1. Site page → **Single-page app** → route တိုင်း WP တစ်ခု (ဤ repo: WPs သီးခြား၊ router တစ်ခုမဟုတ်)။
2. Form factor FullPage = `SharePointFullPage`။
3. Default **parent unlock မလုပ်**။ Deploy ပြီး canvas clip နေသေးရင် unlock = fallback။

## Do / Don't

| Do | Don't |
|----|-------|
| Modern page မှာ full-width **section** smoke | `supportsFullBleed` CSS တစ်ခုတည်း canvas ပြင်မည်ဟု ယူဆ |
| Height/overflow unlock — width သာ မဟုတ် | FabricBlock 450px lock ထား |
| WP full-width **နှင့်** SPA (နှစ်ခုလုံးသုံးရင်) smoke | Workbench-only စစ်ပြီး full width ကြေညာ |

## Smoke

- Full-width section → content classic width တူ; ရှည် pages scroll; 450px clip မရှိ
- SPA (သုံးရင်) → product က hide လိုရင် double chrome မရှိ (`references/site-chrome.md`)
- `.sppkg` update ပြီး hard refresh

# Classic ↔ SPFx parity inventory (DBS-FFW)

> Docs ဘာသာပြန် — live SoT = `docs/migration/PARITY.md`။ Copy သုံးရင် Status tokens အင်္ဂလိပ်မူ ထား။

Site URL: deploy မှာ အတည်ပြု (hardcoded tenant/site path မရှိ)။ Visual SoT = classic `.aspx` + `DBS-FFW-classicsite/2025/style.css`။ Status = **parity PASS** မှသာ cutover။

## Canonical

| Host | Notes |
|------|--------|
| Classic `DBS-FFW-classicsite/` | year folders `2023/` `2024/` `2025/`; live SoT = `2025/` |
| SPFx `DBS-FFW-SPFX/` | live page တစ်ခု = WP တစ်ခု; **Ffw** scaffold ပြီး |

## Pages

| Classic | SPFx target | Status |
|---------|-------------|--------|
| `2025/index.aspx` | Ffw | todo |
| `2025/past-events.aspx` | PastEvents | todo |
| `2025/back-door.aspx` | BackDoor | defer |
| `2024/*` / `2023/*` | — | cut / defer unless user names that year |
| `2024/index-old.aspx` / `2023/clickr-test.aspx` | — | cut |

## Chrome

Classic chrome = ASPX တိုင်း **inline** `header.page-banner`။ Modern SP chrome ဖျောက်ရန် user တောင်းမှသာ Site Pages `ShowHeader` / `ShowFooter` / `ShowBanner` — `references/site-chrome.md`။

## Immutable contracts

- Classic class semantics + visual token rows (`classic-visual-parity`)
- Hardcoded site path မရှိ
- Classic CSS သုံး OpenSans-Condensed weights SPFx မှာ load ရမည်
- Data = year JSON (`events.json`, `participants.json`, `winnerlists.json`) via `SPHttpClient` / fetch; `@pnp/sp` ask-first
- Slice script က သက်သေမပြလျှင် SharePoint lists မတီထွင်

## Visual PASS checklist

font-size · **font-weight** · font color · BG · spacing · gap · margin · padding · break-line · letter-spacing · line-height · hover · animation · `@media` (classic px)

| Status | Meaning |
|--------|---------|
| inventory only | Docs သာ |
| wired / baseline | Func OK; visual FAIL နိုင် |
| parity PASS | Func + Visual |

Live status = `docs/migration/PARITY.md` (repo SoT) — `progress.md` နဲ့ sync။ ဤဖိုင် = skill template copy။

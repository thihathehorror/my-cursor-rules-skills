---
name: bulk-classic-to-spfx-baseline
description: >-
  [MM] Classic ASPX စာမျက်နှာများစွာကို SPFx web parts သီးခြား scaffold —
  wired/baseline သာ၊ parity နောက်မှ။ Trigger: all pages at once, bulk scaffold,
  baseline wave, visual PASS မကြေညာဘဲ WPs တွဲ wire။ DBS-FFW သာ; hub pageKey router မသုံး။
source: _cursor/skills/bulk-classic-to-spfx-baseline/SKILL.md
---

# Bulk Classic → SPFx Baseline (DBS-FFW)

Clickr `mk` playbook မှ **wire-first** wave — hub router / mk chat/behavior rules **မပါ**။

## When to load

| Load | Skip |
|------|------|
| User က bulk / all pages / all web parts at once / baseline wave / scaffold together | Single-slice visual parity tweak သာ |
| Cut WPs (PastEvents, BackDoor) ကို stubs အဖြစ် re-scaffold | Hub `pageKey` router (rule 17 ငြင်း) |
| Live routes အားလုံးအတွက် inventory + manifest + serve.json | ထို wave ထဲ parity PASS ကြေညာ |

**Load order:** `docs/migration/PARITY.md` → ဤ skill → `classic-to-spfx-migration` (appendix) → Yeoman patterns အတွက် `spfx`/`create.md` → Wave 3 မတိုင်မီ parity skills **မလို**။

## Hard rejects (main migration နဲ့တူ)

- Hub web part + `pageKey` router (classic page တစ်ခု = WP တစ်ခုသာ)
- SPFx 1.20 / Fluent v8 မှာ Heft / Fluent v9
- User approval မရှိ npm packages အသစ်
- Baseline wave အတွင်း **parity PASS** သို့ Visual PASS ကြေညာ
- `2023/clickr-test.aspx` / `*-old.aspx` / prior-year trees — user မခေါ်လျှင် မပို့
- Hardcoded tenant/site URLs
- sppkg ထဲ vendor minified jQuery/UIKit/Swiper/FullCalendar bundles အပြည့်ထည့်

## Wave order (ကျော်မရ)

| Wave | Goal | Status allowed |
|------|------|----------------|
| **0 PREP** | `docs/migration/PARITY.md` + `progress.md` sync | inventory only |
| **1 SCAFFOLD** | PARITY table ရှိ **live** route တိုင်း Yeoman-style WP folders | inventory → wired |
| **2 BASELINE** | Thin React shell + shared classic SCSS hook + manifest `supportsFullBleed` + `config.json` + `serve.json` | **wired / baseline** |
| **3 HOST** | Canvas clip ရင် per-WP full-width unlock — [host-modes.md](../classic-to-spfx-migration/references/host-modes.md) | wired / baseline |
| **4 PARITY** | **Separate slices** — `classic-visual-parity` + [visual-typography.md](../classic-to-spfx-migration/references/visual-typography.md) self-check + `uikit-to-spfx-visual-parity` | parity PASS |

User က bulk baseline အတိအလင်း တောင်းရင် Wave 1–3 **တစ် PR** ဖြစ်နိုင်။ Wave 4 = **feature-by-feature**။

## Architecture (ဤ repo)

```
Classic ASPX (one page)  →  SPFx Web Part (one WP)  →  optional SPA host per page
NOT: one hub WP + pageKey router
```

| Classic | SPFx target | Notes |
|---------|-------------|-------|
| `2025/index.aspx` | **Ffw** | ရှိပြီး |
| `2025/past-events.aspx` | **PastEvents** | scope ထဲရှိရင် scaffold |
| `2025/back-door.aspx` | **BackDoor** | user တောင်းမှ; မဟုတ်ရင် defer |

## Wave 1 — Scaffold checklist (WP တိုင်း)

`DBS-FFW-SPFX/src/webparts/<Name>/` အောက်:

- `<Name>WebPart.ts` + `.manifest.json` (`supportsFullBleed: true`, `SharePointWebPart` + `SharePointFullPage`)
- `components/<Name>.tsx` + `I<Name>Props.ts`
- `components/<Name>.module.scss` (baseline မှာ host isolation သာ)
- `loc/en-us.js` + `mystrings.d.ts`
- `config/config.json` bundles မှာ register
- `config/serve.json` entry — tenant page + `debug=true&noredir=true`

ရှိပြီး **Ffw** web part ပုံစံ ကူး — architecture အသစ် မတီထွင်။

## Wave 2 — Baseline content (minimal)

ပန်းတိုင်: page load + console errors မရှိ; classic **look** FAIL နိုင်။

1. Classic page root နဲ့ ကိုက်သော root wrapper class (ဥပမာ `2025/index.aspx` FFW home root)
2. ရှိပြီး `src/shared/styles/classicGlobal.scss` (သို့ ညီမျှ) မှ shared classic tokens import — `uikit.min.css` အပြည့် **မကူး**
3. Main regions placeholder (header optional; body sections stub)
4. Data: read-only smoke သို့ static placeholder — full JSON/PnP port = Wave 4
5. Property pane: `classic-to-spfx-migration` appendix defaults (`events.json` စသည်)

## Wave 3 — Host

Classic full width လိုသော WP တိုင်း:

- Modern page မှာ full-width section
- Ancestor unlock (width + height/overflow) — [host-modes.md](../classic-to-spfx-migration/references/host-modes.md)
- Host mode ကို `docs/migration/SITEASSETS.md` မှာ မှတ်

## Validation (baseline wave)

```bash
cd DBS-FFW-SPFX
gulp bundle
gulp test   # if meaningful
```

Smoke (scope ထဲ WP အားလုံး):

1. Workbench သို့ served tenant page မှာ WP တိုင်း load — console errors မရှိ
2. `supportsFullBleed` manifest ရှိ
3. Root layout မြင်ရ (stub OK)
4. Visual parity checklist ကြောင့် **မပိတ်**

`docs/migration/PARITY.md` Status column ပြင်ပြီး `progress.md` sync။

## Output expectations (bulk wave)

1. PARITY table diff (before → after Status)
2. Scaffold ထားသော WPs vs ရှိပြီးသား
3. `DBS-FFW-SPFX/` တွင် ထည့်သည့် ဖိုင်များ
4. `gulp bundle` ရလဒ်
5. ကြေညာချက်: **wired / baseline only — parity PASS deferred to Wave 4 slices**

## Anti-patterns

- ဤ skill ဖြင့် Wave 4 ကို အမြဲကျော်
- စာမျက်နှာအားလုံး route လုပ်သော mega React ဖိုင်တစ်ခု (hub pattern)
- Classic SCSS hook အစား Fluent redesign
- Baseline ပြီးရုံနဲ့ migration complete ကြေညာ
- Agent turn တစ်ခုမှာ bulk parity PASS (context + quality bar — slices ခွဲ)

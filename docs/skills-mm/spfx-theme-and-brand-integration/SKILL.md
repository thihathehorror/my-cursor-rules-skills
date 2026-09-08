---
name: spfx-theme-and-brand-integration
description: "[MM] SPFx enterprise customizations အတွက် theme token, semantic slot, brand font guidance"
source: _cursor/skills/spfx-theme-and-brand-integration/SKILL.md
---

# SPFx Theme and Brand Integration

## Use for

1. Semantic slots နှင့် theme-aware styling သုံး။
2. Brand Center fonts ကို ဘေးကင်းစွာ ပေါင်း။
3. Light/dark/high-contrast compatibility။

## Do not use for

1. Hard-coded theme color overrides — **ခြွင်းချက်** ဤ repo classic visual clone (`classic-visual-parity`): `DBS-FFW-classicsite/2025/style.css` မှ classic hex/px **လိုအပ်**။
2. Tenant strategy ကျော်သော ad-hoc font imports — clone အတွက် classic/SPFx assets ထဲ ရှိပြီး OpenSans-Condensed faces = in-scope။

## Trigger conditions

1. Theme-related UI သို့ branding တောင်းဆိုမှု။
2. Cross-tenant visual consistency လိုအပ်ချက်။

## Enterprise guardrails

1. Fixed values အစား semantic tokens ဦးစားပေး — **ခြွင်းချက်** ဤ repo classic clone: classic fixed values သုံး။
2. High-contrast accessibility စစ်။
3. Branding extensible + tenant-aware ထား။

## Output expectations

1. Theme-safe enterprise UI။
2. Standard SharePoint themes ကြား regressions မရှိ။

## Typical target paths (SPFx ပရောဂျက် မဆို)

1. `src/**/**/*.module.scss`
2. `src/shared/components/**`

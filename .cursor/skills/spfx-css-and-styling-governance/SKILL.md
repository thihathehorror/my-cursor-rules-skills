---
name: spfx-css-and-styling-governance
description: "[MM] SPFx components အတွက် CSS architecture နှင့် styling governance"
---

# SPFx CSS and Styling Governance

## Use for

1. CSS module structure နှင့် style isolation။
2. SCSS ဖိုင်များ naming တသမတ် + ထိန်းသိမ်းရလွယ်။
3. Web parts ကြား style collisions တား။

## Do not use for

1. Default အနေဖြင့် styling frameworks အသစ် ထည့်။
2. တန်ဖိုးမရှိဘဲ stable component styles ပြန်ရေး။

## Trigger conditions

1. Style layer အသစ် သို့ major visual refresh။
2. CSS conflicts, leakage, maintainability ပြဿနာ။

## Enterprise guardrails

1. Styling local + explicit ထား။
2. Fluent-aligned visual language — **ခြွင်းချက်** ဤ repo classic → SPFx: `DBS-FFW-classicsite/2025/style.css` ကိုက် (`classic-visual-parity`)။ Isolation ဆက်လို။
3. အတိအလင်း ခွင့်မရလျှင် `spfx-solution` မှာ Tailwind မရှိ။

## Output expectations

1. Styling behavior ခန့်မှန်းနိုင်။
2. ရေရှည် style ထိန်းသိမ်းရ ပိုလွယ်။

## Typical target paths (SPFx ပရောဂျက် မဆို)

1. `src/**/**/*.module.scss`
2. `src/shared/components/**`

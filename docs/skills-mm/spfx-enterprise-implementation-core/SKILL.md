---
name: spfx-enterprise-implementation-core
description: "[MM] Enterprise SPFx web parts, extensions, shared modules အတွက် core implementation စံနှုန်းများ"
source: _cursor/skills/spfx-enterprise-implementation-core/SKILL.md
---

# SPFx Enterprise Implementation Core

## Use for

1. SPFx workloads အတွက် implementation ချဉ်းကပ်ပုံ သတ်မှတ်။
2. Service boundaries, error handling, typed contracts အတင်း။
3. ကုဒ်ပြောင်းလဲမှုကို enterprise maintainability စံနှုန်းများနဲ့ ညှိ။

## Do not use for

1. Webpack-specific tuning။
2. Implementation မထိသော pure design/styling ဆုံးဖြတ်ချက်။

## Trigger conditions

1. SPFx ကုဒ်ထဲ feature အသစ် သို့ significant refactor မဆို။
2. Cross-webpart shared service/component ပြောင်းလဲမှု။

## Enterprise guardrails

1. ပြောင်းလဲမှု scoped + ပြန်လှည့်နိုင်။
2. အတိအလင်း မတောင်းလျှင် API contracts ထိန်း။
3. Logic paths ပြင်ရင် test updates လို။

## Output expectations

1. Module boundaries ရှင်း + typed interfaces။
2. Error နှင့် loading behavior ခန့်မှန်းနိုင်။
3. Incidental runtime dependency drift မရှိ။

## Typical target paths (SPFx ပရောဂျက် မဆို)

1. `src/webparts/**`
2. `src/shared/**`

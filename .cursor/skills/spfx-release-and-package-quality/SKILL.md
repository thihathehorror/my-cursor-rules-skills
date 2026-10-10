---
name: spfx-release-and-package-quality
description: "[MM] Enterprise SPFx delivery အတွက် packaging နှင့် release quality controls"
---

# SPFx Release and Package Quality

## Use for

1. Pre-release packaging validation။
2. SKU/package profile စစ် နှင့် App Catalog readiness။
3. Shipped features နှင့် release metadata ကိုက်ညီမှု။

## Do not use for

1. Feature implementation အသေးစိတ်။
2. Release quality နဲ့ မဆိုင် UI-only tasks။

## Trigger conditions

1. `package-solution` workflow ပြောင်းလဲမှု။
2. Release checklist သို့ app packaging တောင်းဆိုမှု။

## Enterprise guardrails

1. Package outputs deterministic။
2. Release မတိုင်မီ solution metadata စစ်။
3. Tenant deploy မတိုင်မီ regressions ဖမ်း။

## Output expectations

1. Release-ready package artifacts။
2. Deployment နှင့် rollback အန္တရာယ် လျှော့။

## Typical target paths (SPFx ပရောဂျက် မဆို)

1. `config/package-solution*.json`
2. `docs/publishing/**`
3. `docs/implementation/**`

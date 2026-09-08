---
name: spfx-accessibility-and-content-quality
description: "[MM] Enterprise SPFx accessibility နှင့် UX text quality guidance"
source: _cursor/skills/spfx-accessibility-and-content-quality/SKILL.md
---

# SPFx Accessibility and Content Quality

## Use for

1. Keyboard, focus, screen-reader validation။
2. Placeholder/fallback/empty/error state quality။
3. UI text ရှင်းလင်းမှု၊ tone၊ actionability။

## Do not use for

1. Build pipeline ပြောင်းလဲမှု။
2. UI မထိသော back-end/service-only updates။

## Trigger conditions

1. Command surfaces သို့ interaction flows အသစ်။
2. User-visible text သို့ state model ပြောင်းလဲမှု မဆို။

## Enterprise guardrails

1. Non-mouse operation parity။
2. ဝေဝါး microcopy ရှောင်။
3. Error နှင့် empty states မှ recovery paths ရှင်း။

## Output expectations

1. Accessible နှင့် နားလည်ရသော UI။
2. ရှင်းမထားသော interactions ကြောင့် support ဝန် လျှော့။

## Typical target paths (SPFx ပရောဂျက် မဆို)

1. `src/webparts/**/components`
2. `src/shared/components`
3. `src/shared/licensing-ui`

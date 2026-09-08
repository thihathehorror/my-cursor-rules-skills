---
name: spfx-property-pane-reactivity
description: "[MM] SPFx မှာ reactive vs non-reactive property pane behavior ရွေးရန် decision framework"
source: _cursor/skills/spfx-property-pane-reactivity/SKILL.md
---

# SPFx Property Pane Reactivity

## Use for

1. Reactive သို့ non-reactive property pane behavior ရွေးခြင်း။
2. Property edits ကြောင့် noisy rerender လျှော့ခြင်း။

## Do not use for

1. Property pane experience နဲ့ မဆိုင် business logic။
2. Styling-only tasks။

## Trigger conditions

1. Property pane fields အသစ် သို့ ပြင်။
2. Web part properties တည်းဖြတ်စဉ် performance သို့ UX ပြဿနာ။

## Enterprise guardrails

1. Lightweight immediate feedback = reactive ဦးစားပေး။
2. Expensive operations သို့ external calls = non-reactive ဦးစားပေး။
3. Apply behavior ကို users ထံ ရှင်းပြ။

## Output expectations

1. Property-edit experience ခန့်မှန်းနိုင်။
2. Edit-time performance regressions လျှော့။

## Typical target paths (SPFx ပရောဂျက် မဆို)

1. `src/webparts/**/**WebPart.ts`

---
name: spfx-extensions-enterprise-patterns
description: "[MM] SPFx extensions enterprise patterns — dialogs, commands, host-safe UX"
source: _cursor/skills/spfx-extensions-enterprise-patterns/SKILL.md
---

# SPFx Extensions Enterprise Patterns

## Use for

1. Application Customizer, Field Customizer, ListView Command Set အလုပ်။
2. SPFx extensions ထဲ custom dialog patterns။
3. Command interaction နှင့် discoverability quality။

## Do not use for

1. Extensions မပါသော web-part-only behavior။
2. Toolchain-only ပြဿနာ။

## Trigger conditions

1. Extension feature implementation သို့ refactor။
2. Command surface, dialog, host-page integration updates။

## Enterprise guardrails

1. Host context လေးစား; disruptive overlays ရှောင်။
2. Command behavior ခန့်မှန်းနိုင် + ပြန်လှည့်နိုင်။
3. Dialogs နှင့် command flows မှာ accessibility။

## Output expectations

1. ဘေးကင်း၊ သပ်သော extension UX။
2. Host-page side effects အနည်းဆုံး။

## Typical target paths (SPFx ပရောဂျက် မဆို)

1. `src/extensions/**`
2. `src/shared/**`

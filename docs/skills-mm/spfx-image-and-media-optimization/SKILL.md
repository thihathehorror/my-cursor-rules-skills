---
name: spfx-image-and-media-optimization
description: "[MM] Responsive နှင့် performance-aware SPFx image/media optimization patterns"
source: _cursor/skills/spfx-image-and-media-optimization/SKILL.md
---

# SPFx Image and Media Optimization

## Use for

1. Image-heavy web parts သို့ dashboard cards။
2. Responsive media handling နှင့် display performance။
3. SPFx image helper guidance ပေါင်းစည်း။

## Do not use for

1. Non-media feature အလုပ်။
2. Pure build pipeline tuning။

## Trigger conditions

1. Image rendering လိုအပ်ချက် အသစ်။
2. Image loading နှေး သို့ layout shift။

## Enterprise guardrails

1. Page performance နှင့် perceived load speed optimize။
2. Default views မှာ oversized assets ရှောင်။
3. Images အတွက် accessibility metadata ထိန်း။

## Output expectations

1. Image rendering paths ပိုမြန်။
2. Viewport sizes ကြား responsive ပိုကောင်း။

## Typical target paths (SPFx ပရောဂျက် မဆို)

1. `src/webparts/**/assets`
2. `src/webparts/**/components`

---
name: spfx-enterprise-code-and-performance
description: >-
  [MM] SPFx web parts/extensions coding, performance, best-practice —
  data access (REST, Graph, PnPjs), recommended npm packages, sample patterns။
---

# SPFx Enterprise Code & Performance Guidance

**SPFx ကုဒ်ရေး သို့ review** သည့်အခါ သုံး — UX သက်သက်မဟုတ်:

- Data access ချဉ်းကပ်ပုံ ရွေး (SP REST, Microsoft Graph, PnPjs)။
- Services, hooks, components ဖွဲ့စည်း။
- Performance best practices (bundle size, network calls, rendering)။
- SPFx အတွက် အများလက်ခံ npm packages ရွေး။

ဤ skill = **code-focused**; တွဲ:

- UX အတွက် `spfx-enterprise-design-core` + `spfx-accessibility-and-content-quality`။
- Theming/styling အတွက် `spfx-theme-and-brand-integration` + `spfx-css-and-styling-governance`။

---

## 1. Overall architectural patterns

1. **Separation of concerns**
   - Web parts/extensions = **thin shells**; logic ရွှေ့:
     - `services/` (data access, domain logic)
     - `components/` (pure React views + small view-model logic)
     - `hooks/` (reusable state/data hooks)

2. **Typed contracts everywhere**
   - External data တိုင်း interfaces:
```ts
export interface ISiteRiskSummary {
  siteId: string;
  title: string;
  url: string;
  riskScore: number;
  externalUsersCount: number;
}
```

3. **Web part instances နဲ့ ချည်သော static singletons ရှောင်**
   - Context သို့ service instances ကို props သို့ React context ဖြင့် ပေး။

---

## 2. Data access: REST, Graph, and PnPjs

### 2.1 Recommended stack

- SharePoint data = **SharePoint REST** သို့ **PnPjs (`@pnp/sp`)**။
- Cross-service data = **Microsoft Graph** သို့ **PnPjs `@pnp/graph`**။
- **PnPjs** ဦးစားပေး:
  - Cleaner, fluent APIs။
  - Batching, caching, error handling built-in။

Install (ဥပမာ):
```bash
npm install @pnp/sp @pnp/graph @pnp/logging @pnp/common @pnp/odata --save
```

Web part/extension တိုင်း `onInit` မှာ PnPjs တစ်ကြိမ် initialize:

```ts
import { sp } from '@pnp/sp';
import { SPFx } from '@pnp/spfx';

protected async onInit(): Promise<void> {
  await super.onInit();

  sp.setup({
    spfxContext: this.context
  });
}
```

### 2.2 Sample data service with PnPjs

```ts
// services/SiteRiskService.ts
import { sp } from '@pnp/sp';
import '@pnp/sp/webs';
import '@pnp/sp/lists';
import '@pnp/sp/items';

import { ISiteRiskSummary } from '../models/ISiteRiskSummary';

export class SiteRiskService {
  public async getTopRiskSites(take: number = 20): Promise<ISiteRiskSummary[]> {
    const items = await sp.web.lists.getByTitle('SiteRisk').items
      .select('Id,Title,SiteUrl,RiskScore,ExternalUsersCount')
      .orderBy('RiskScore', false)
      .top(take)();

    return items.map(i => ({
      siteId: i.Id.toString(),
      title: i.Title,
      url: i.SiteUrl,
      riskScore: i.RiskScore,
      externalUsersCount: i.ExternalUsersCount
    }));
  }
}
```

Guidelines:
- REST calls = service classes; **raw REST URLs ကို components ကြား မဖြန့်**။
- လိုအပ်သော fields သာ `select`/`expand`။
- List အပြည့် မယူ — `top()` + paging။

---

## 3. Performance best practices

### 3.1 Bundle size

1. **SPFx/SharePoint ပေးသော frameworks သုံး**
   - SPFx က ရှိပြီး React/Fluent UI ကို ကိုယ်ပိုင် bundle မလုပ်။

2. **ကြီးသော general-purpose libraries ရှောင်**
   - Focused utilities (`moment` အစား `date-fns`)။

3. **Heavy, low-frequency features = dynamic imports**

```ts
const LazyDetailsPanel = React.lazy(() =>
  import(/* webpackChunkName: 'details-panel' */ './DetailsPanel')
);
```

### 3.2 Network performance

1. **Batching** (PnPjs):
```ts
import { sp } from '@pnp/sp';

const [batchedSP, execute] = sp.batched();

const sitesPromise = batchedSP.web.lists.getByTitle('Sites').items.top(100)();
const policiesPromise = batchedSP.web.lists.getByTitle('Policies').items.top(100)();

await execute();

const [sites, policies] = await Promise.all([sitesPromise, policiesPromise]);
```

2. မကြာခဏသုံး reference data **Caching** (PnPjs `caching`)။

3. **Chatty patterns ရှောင်**
   - Row တိုင်း REST ၁ ခေါ် မလုပ်; filter, aggregation, batched reads။

### 3.3 Rendering performance

1. Heavy child components = **React memoization**:
```ts
export const RiskTile = React.memo((props: IRiskTileProps) => {
  // render
});
```

2. ကြီးသော lists = **windowing/virtualization** (ဥပမာ `@fluentui/react` `DetailsList` + `onRenderMissingItem` သို့ ခွင့်ပြု third-party virtual list)။

3. `render` ထဲ heavy computation ရှောင်; hooks သို့ services မှာ pre-compute။

---

## 4. Recommended npm packages (baseline)

Governance ခွင့်ရရင် စဉ်းစား:

- **`@pnp/sp`, `@pnp/graph`** – SharePoint နှင့် Graph အတွက် fluent, typed access။
- **`@fluentui/react`** – Microsoft design-system; M365 နဲ့ ကိုက်။
- **`date-fns`** – Lightweight date utilities။
- **`lodash-es` (cherry-picked)** – Helpers; tree-shaken imports (`import debounce from 'lodash-es/debounce'`)။

ရှောင်:
- Fluent UI နဲ့ ထပ်သော ကြီး UI frameworks။
- SPFx theming နဲ့ မကိုက် runtime styling frameworks — အတိအလင်း ခွင့်မှလွဲ။

---

## 5. Error handling & logging

1. Services မှာ error handling ဗဟိုပြု:
```ts
public async getData(): Promise<IData[]> {
  try {
    return await sp.web.lists.getByTitle('Data').items();
  } catch (error) {
    // Optionally log to App Insights or console in dev
    console.error('Failed to load data', error);
    throw error; // Let UI decide how to present the failure
  }
}
```

2. UI components က errors ကို friendly messages **ပြန်ပြော**; raw error objects **မယို**။

3. Production monitoring ခွင့်ရရင် **Application Insights** ပေါင်း။

---

## 6. How AI editors should use this skill

SPFx ကုဒ် ထုတ်/review:

1. **Data access style ရွေး**: SharePoint/Graph = PnPjs ဦးစားပေး; calls = services။
2. **Typing အတင်း**: External data နှင့် props တိုင်း interfaces။
3. **Performance patterns**: batching, caching, lazy loading, memoization, tree shaking။
4. **Safe npm packages**: အထက်စာရင်း; မလို heavy deps ရှောင်။
5. **Maintainability**: Thin web part/extension classes, services ရှင်း၊ reusable hooks/components။

Design, theming, toolchain skills တွဲပြီး Microsoft guidance နဲ့ ကိုက် **enterprise-grade SPFx** — မြန်၊ ထိန်းသိမ်းရ၊ ညှိ။

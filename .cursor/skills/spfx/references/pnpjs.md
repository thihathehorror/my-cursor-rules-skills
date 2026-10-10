# PnPjs Data Access (default)

**Rule: SPFx မှာ SharePoint နှင့် Microsoft Graph data operation တိုင်း PnPjs သုံး။** ဤ skill ၏ default data-access layer။ User အတိအလင်း တောင်းမှ သို့ ပရောဂျက်ထဲ dependency ထည့်မရမှသာ raw `SPHttpClient` သို့ `MSGraphClientV3`။

## Install

လိုအပ်သော operations နဲ့ ကိုက် **latest** PnPjs packages။ ပရောဂျက် SPFx/TypeScript level ကိုက် major version pin (`package.json` အရင်ဖတ်):

```
npm install @pnp/sp @pnp/graph --save
```

- `@pnp/sp` — SharePoint REST (lists, items, files, site, search)။
- `@pnp/graph` — Microsoft Graph (users, groups, mail, calendar, Teams)။

Bundle သေးရန် အစစ်သုံး packages သာ install။

## SPFx context ဖြင့် initialize

Auth, base URL, telemetry အလိုအလျောက် ချိတ်ရန် SPFx context ဖြင့် PnPjs instance တစ်ကြိမ်ဖန်။ `onInit()` မှာလုပ်ပြီး instance သိမ်း — call တိုင်း ပြန်ဖန် မလုပ်။

```typescript
import { spfi, SPFx as spSPFx } from "@pnp/sp";
import { graphfi, SPFx as graphSPFx } from "@pnp/graph";
import "@pnp/sp/webs";
import "@pnp/sp/lists";
import "@pnp/sp/items";
import "@pnp/graph/users";

// In a web part: this.context is WebPartContext
const sp = spfi().using(spSPFx(this.context));
const graph = graphfi().using(graphSPFx(this.context));
```

Extensions: extension `this.context` ပေး။ Service-scoped: service class ထဲ instance ဖန်ပြီး context ဖြတ်။

## Selective imports

PnPjs = modular — သုံးသည့် sub-modules သာ import၊ tree-shaking က bundle သေးစေ။ Side-effect modules (ဥပမာ `"@pnp/sp/items"`) ကို instance setup နေရာမှာ တစ်ကြိမ် import။

## Common operations

```typescript
// Read items from a list (select only needed fields, page with top)
const items = await sp.web.lists
  .getByTitle("Documents")
  .items.select("Id", "Title", "Modified").top(50)();

// Create an item
await sp.web.lists.getByTitle("Tasks").items.add({ Title: "New task" });

// Update an item
await sp.web.lists.getByTitle("Tasks").items.getById(1).update({ Title: "Updated" });

// Delete an item
await sp.web.lists.getByTitle("Tasks").items.getById(1).delete();

// Microsoft Graph: current user
const me = await graph.me();
```

## Permissions for Graph

Microsoft Graph နှင့် cross-resource calls = **SharePoint admin center → API access** မှာ API permissions approve လို။ `package-solution.json` `webApiPermissionRequests` မှာ ကြေညာ၊ deploy ပြီး admin approve ရမည်ဟု user ကို ပြော။

## Best practices

- Payload သေးရန် `.select()` နှင့် `.top()` — fields/rows အားလုံး မျက်စိမှိတ် မယူ။
- UI မှာ errors + loading states ကိုင်; swallow မလုပ်၊ failures ပြ။
- Data logic = service/helper — React render code ထဲ မထား။
- Type conflicts ရှောင်ရန် PnPjs major version ကို ပရောဂျက် SPFx + TypeScript နဲ့ ကိုက်။

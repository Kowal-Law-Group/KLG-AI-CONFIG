# Notion Schema: Research Database

## Database ID

Data source: `collection://622bfafd-45b1-451a-b518-f72d86767cb0`

## Key Properties for Authority Entries

### Title (required)
- Type: title
- Format: "[Case Name], [Full Citation] ([Year])"
- Example: "Conover v. Hall, 11 Cal.3d 842 (1974)"
- For statutes: "Cal. Civ. Proc. Code § 437c"

### Case Portal (relation)
- Type: relation to `collection://2da0fc06-a06c-8033-978b-000bd2803cd4`
- Format: JSON array string with page URL(s)
- Example: `"[\"https://www.notion.so/2fd0fc06a06c80b0bb84f430ecece2f5\"]"`
- For multiple relations:
  `"[\"https://www.notion.so/PAGE_ID_1\",\"https://www.notion.so/PAGE_ID_2\"]"`
- CRITICAL: Must be a JSON-encoded array string. A bare URL
  or page ID will silently fail.

### 📚Related Research (self-relation)
- Type: relation to `collection://622bfafd-45b1-451a-b518-f72d86767cb0`
- Format: Same JSON array string format as Case Portal
- Use this to link the authority back to the research
  project page that produced it.

### Tags (multi-select)
- Type: multi_select
- For authorities, use: `["Research", "Westlaw Authority"]`
- NOTE: "Westlaw Authority" may not exist as an option yet.
  If creation fails due to unknown option, first run:
  ```
  notion-update-data-source with statements:
  ALTER COLUMN "Tags" SET MULTI_SELECT(
    [all existing options],
    'Westlaw Authority':purple
  )
  ```
  IMPORTANT: ALTER COLUMN for multi-select requires passing
  ALL existing options plus the new one. Fetch the current
  schema first to get the complete option list.

### Publish or Pass? (status)
- Type: status
- For authorities: "Not Applicable"

### Note (text)
- Type: text
- Format: "[Court], [Year]. Cited in [N] research memos
  for [Matter Short Name]."

### Date (date)
- Type: date
- Use expanded format: `"date:Date:start": "2026-03-10"`

### Salience (select)
- Type: select
- Options: "★", "★★", "★★★"
- For high-leverage authorities (cited in 3+ memos): "★★★"
- For standard authorities: "★★"

## Deduplication Search

To check if an authority already exists:

1. Use `notion-search` with the case name or citation as
   the query, scoped to the Research database:
   ```
   data_source_url: "collection://622bfafd-45b1-451a-b518-f72d86767cb0"
   query: "[case name or citation]"
   ```

2. If a match is found, fetch the page to confirm it's
   the same authority (not just a similar name).

3. If confirmed duplicate: update the existing page's
   Case Portal and Related Research relations to include
   the new matter. Do NOT create a new page.

## Batch Creation Considerations

- Notion API has rate limits. For large batches (50+),
  expect the process to take 5–10 minutes.
- The `notion-create-pages` tool supports creating up
  to 100 pages in a single call, but each page needs
  unique content, so batch by groups of 5–10 to manage
  context and error handling.
- If a creation fails, log the failure and continue with
  the remaining authorities. Report all failures at the end.

# Notion Schema: Research Database (Content Research)

## Database & View IDs

- **Data source:** `collection://622bfafd-45b1-451a-b518-f72d86767cb0`
- **Blog This: Add Research view:** `view://16c0fc06-a06c-8091-ac93-000c48d0e6e6`
  - Filters: Research Tags contains "Blog or Pod This" tag
    AND Publish or Pass? = "Need Research"

## Key Properties for This Skill

### Title (title)
The item name as entered in the database. May contain case
names, article titles, or topic descriptions.

### Publish or Pass? (status)
The workflow status. This skill transitions items from
"Need Research" to "Further Review".

Valid values for this skill:
- Read: `"🔍Need Research"` (items to process)
- Write: `"👓Further Review"` (items after processing)

### URL (url)
Property name: `userDefined:URL`
The source URL for the item. May be a court site, blog,
news outlet, Westlaw, Lexis, or LinkedIn URL.

### Research Tags (relation)
Property name: `🏷️Research Tags`
Relation to the Research Tags database. Items in the
"Blog This: Add Research" view have the "Blog or Pod This"
tag. Do NOT modify this property.

### Note (text)
Short text note. After processing, update with:
"[Court], [Year]. Full text loaded [date]." (for cases)
or "[Source]. Content fetched [date]." (for articles)

### Case Pub Date (text)
The publication date of the case or article. May be
pre-populated. Do not overwrite if already set.

### Legal Content Production (relation)
Property name: `📡 Legal Content Production`
Relation to the content production database. Do NOT modify
this property -- it is managed separately.

## Updating Records

### Changing Status

Use `notion-update-page` with the page URL/ID:

```
"Publish or Pass?": "👓Further Review"
```

### Inserting Page Content

Use `notion-update-page` with `update_content` to append
content to the page body. Use Notion-flavored markdown.

IMPORTANT: The `update_content` field uses `old_str` and
`new_str` for targeted edits. For appending to an empty
page, use `insert_content_after` instead, or use
`update_content` with the last line of existing content
as `old_str`.

For pages that may be empty, the safest approach is:
1. Fetch the page first to see existing content.
2. If empty, use `insert_content_after` with no anchor
   (appends to end).
3. If not empty, use `insert_content_after` with the last
   content block as anchor.

### Batch Considerations

- When processing 10+ records, expect 1-2 minutes for all
  Notion API calls.
- If rate-limited (429 error), wait 2 seconds and retry.
- Process records sequentially, not in parallel.
- Report each successful update to the user as it completes.

## Idempotency

Before updating any record, fetch its current content.
If the page body already contains "## Case Text" or
"## Source Content", the record was already processed
by a prior run. Skip it.

## Template Awareness

The Research database has a "Need Research" default
template (ID: `23b0fc06-a06c-8030-9a8f-f4e3d1f1d40e`).
New items created from this template may have placeholder
content. Do not treat template placeholder text as
"already processed."

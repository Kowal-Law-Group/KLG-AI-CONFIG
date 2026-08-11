# Comet Westlaw Find & Print Prompt

## Template

```
COMET WESTLAW INSTRUCTIONS:

The authority list below needs to be run through Westlaw
Find & Print.

1. Open a new browser tab.
2. Navigate to Westlaw Find & Print.
3. If a login screen appears, pause for user login.
4. Paste the authority list into the Find & Print input field.
5. Verify the pasted content matches.
6. NEVER choose "Substitute with reporter images when available
   (PDF)" or similar options.
7. Apply these settings:
   - Documents: Full text documents
   - Cases: Full text documents with reporter images
   - Statutes & Court Rules: Statutory text only
   - Delivery: Download
   - Format: Word (.doc)
   - Output: Single merged file
8. If Westlaw reports citations are out of plan, unselect them.
   Do not incur additional charges.
9. If Westlaw does not accept certain citations, skip them and
   report to user at end.
10. Execute Find & Print and download the resulting .doc file.

AUTHORITY LIST:
[INSERT FORMATTED AUTHORITY LIST HERE]
```

## Authority List Formatting Rules

### Cases
- Reporter volume, reporter name, and start page ONLY
- Omit case name and year
- Examples:
  - `75 Cal.App.5th 1234`
  - `592 F.3d 1063`

### Statutes
- Code name and section number
- Examples:
  - `Cal. Civ. Code § 1942.4`
  - `42 U.S.C. § 1983`

### Formatting
- One authority per line
- No blank lines between entries
- Batches of 100 max if over 100 items

### Deduplication
- Remove exact duplicates before generating the list
- Use only the base citation (volume + reporter + start page)

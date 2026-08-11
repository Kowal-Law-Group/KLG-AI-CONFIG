---
name: klg-shared-scripts
description: "Shared utility scripts used by other KLG skills. Contains fix_docx_standalone.py which fixes the Word 'unreadable content' error caused by pack.py stripping standalone='yes' from XML declarations. This skill is not triggered directly — it provides scripts called by other skills during .docx generation."
---

# KLG Shared Scripts

Utility scripts shared across KLG skills. These are not invoked directly
by the user — they are called by other skills as part of their workflows.

## fix_docx_standalone.py

Fixes the Microsoft Word "Word found unreadable content" error that
occurs when .docx files are produced by the public docx skill's
`pack.py`. The root cause is that `pack.py` uses Python's
`minidom.toxml()` to condense XML, which silently strips
`standalone="yes"` from XML declarations. Word requires this attribute.

### Usage

Run after every `pack.py` call that produces a .docx, before delivering
the file:

```bash
python /mnt/skills/user/klg-shared-scripts/fix_docx_standalone.py output.docx
```

The script fixes the file in place. It is idempotent — safe to run
multiple times, and harmless on files that don't need fixing.

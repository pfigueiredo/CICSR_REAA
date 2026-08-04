# Step 06 — Multipage migration

## Goal

Implement the **public** multi-page structure in static HTML. Reuse existing CSS/JS/i18n; do not redesign. No Chat / private / Loja routes.

## Prerequisites

- [x] Steps 02 and 05 accepted
- [x] Step 05 placeholder copy frozen
- Step 09 left deferred

## Note

**Planning gate cleared.** Step 04 replies can arrive in parallel.

## Status

`done` (2026-08-04) — public multipage tree generated

---

## Tasks

- [x] Create folder structure matching public routes
- [x] Shared header/nav/footer (generated consistently via `scripts/build_multipage.py`)
- [x] Move Confederação, Princípios, Membros, História, Documentos, Contactos to pages
- [x] Homepage portal (hero + area grid)
- [x] Placeholder pages (Comunicações, Eventos, 1762/1786, história threads)
- [x] Do **not** add `/chat/`, `/biblioteca/`, `/loja/`
- [x] Fix i18n fetch for nested paths (`getSiteRoot()` in `js/i18n.js`)
- [x] Relative asset paths from depth-1 and depth-2
- [ ] Smoke-test on GitHub Pages after push

## Regenerating pages

```bash
python scripts/build_multipage.py
```

Re-run after changing chrome/nav templates in that script. Hand-edits to generated HTML will be overwritten.

## Deliverables

- Portal `index.html` + section folders
- Locale keys for portal / placeholders / events / communications (PT EN FR AR)
- Latin signatory spelling: Kamal **El Fadhi** (AR Arabic form unchanged pending confirmation)
- CSS: `.portal-grid`, `.status-block`, `.footer-nav`, `.documents-4`

## Acceptance criteria

- [x] Primary nav targets resolve as folders
- [x] Placeholders use Step 05 pattern
- [x] No Chat / shop / private UI
- [x] Design tokens retained
- [x] Nested `locales/*.json` load via script-relative root

## Next

→ Step 07 polish (hreflang per page, AR name confirmation, any path QA)  
→ Step 08 when stakeholder content arrives  
→ Step 10 launch checklist before calling it shipped

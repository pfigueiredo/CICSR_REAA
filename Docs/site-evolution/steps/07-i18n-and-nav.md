# Step 07 — i18n and nav

## Goal

Make multipage navigation and locales consistent across PT/EN/FR/AR, including RTL and the El Fadhi spelling fix.

## Prerequisites

- Step 06 structure in progress or done
- Signatory spelling confirmed (Kamal El Fadhi)

## Inputs

- `locales/*.json`
- `js/i18n.js`
- Nav labels from Step 02
- Placeholder strings from Step 05

## Tasks

- [ ] Add locale keys for new nav items and placeholder pages
- [ ] Fix `Kamal El-Fehdi` → `Kamal El Fadhi` (or exact approved form) in all locales
- [ ] Ensure language switcher keeps path + `?lang=` (or equivalent) on every page
- [ ] Update `hreflang` / alternate links per page if needed
- [ ] Verify Arabic RTL on nested routes (`css/rtl.css`)
- [ ] Mobile menu: primary vs secondary items

## Decisions needed

- Exact public spelling: `El Fadhi` vs `El-Fadhi` vs Arabic form on AR locale

## Deliverables

- Locale diffs reviewed
- Nav complete in four languages

## Acceptance criteria

- No missing i18n keys on new pages
- Spelling corrected site-wide
- AR layout usable on `/historia/reaa/` depth

## Status

`todo`

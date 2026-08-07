# Section — Comunicações (Discurso do Presidente)

## Purpose

Publish institutional communications, starting with the President’s address; later possibly boletim / comunicados (`Docs/specs.txt` IV).

## Route(s)

- `/comunicacoes/` — hub (discursos + future notes)
- `/comunicacoes/discurso-lisboa-2026/` — Discurso de posse (Lisboa, 4 Jul 2026)

## Nav visibility

**footer / secondary only** (not primary; primary nav already has 7 items)

## Content status

`ready` for first speech (HTML PT/EN/FR + PDF PT/EN/FR/ES). AR page: note + Portuguese body until translation exists.

## Decisions (Step 04 — 2026-08-06 / speech publish 2026-08-07)

- Publish President’s address under Comunicações (not a separate `/discursos/` tree)
- Site locales: PT / EN / FR / AR; **ES = PDF download only** (no 5th site locale)
- PDFs: originals in `Docs/discursos/`; public copies in `assets/speeches/`
- Photo: `assets/people/jose-manuel-moreira.jpg` (from `Docs/HCT25822.jpg`)
- Q11 boletim under Comunicações? — **after meeting**

## Presidency (byline)

- **José Manuel Moreira**, Supremo Conselho Português · SGC
- Speech date: **4 July 2026** (Lisboa) — 1st presidential mandate of the Confederation
- Mandate window (stakeholder): **4 July 2026 – 3 July 2029**

## Sources

- `Docs/discursos/` — PT, EN, FR, ES PDFs
- `Docs/HCT25822.jpg` — portrait
- Strategic mention of “Mensagem do Presidente” in `Docs/specs.txt`
- Presidency rotation: **Portugal → Marrocos → Brasil → França** (Regulamento Art. 9; 3-year mandates)

## Subpages / subsections

- Hub card → speech page
- PDF downloads: PT / EN / FR / ES
- Future: comunicados, boletim (note on hub only)

## i18n notes

Keys: `communications.*`, `speech.lisboa2026.*`  
AR: `speech.lisboa2026.arNote` + Portuguese `bodyHtml` / salutation until Arabic translation.

## Open questions

- Boletim under Comunicações? (Q11 — post-meeting)
- Photo credit for discurso (if required)

## Ready for implementation?

yes — published (first speech)

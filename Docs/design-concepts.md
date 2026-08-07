# CISCSR Website — Design Concepts / Conceitos de Design

> **Scope / Âmbito:** This document describes the **website design only**—visual identity, layout, typography, colour, multilingual delivery, and technical approach. It does **not** present the Confederation's mission, doctrine, or strategic programme (covered separately by another speaker).

---

## 1. Purpose of this document / Objetivo deste documento

### Português

Este documento explica as decisões de design do website da CISCSR: por que o site tem este aspeto, como comunica dignidade institucional, e como suporta quatro idiomas incluindo árabe. Destina-se a apresentações públicas, revisão por delegados dos Supremos Conselhos, e como referência de manutenção futura.

**Site em produção:** https://pfigueiredo.github.io/CICSR_REAA/

### English

This document explains the design decisions behind the CISCSR website: why it looks the way it does, how it communicates institutional dignity, and how it supports four languages including Arabic. It is intended for public presentations, review by Supreme Council delegates, and as a maintenance reference.

**Live site:** https://pfigueiredo.github.io/CICSR_REAA/

---

## 2. Design challenge / O desafio de design

### Português

A Confederação reúne jurisdições em Portugal, Marrocos, Brasil e França. O website precisa de ser:

- **Uma porta de entrada digital única** — reconhecível, estável, credível
- **Institucional e discreto** — não comercial, não estilo startup, não redes sociais
- **Portador de texto oficial** — a Declaração de Princípios (documento trilingue FR-PT-AR) com o peso visual adequado
- **Multilingue desde a origem** — PT, EN, FR, AR, com suporte RTL para árabe

O desafio não é "chamar a atenção", mas **estabelecer confiança** através da forma.

### English

The Confederation brings together jurisdictions in Portugal, Morocco, Brazil, and France. The website must be:

- **A single digital front door** — recognisable, stable, credible
- **Institutional and discreet** — not commercial, not startup-styled, not social-media driven
- **A carrier of official text** — the Declaration of Principles (trilingual FR-PT-AR document) with appropriate visual weight
- **Multilingual from day one** — PT, EN, FR, AR, with RTL support for Arabic

The challenge is not to "grab attention", but to **establish trust** through form.

---

## 3. Concept: classical institutional / Conceito: institucional clássico

### Português

O conceito central é **institucional clássico** — um site que se comporta como um documento formal, não como uma landing page de marketing.

**Metáfora do documento:** O conteúdo vive dentro de um `page-frame` centrado, sobre fundo pergaminho com grelha subtil. Evoca arquivo, continuidade, registo — não funil de conversão.

**Hero cerimonial:** Fundo navy profundo, moldura dupla dourada, ornamento linear. Funciona como limiar ou portal de entrada, não como banner promocional.

**Ritmo de secções:** Alternância entre superfícies claras (`section-light`), quentes (`section-warm`) e escuras (`section-dark`) cria pacing visual sem animações chamativas.

**Restrição formal:** Raio de cantos zero (`--radius: 0px`); sem tipografia display moderna; sem gradientes decorativos além de texturas discretas de herança.

### English

The core concept is **classical institutional** — a site that behaves like a formal document, not a marketing landing page.

**Document metaphor:** Content lives inside a centred `page-frame` on a parchment grid background. It evokes archive, continuity, and record — not a conversion funnel.

**Ceremonial hero:** Deep navy background, double gold frame, linear ornament. It acts as a threshold or portal, not a promotional banner.

**Section rhythm:** Alternation between light (`section-light`), warm (`section-warm`), and dark (`section-dark`) surfaces creates visual pacing without flashy animation.

**Formal restraint:** Zero border radius (`--radius: 0px`); no modern display typography; no decorative gradients beyond subtle heritage textures.

---

## 4. Colour and typography system / Sistema de cor e tipografia

### 4.1 Colour palette / Paleta de cores

#### Português

| Token | Valor | Uso | Racional |
|-------|-------|-----|----------|
| `--navy` | `#111A2A` | Secção membros, tom do rodapé | Azul-negro profundo: autoridade sem o rigor do preto puro |
| `--navy-deep` | `#08101C` | Hero | Limiar cerimonial; enquadra o nome e o logo |
| `--gold` | `#B08A4A` | Botões, ornamentos, marcadores | Acento tradicional; calor sobre superfícies escuras |
| `--gold-dark` | `#7F6234` | Bordas, regras duplas | Dourado contido — decorativo, não ostentoso |
| `--parchment` | `#F3E8D2` | Fundo da página, secções quentes | Papel envelhecido — não branco estéril |
| `--paper` | `#FBF6EA` | Moldura de conteúdo, cartões | Superfície interior ligeiramente mais clara |
| `--burgundy` | `#691B24` | Faixa do lema, rótulos, declaração | Gravidade e formalidade |
| `--ink` / `--muted` | `#171412` / `#665E52` | Texto principal / secundário | Contraste forte no pergaminho |

**O que rejeitámos:**
- Branco puro + azul corporativo (demasiado genérico, estilo SaaS)
- Vermelhos e dourados de alta saturação (kitschy em ecrã)
- Paletas frias e cinzentas (demasiado burocráticas sem calor)

**Manutenção:** Todas as cores são propriedades CSS em `:root` — um único ponto para afinar o site inteiro.

#### English

| Token | Value | Use | Rationale |
|-------|-------|-----|-----------|
| `--navy` | `#111A2A` | Members section, footer tone | Deep blue-black: authority without harsh pure black |
| `--navy-deep` | `#08101C` | Hero | Ceremonial threshold; frames name and logo |
| `--gold` | `#B08A4A` | Buttons, ornaments, markers | Traditional accent; warmth on dark surfaces |
| `--gold-dark` | `#7F6234` | Borders, double rules | Muted gold — decorative, not flashy |
| `--parchment` | `#F3E8D2` | Page backdrop, warm sections | Aged paper — not sterile white |
| `--paper` | `#FBF6EA` | Content frame, cards | Slightly lighter inner surface |
| `--burgundy` | `#691B24` | Motto band, labels, declaration | Gravitas and formality |
| `--ink` / `--muted` | `#171412` / `#665E52` | Primary / secondary text | Strong contrast on parchment |

**What we rejected:**
- Pure white + corporate blue (too generic, SaaS-like)
- High-saturation reds and golds (kitschy on screen)
- Cold grey palettes (too bureaucratic without warmth)

**Maintenance:** All colours are CSS custom properties in `:root` — a single place to tune the entire site.

#### Palette diagram

```
┌─────────────────────────────────────────────────────────┐
│  navy-deep #08101C  │  HERO — ceremonial threshold     │
├─────────────────────────────────────────────────────────┤
│  parchment #F3E8D2  │  page backdrop (grid texture)    │
│  paper     #FBF6EA  │  content frame, cards, forms       │
├─────────────────────────────────────────────────────────┤
│  gold      #B08A4A  │  accents, CTAs, ornaments          │
│  gold-dark #7F6234  │  borders, double rules           │
├─────────────────────────────────────────────────────────┤
│  burgundy  #691B24  │  motto band, declaration labels    │
│  navy      #111A2A  │  members panel, footer             │
└─────────────────────────────────────────────────────────┘
```

### 4.2 Typography / Tipografia

#### Português

| Papel | Fonte | Onde | Porquê |
|-------|-------|------|--------|
| Títulos e nome institucional | **Georgia** | `h1–h3`, `.lead`, lema, signatários | Serif clássica de sistema; evoca títulos gravados e documentos oficiais; sem dependência de CDN para latim |
| Corpo e interface | **Trebuchet MS** | Parágrafos, navegação, formulários | Sans humanista e legível; incluída em Windows/macOS; sem licenciamento |
| Árabe | **Noto Sans Arabic** | Corpo e títulos em RTL | Cobertura completa de glifos; tom formal; paridade com as outras línguas |

**Princípio:** Serif para a voz institucional; sans para a função de leitura.

**Porque não Inter, Poppins ou Playfair Display:** Evita associações com startups dos anos 2020 ou convites de casamento; reduz tempo de carregamento e dependências.

**Escala responsiva:** Títulos usam `clamp()` — dignidade em desktop e mobile sem designs separados.

#### Type specimen

```
Georgia (headings):
Confederação Internacional dos Supremos Conselhos

Trebuchet MS (body):
Instituição confederal dedicada à cooperação fraterna entre Supremos Conselhos.

Noto Sans Arabic (RTL):
الاتحاد الدولي للمجالس العليا السيادية والمنتظمة
```

#### English

| Role | Font | Where | Why |
|------|------|-------|-----|
| Headings & institution name | **Georgia** | `h1–h3`, `.lead`, motto, signatories | System classical serif; evokes engraved titles and official documents; no CDN dependency for Latin scripts |
| Body & UI | **Trebuchet MS** | Paragraphs, nav, forms | Humanist readable sans; ships with Windows/macOS; no licensing |
| Arabic | **Noto Sans Arabic** | RTL body and headings | Full glyph coverage; formal tone; parity with other languages |

**Principle:** Serif for institutional voice; sans for reading function.

**Why not Inter, Poppins, or Playfair Display:** Avoids 2020s startup or wedding-invitation associations; reduces load time and dependencies.

**Responsive scale:** Headings use `clamp()` — dignity on desktop and mobile without separate designs.

---

## 5. Layout and page structure / Estrutura da página

### Português

O site é uma **página única com âncoras** — adequada a um folheto institucional digital. Cada secção tem um papel de design definido:

| Secção | Papel de design |
|--------|-----------------|
| Cabeçalho fixo + idiomas | Orientação permanente; PT / EN / FR / AR discretos |
| Hero | Âncora de identidade + CTAs primários |
| A Confederação | Texto institucional suplementar (tom web) |
| Quatro pilares | Resumo visual antes da declaração completa |
| `#declaracao` | Bloco de documento formal — borda dupla, signatários em serif |
| Membros (painel escuro) | Mapa + lista de jurisdições |
| História | Cronologia em grelha |
| Documentos | Cartões de arquivo; ligação ao PDF trilingue |
| Lema | Faixa burgundy — citação como pontuação visual |
| Contactos | Canal institucional reservado |

### English

The site is a **single page with anchors** — suited to a digital institutional brochure. Each section has a defined design role:

| Section | Design role |
|---------|-------------|
| Sticky header + languages | Permanent orientation; discreet PT / EN / FR / AR |
| Hero | Identity anchor + primary CTAs |
| The Confederation | Supplementary institutional copy (web tone) |
| Four pillars | Visual summary before full declaration |
| `#declaracao` | Formal document block — double border, serif signatories |
| Members (dark panel) | Map + jurisdiction list |
| History | Grid chronology |
| Documents | Archive cards; link to trilingual PDF |
| Motto | Burgundy band — quotation as visual punctuation |
| Contact | Reserved institutional channel |

---

## 6. Key UI patterns / Padrões de interface

### Português

**Hero:** Navy profundo, logo em variante clara, moldura dourada dupla, ornamento linear com losango. O visitante compreende imediatamente que entrou num espaço institucional.

**Declaração de Princípios:** Bloco `.declaration` com fundo paper, borda tripla, listas formais, signatários em serif. O texto do PDF trilingue é reproduzido verbatim em PT, FR e AR.

**Documentos:** Três cartões com hierarquia tipográfica (rótulo burgundy → título serif → meta muted). O primeiro cartão liga ao PDF oficial.

**Contacto:** Formulário em caixa branca com borda dupla — placeholder para secretariado futuro.

### English

**Hero:** Deep navy, light logo variant, double gold frame, linear ornament with diamond. The visitor immediately understands they have entered an institutional space.

**Declaration of Principles:** `.declaration` block with paper background, triple border, formal lists, serif signatories. Trilingual PDF text reproduced verbatim in PT, FR, and AR.

**Documents:** Three cards with typographic hierarchy (burgundy label → serif title → muted meta). First card links to the official PDF.

**Contact:** Form in white box with double border — placeholder for future secretariat.

---

## 7. Multilingual and RTL approach / Abordagem multilingue e RTL

### Português

- **Mecanismo:** JavaScript vanilla (`js/i18n.js`) + ficheiros JSON em `locales/` — sem framework, sem build step
- **Marcacao:** Atributos `data-i18n` no HTML; listas dinâmicas para a declaração
- **Resolução de idioma:** `?lang=` → `localStorage` → idioma do browser → português por defeito
- **Árabe:** `dir="rtl"` no `<html>`; folha `css/rtl.css`; Noto Sans Arabic para corpo e títulos
- **SEO:** `hreflang` no `<head>` para as quatro línguas

*A paridade entre jurisdições está assumida no design desde o primeiro dia.*

### English

- **Mechanism:** Vanilla JavaScript (`js/i18n.js`) + JSON files in `locales/` — no framework, no build step
- **Markup:** `data-i18n` attributes in HTML; dynamic lists for the declaration
- **Locale resolution:** `?lang=` → `localStorage` → browser language → Portuguese default
- **Arabic:** `dir="rtl"` on `<html>`; `css/rtl.css` stylesheet; Noto Sans Arabic for body and headings
- **SEO:** `hreflang` in `<head>` for all four languages

*Parity across jurisdictions is assumed in the design from day one.*

---

## 8. Logo and brand asset pipeline / Pipeline do logo

### Português

O logo inicial (`Docs/Logo_black_whiteBG.png`) tinha fundo branco opaco — incompatível com o pergaminho e com a secção escura.

O script `scripts/prepare_logo.py` (Pillow):

1. Remove o branco (threshold configurável)
2. Gera `logo-on-light.png` para superfícies claras
3. Gera `logo-on-dark.png` (invertido/dourado) para hero e secções navy
4. Produz `logo-header.png`, `logo-hero.png`, favicons
5. Cria pré-visualizações compostas em `assets/logo/previews/` para QA

Quando o SVG final chegar, o script pode ser estendido; os PNGs servem como fallback.

### English

The initial logo (`Docs/Logo_black_whiteBG.png`) had an opaque white background — incompatible with parchment and the dark section.

The `scripts/prepare_logo.py` script (Pillow):

1. Removes white (configurable threshold)
2. Generates `logo-on-light.png` for light surfaces
3. Generates `logo-on-dark.png` (inverted/gold-tinted) for hero and navy sections
4. Produces `logo-header.png`, `logo-hero.png`, favicons
5. Creates composite previews in `assets/logo/previews/` for QA

When the final SVG arrives, the script can be extended; PNGs serve as fallbacks.

---

## 9. Accessibility and responsive behaviour / Acessibilidade e responsividade

### Português

- HTML semântico (`header`, `main`, `section`, `nav`, `footer`)
- Texto `alt` localizado no logo
- Botões de idioma com `aria-pressed`
- Contraste intencional: texto claro no hero; texto escuro no pergaminho
- Breakpoints: **980px** (menu móvel, grelhas a uma coluna) e **640px** (tipografia e espaçamento reduzidos)

### English

- Semantic HTML (`header`, `main`, `section`, `nav`, `footer`)
- Localised `alt` text on logo
- Language buttons with `aria-pressed`
- Intentional contrast: light text on hero; dark text on parchment
- Breakpoints: **980px** (mobile menu, single-column grids) and **640px** (reduced typography and spacing)

---

## 10. Technical approach (summary) / Abordagem técnica (resumo)

### Português

| Aspeto | Escolha |
|--------|---------|
| Stack | HTML + CSS + JavaScript vanilla |
| Hospedagem | GitHub Pages (deploy automático via Actions) |
| i18n | JSON + `data-i18n` (sem build) |
| Assets | Logo gerado por script Python |
| Repositório | https://github.com/pfigueiredo/CICSR_REAA |

Sem dependência de CMS, servidor, ou framework JavaScript — manutenção acessível a qualquer equipa com competências web básicas.

### English

| Aspect | Choice |
|--------|--------|
| Stack | Vanilla HTML + CSS + JavaScript |
| Hosting | GitHub Pages (automatic deploy via Actions) |
| i18n | JSON + `data-i18n` (no build) |
| Assets | Logo generated by Python script |
| Repository | https://github.com/pfigueiredo/CICSR_REAA |

No CMS, server, or JavaScript framework dependency — maintainable by any team with basic web skills.

---

## 11. What this site deliberately avoids / O que o site evita deliberadamente

### Português

- Estética de startup ou produto SaaS
- Sliders, vídeos de fundo, animações de scroll
- Tipografia display moderna (Inter, Poppins)
- Branco puro e azul corporativo genérico
- Dependência de plataformas proprietárias
- Conteúdo estratégico da Confederação (calendário, boletim, rotação) — reservado para fase posterior

### English

- Startup or SaaS product aesthetic
- Sliders, background videos, scroll animations
- Modern display typography (Inter, Poppins)
- Pure white and generic corporate blue
- Dependency on proprietary platforms
- Confederation strategic content (calendar, bulletin, rotation) — reserved for a later phase

---

## 12. Live URL and file map / URL e mapa de ficheiros

### Português

**Site:** https://pfigueiredo.github.io/CICSR_REAA/  
**Apresentação (deck PT + FR):** https://pfigueiredo.github.io/CICSR_REAA/presentation/

```
CICSR_REAA/
  index.html              # Página principal
  css/styles.css          # Design tokens e estilos
  css/rtl.css             # Overrides RTL
  js/i18n.js, js/main.js  # Internacionalização e menu
  locales/*.json          # Traduções PT, EN, FR, AR
  assets/logo/            # Variantes do logo
  Docs/design-concepts.md # Este documento
  presentation/           # Deck reveal.js
```

### English

**Site:** https://pfigueiredo.github.io/CICSR_REAA/  
**Presentation (PT + FR deck):** https://pfigueiredo.github.io/CICSR_REAA/presentation/

(Same file map as above.)

---

## Appendix A: Colour tokens / Apêndice A: Tokens de cor

```css
:root {
  --navy: #111A2A;
  --navy-deep: #08101C;
  --burgundy: #691B24;
  --gold: #B08A4A;
  --gold-dark: #7F6234;
  --parchment: #F3E8D2;
  --paper: #FBF6EA;
  --ink: #171412;
  --muted: #665E52;
  --line: rgba(127, 98, 52, 0.36);

  --serif: Georgia, "Times New Roman", Times, serif;
  --sans: "Trebuchet MS", Arial, sans-serif;

  --content: 1160px;
  --radius: 0px;
}
```

Source: `css/styles.css`

---

## Appendix B: Screenshot list for presenters / Apêndice B: Capturas para apresentadores

| File | Description |
|------|-------------|
| `hero-pt.png` | Hero section (Portuguese) |
| `declaration-pt.png` | Declaration of Principles block |
| `pillars.png` | Four pillars grid |
| `members-dark.png` | Dark members section |
| `arabic-rtl.png` | Full page with `?lang=ar` |
| `mobile.png` | Mobile viewport (390px) |

Located in: `presentation/assets/screenshots/`

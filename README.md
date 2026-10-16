# Hisab Technical Services — website

Static website for Hisab Technical Services LLC (Dubai), focused only on air conditioning:

1. **Split AC** — supply and installation
2. **VRF / VRV AC systems** — design, installation, commissioning
3. **Ducted split AC** — duct design, installation, air balancing
Focus: new installations for buildings, towers and villas. Maintenance only during the warranty period.

MEP, electrical, plumbing, gypsum and fit-out content from the previous draft was removed on purpose.

## Pages
| File | Page |
|---|---|
| `index.html` | Home: hero, the 3 AC packages, why Hisab, process, project spotlight, FAQ |
| `ac-systems.html` | Comparison table + detail for each package (`#split`, `#vrf`, `#ducted`) |
| `contact.html` | Free site inspection form (`#book`), phone, WhatsApp, e-mail |
| `projects.html` | Project galleries (real photos from the company profile) + reference list |
| `about.html` | Company, leadership, vision, mission, principles |
| `thank-you.html`, `404.html` | Form success page and not-found page |

## Request form
The form uses **Netlify Forms** (form name `site-inspection`). Submissions appear in Netlify → the site → **Forms**.
To get an e-mail for each request: Netlify → Forms → **Form notifications** → Add notification → Email.

Package buttons open the form with the system already selected (`maintenance.html?system=vrf#book`).

## Deploy
Plain HTML/CSS/JS, no build step. Netlify publishes the repository root (`netlify.toml`).

## Photos
All pictures in `assets/photos/` can be replaced by a file with the same name (hero, pkg-split, pkg-vrf, pkg-ducted, why). Adding `team.jpg` and `uniform-back.jpg` turns on the "Our team" section. Rebuild with `_tools/build.py`.

## Editing
Pages are plain HTML. `_tools/build.py` regenerates all pages from one file (shared header, footer, packages, FAQ):
`python3 _tools/build.py .` — run it from this folder after editing the text in the script.

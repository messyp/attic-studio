# Beautiful Distraction

The studio website at https://beautifuldistraction.com: a hand-written home page (`index.html`, with its styles, moth and textures in `home/`), plus a support page and a privacy policy for each app. Plain HTML, hosted free on GitHub Pages. The repo keeps its old name, `attic-studio`.

## Pages

| Page | Path | Used for |
|---|---|---|
| Home | `/` | Marketing URL (optional) |
| Watch Toys | `/watch-toys/` and `/watch-toys/privacy/` | App Store Connect → Support URL and Privacy Policy URL |
| Watch Pinball | `/watch-pinball/` and `/watch-pinball/privacy/` | the same |
| Pixel MTB | `/pixel-mtb/` and `/pixel-mtb/privacy/` | the same, when it ships |

Support and privacy pages are generated: edit the app list (or the support address, `CONTACT`) in `tools/build.py`, then run `python3 tools/build.py`. Commit the generated HTML; GitHub Pages serves it as is. The home page isn't generated, so add new apps to `index.html` by hand. `tools/make_paper.py` regenerates the textures.

## Hosting

GitHub Pages deploys `main` from the repo root. The domain is registered and managed at Cloudflare, with DNS-only records for GitHub Pages, and `CNAME` holds the custom domain. Old `messyp.github.io/attic-studio/...` URLs redirect here, so App Store Connect links keep working.

## Adding an app

Add an entry to `APPS` in `tools/build.py` (name, tagline, help and privacy text), put a 256×256 icon at `images/<slug>-icon.png`, run the build, and add a card to `index.html`.

## Previewing locally

`python3 -m http.server 8123` in this folder, then open http://localhost:8123.

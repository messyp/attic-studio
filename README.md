# Attic Studio

The Attic Studio website: a home page, plus a support page and a privacy policy for each app. Plain HTML and one stylesheet, hosted free on GitHub Pages.

## Pages

| Page | Path | Used for |
|---|---|---|
| Home | `/` | Marketing URL (optional) |
| Watch Toys | `/watch-toys/` and `/watch-toys/privacy/` | App Store Connect → Support URL and Privacy Policy URL |
| Watch Pinball | `/watch-pinball/` and `/watch-pinball/privacy/` | the same, when it ships |
| Pixel MTB | `/pixel-mtb/` and `/pixel-mtb/privacy/` | the same, when it ships |

The pages are generated: edit the app list (or the support address, `CONTACT`) in `tools/build.py`, then run `python3 tools/build.py`. Commit the generated HTML; GitHub Pages serves it as is.

## Publishing on GitHub Pages

1. Create a **public** repo (Pages on a free account needs public), e.g. `attic-studio`, and push this folder to `main`.
2. Repo → Settings → Pages → Build and deployment: **Deploy from a branch**, branch `main`, folder `/ (root)`.
3. After a minute the site is at `https://<username>.github.io/attic-studio/`, so the Watch Toys URLs are
   `https://<username>.github.io/attic-studio/watch-toys/` and `.../watch-toys/privacy/`.

All links are relative, so the site works at that address and on a custom domain later (Settings → Pages → Custom domain).

## Adding an app

Add an entry to `APPS` in `tools/build.py` (name, tagline, blurb, help and privacy text), put a 256×256 icon at `images/<slug>-icon.png`, and run the build.

## Previewing locally

`python3 -m http.server 8123` in this folder, then open http://localhost:8123.

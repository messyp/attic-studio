# Attic Studio

The website for Paul Messenger's apps: a home page, plus a support page and a privacy policy for each app. Plain HTML and one stylesheet, hosted free on GitHub Pages.

## Pages

| Page | Path | Used for |
|---|---|---|
| Home | `/` | Marketing URL (optional) |
| Watch Toys support | `/watch-toys/` | App Store Connect → Support URL |
| Watch Toys privacy | `/watch-toys/privacy/` | App Store Connect → Privacy Policy URL |

Before publishing, replace `CONTACT_EMAIL` (in `watch-toys/index.html` and `watch-toys/privacy/index.html`) with the support address.

## Publishing on GitHub Pages

1. Create a **public** repo (Pages on a free account needs public), e.g. `attic-studio`, and push this folder to `main`.
2. Repo → Settings → Pages → Build and deployment: **Deploy from a branch**, branch `main`, folder `/ (root)`.
3. After a minute the site is at `https://<username>.github.io/attic-studio/`, so the Watch Toys URLs are
   `https://<username>.github.io/attic-studio/watch-toys/` and `.../watch-toys/privacy/`.

All links are relative, so the site works at that address and on a custom domain later (Settings → Pages → Custom domain).

## Adding an app

Copy `watch-toys/` to a new folder, change the name, icon, help text and privacy details, and add a card for it on the home page.

## Previewing locally

`python3 -m http.server 8123` in this folder, then open http://localhost:8123.

"""Builds the Attic Studio site from the app list below: the home page plus a support page and a
privacy policy for each app. Edit APPS (or CONTACT) and run `python3 tools/build.py`."""
import html
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STUDIO = "Attic Studio"
CONTACT = "paulmessenger@hotmail.com"   # the support address, shown on every app's pages
UPDATED = "16 October 2026"

APPS = [
    {
        "slug": "watch-toys",
        "name": "Watch Toys",
        "tagline": "Tactile toys and tiny games for Apple Watch.",
        "blurb": "Fifteen tactile toys and tiny games for Apple Watch: steel balls, fireworks, bubble poppers, "
                 "smoke, mazes and more, all with haptics you can feel.",
        "status": None,
        "help": [
            ("What's free?", "Magnet, Orbs, Pop, Maze and Trace are free to play. One purchase, <em>Unlock all toys</em>, "
                             "unlocks the rest. Each locked toy can be tried free twice, for a minute at a time."),
            ("Restoring your purchase", "Open any locked toy and tap <em>Restore purchase</em>, signed in with the Apple "
                                        "Account you bought it with. Family Sharing is included."),
            ("Haptics feel too weak or too strong", "Open Settings on the home screen and choose Haptics (Off, Soft, Normal "
                                                     "or Strong). Each toy also has its own settings behind the gear button."),
        ],
        "privacy": [
            ("No data collected", "Watch Toys doesn't collect, store or share any personal data. There is no account, "
                                  "no analytics, no advertising and no tracking."),
            ("What stays on your watch", "Your settings and scores (such as bubbles popped and your best memory sequence) "
                                         "are kept only on your watch. Some toys use the watch's motion sensors so they can "
                                         "respond when you tilt or shake your wrist. That data stays on the watch and is "
                                         "not recorded."),
            ("Purchases", "Purchases are handled by Apple through the App Store. We never see your payment details."),
        ],
    },
    {
        "slug": "watch-pinball",
        "name": "Watch Pinball",
        "tagline": "Proper pinball on your wrist.",
        "blurb": "Three pinball tables for Apple Watch, Cosmic, Haunted and Treasure, each with its own missions, "
                 "multiball and wizard mode. Wind the plunger with the Digital Crown and nudge with a flick of the wrist.",
        "status": "Coming soon",
        "help": [
            ("Controls", "Tap or hold the left or right half of the screen to flip that side. Before each ball, wind the "
                         "plunger with the Digital Crown and let go with a tap. A firm shake of the wrist nudges the table, "
                         "but three in a few seconds is a tilt."),
            ("Can't see the flippers?", "The camera follows the ball and drops to the flippers as it falls. If a ball "
                                        "gets close to flippers that are off screen, the game slows down until they're in view."),
        ],
        "privacy": [
            ("No data collected", "Watch Pinball doesn't collect, store or share any personal data. There is no account, "
                                  "no analytics, no advertising and no tracking."),
            ("What stays on your watch", "Your settings and high scores are kept only on your watch. The game uses the "
                                         "watch's motion sensors so a shake of the wrist can nudge the table. That data "
                                         "stays on the watch and is not recorded."),
        ],
    },
    {
        "slug": "pixel-mtb",
        "name": "Pixel MTB",
        "tagline": "A pixel-art mountain bike game for iPhone.",
        "blurb": "Ride pixel-art trails through forests, an old town, a canyon and a glacier. Pump the rollers, "
                 "pop off the lips, flip and grab your way to three stars on every trail.",
        "status": "Coming soon",
        "help": [
            ("Controls", "Hold to crouch and release to pump: let go on the back of a roller to gain speed, or right on "
                         "a lip to pop higher. Drag left and right to balance, wheelie or flip in the air, and flick to "
                         "grab. Tap Retry to go back to the last checkpoint."),
            ("Your progress", "Stars, best scores and times are saved on your iPhone. Deleting the app deletes them."),
        ],
        "privacy": [
            ("No data collected by us", "Pixel MTB doesn't collect or share any personal data with us. There is no "
                                        "account, no analytics, no advertising and no tracking."),
            ("What stays on your iPhone", "Your progress, scores and settings are kept only on your iPhone."),
            ("Game Center", "If you're signed in to Game Center, your scores are sent to Apple's Game Center so they can "
                            "appear on leaderboards with your Game Center name. That's handled by Apple under Apple's own "
                            "privacy policy, and you can turn Game Center off in your iPhone's Settings."),
        ],
    },
]

LOGO = """<svg viewBox="0 0 44 44" aria-hidden="true">
        <path d="M4 40 L22 6 L40 40 Z" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>
        <circle cx="22" cy="28" r="6" fill="#d9622b"/>
        <path d="M22 22 V34 M16 28 H28" stroke="var(--bg)" stroke-width="1.6"/>
      </svg>"""


def page(title, description, up, body):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="icon" href="{up}images/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{up}style.css">
</head>
<body>
<main>
  <header class="site">
    <a class="brand" href="{up or './'}">
      {LOGO}
      <span>{STUDIO}</span>
    </a>
  </header>
{body}
  <footer>© 2026 {STUDIO}</footer>
</main>
</body>
</html>
"""


def app_head(app, up, subtitle, current):
    support = "./" if current == "support" else "../"
    privacy = "privacy/" if current == "support" else "./"
    sc = ' aria-current="page"' if current == "support" else ""
    pc = ' aria-current="page"' if current == "privacy" else ""
    status = f' <span class="tag">{app["status"]}</span>' if app["status"] else ""
    return f"""
  <div class="app-head">
    <img src="{up}images/{app['slug']}-icon.png" alt="{app['name']} icon">
    <div>
      <h1>{app['name']}</h1>
      <p>{subtitle}{status}</p>
    </div>
  </div>
  <nav class="sub">
    <a href="{support}"{sc}>Support</a>
    <a href="{privacy}"{pc}>Privacy policy</a>
  </nav>
"""


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(text)


mail = f'<a href="mailto:{CONTACT}">{CONTACT}</a>'
cards = ""
for app in APPS:
    status = f' <span class="tag">{app["status"]}</span>' if app["status"] else ""
    cards += f"""
  <section class="app">
    <img class="icon" src="images/{app['slug']}-icon.png" alt="{app['name']} icon">
    <div>
      <h2>{app['name']}{status}</h2>
      <p>{html.escape(app['blurb'])}</p>
      <div class="links">
        <a href="{app['slug']}/">Support</a>
        <a href="{app['slug']}/privacy/">Privacy policy</a>
      </div>
    </div>
  </section>
"""
write("index.html", page(STUDIO, "Little apps, made in an attic.", "", f"""
  <h1>Little apps, made in an attic.</h1>
  <p class="lede">Small, hand-made apps and games for Apple Watch and iPhone.</p>
  <div class="apps">{cards}  </div>
"""))

for app in APPS:
    help_html = "".join(f"  <p><strong>{q}:</strong> {a}</p>\n" if not q.endswith("?") else f"  <p><strong>{q}</strong> {a}</p>\n"
                        for q, a in app["help"])
    write(f"{app['slug']}/index.html", page(f"{app['name']} Support", f"Help and contact for {app['name']}.", "../",
          app_head(app, "../", app["tagline"], "support") + f"""
  <h2 id="contact">Get in touch</h2>
  <p>Questions, bugs or ideas? Email {mail}. If something isn't working, say which device and software version you're using.</p>

  <h2 id="help">Common questions</h2>
{help_html}"""))
    privacy_html = "".join(f"  <h2>{h}</h2>\n  <p>{p}</p>\n" for h, p in app["privacy"])
    write(f"{app['slug']}/privacy/index.html", page(f"{app['name']} Privacy", f"Privacy policy for {app['name']}.", "../../",
          app_head(app, "../../", "Privacy policy", "privacy") + privacy_html + f"""
  <h2>Changes and contact</h2>
  <p>If this policy changes, the new version will be posted on this page. Questions about privacy: {mail}.</p>
  <p class="small">Last updated {UPDATED}.</p>
"""))
print("built", 1 + 2 * len(APPS), "pages")

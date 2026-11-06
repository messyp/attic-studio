#!/bin/zsh
# Renders tools/badge.html to images/badge.png at 3x. Needs the site served on localhost:8123.
cd "${0:A:h}/.."
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars \
  --force-device-scale-factor=3 --window-size=330,150 --default-background-color=00000000 \
  --virtual-time-budget=4000 --screenshot="$PWD/images/badge.png" http://localhost:8123/tools/badge.html
python3 -c "
from PIL import Image
im = Image.open('images/badge.png')
im = im.crop(im.getbbox())
im.resize((640, round(640 * im.height / im.width)), Image.LANCZOS).save('images/badge.png', optimize=True)"

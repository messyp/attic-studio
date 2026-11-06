// The moth circles the bulb and keeps headbutting it. It will chase your pointer or a tap for a few
// seconds, then gets bored. Scroll away and it floats off up the page with the bulb. After a while
// it settles on the bulb and leaves you alone until you click the bulb.
(() => {
  const CHASE_FOR = 11000;     // how long it will follow you
  const IGNORE_FOR = 30000;    // how long it then ignores you
  const REST_AFTER = 30000;    // how long it flies around before settling

  const moth = document.getElementById('moth');
  const pupils = document.getElementById('pupils');
  const bulb = document.querySelector('.bulb');
  const glass = document.querySelector('.glass');
  const tink = document.getElementById('tink');
  const clamp = (v, lo, hi) => Math.min(hi, Math.max(lo, v));

  // Where the light is. It scrolls with the page, so the moth leaves with it.
  function light() {
    const r = glass.getBoundingClientRect();
    return {
      x: clamp(r.left + r.width / 2, 40, innerWidth - 40),
      y: Math.max(r.top + r.height / 2, -170),
      top: r.top,
      onScreen: r.bottom > 0 && r.top < innerHeight,
    };
  }
  // Its perch: sitting on the shoulder of the bulb.
  const perch = (l) => ({ x: l.x - 2, y: Math.max(l.top + 2, -170) });

  let x, y, vx = 0, vy = 0;

  function place(tilt) {
    const w = moth.clientWidth;
    moth.style.transform = `translate3d(${x - w / 2}px, ${y - w * .42}px, 0) rotate(${tilt}deg)`;
  }

  if (matchMedia('(prefers-reduced-motion: reduce)').matches) {
    const sit = () => { ({ x, y } = perch(light())); place(-8); };
    moth.classList.add('resting');
    sit();
    addEventListener('scroll', sit, { passive: true });
    addEventListener('resize', sit);
    return;
  }

  const start = light();
  x = start.x - 110; y = start.y + 30;

  const pointer = { x: 0, y: 0 };
  let chasing = false, chaseEnds = 0, ignoreUntil = 0;
  let resting = false, restAt = performance.now() + REST_AFTER;
  let charging = false, nextBonk = performance.now() + 2600;
  let phase = 0, last = performance.now();

  function offer(px, py, now) {
    pointer.x = px; pointer.y = py;
    if (resting || now < ignoreUntil || !light().onScreen) return;
    if (!chasing) { chasing = true; chaseEnds = now + CHASE_FOR; charging = false; }
  }
  function loseInterest(now) {
    if (!chasing) return;
    chasing = false;
    ignoreUntil = now + IGNORE_FOR;
  }

  addEventListener('pointermove', (e) => {
    if (e.pointerType === 'mouse') offer(e.clientX, e.clientY, performance.now());
  }, { passive: true });
  addEventListener('pointerdown', (e) => {
    if (!e.target.closest('.bulb')) offer(e.clientX, e.clientY, performance.now());
  }, { passive: true });
  addEventListener('scroll', () => loseInterest(performance.now()), { passive: true });

  bulb.addEventListener('click', () => {
    const now = performance.now();
    resting = false;
    moth.classList.remove('resting');
    restAt = now + REST_AFTER;
    ignoreUntil = 0;
    nextBonk = now + 1600;
    vy = -240;
  });

  function bonk(l) {
    if (!l.onScreen) return;
    tink.style.left = `${l.x + 26}px`;
    tink.style.top = `${l.y - 46}px`;
    tink.classList.remove('on');
    bulb.classList.remove('bonk');
    void tink.offsetWidth;        // restarts both animations
    tink.classList.add('on');
    bulb.classList.add('bonk');
  }
  bulb.addEventListener('animationend', () => bulb.classList.remove('bonk'));

  function frame(now) {
    const dt = Math.min(.033, (now - last) / 1000);
    last = now;
    const l = light();

    if (resting) {
      const p = perch(l);
      x = p.x; y = p.y; vx = vy = 0;
      place(-8);
      pupils.setAttribute('transform', 'translate(0 2)');
      requestAnimationFrame(frame);
      return;
    }

    if (chasing && now > chaseEnds) loseInterest(now);
    const settling = !chasing && now > restAt;
    if (settling) charging = false;
    else if (!chasing && l.onScreen && now > nextBonk) charging = true;

    const home = settling ? perch(l) : l;
    const base = chasing ? pointer : home;
    phase += dt * (2.3 + Math.sin(now * .0007));
    const radius = charging || settling ? 0
      : chasing ? 30 + 16 * Math.sin(now * .003)
      : 96 + 34 * Math.sin(now * .0011);
    const tx = base.x + Math.cos(phase) * radius * 1.25;
    const ty = base.y + Math.sin(phase * 1.7) * radius * .8;

    const pull = charging ? 34 : chasing ? 16 : 8;
    const jitter = settling ? 900 : 2600;
    vx += (tx - x) * pull * dt + (Math.random() - .5) * jitter * dt;
    vy += (ty - y) * pull * dt + (Math.random() - .5) * jitter * dt;
    const drag = Math.exp(-dt * 4.4);
    vx *= drag; vy *= drag;
    x += vx * dt; y += vy * dt;

    if (charging && Math.hypot(x - l.x, y - l.y) < 36) {
      charging = false;
      nextBonk = now + 3600 + Math.random() * 4600;
      const a = Math.atan2(y - l.y, x - l.x) + (Math.random() - .5);
      vx = Math.cos(a) * 520; vy = Math.sin(a) * 520;
      bonk(l);
    }
    if (settling && Math.hypot(x - base.x, y - base.y) < 10) {
      resting = true;
      moth.classList.add('resting');
    }

    place(clamp(vx * .05, -24, 24));

    // Eyes always on the light.
    const dx = base.x - x, dy = base.y - y, d = Math.hypot(dx, dy) || 1;
    pupils.setAttribute('transform', `translate(${dx / d * 3.4} ${dy / d * 3.4})`);
    requestAnimationFrame(frame);
  }
  place(0);
  requestAnimationFrame(frame);
})();

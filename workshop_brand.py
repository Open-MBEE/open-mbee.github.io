"""OpenMBEE workshop brand page (2027 workshop badges), derived from the OpenMBEE brand guidelines page."""

GFX = [
    ("openmbee-workshop-2027", "OpenMBEE 2027 Workshop at INCOSE IW", "Badge for the workshop at INCOSE IW 2027"),
    ("openmbee-workshop-2027-caltech", "OpenMBEE 2027 Workshop at Caltech", "Badge for the workshop at Caltech"),
]

SWATCHES = [
    ("Dk Blue", "#10052F", "16 / 5 / 47", "Backgrounds, text on light"),
    ("Lt Blue", "#64DDFA", "100 / 221 / 250", "Accents on dark backgrounds"),
    ("Grey", "#D6D6D6", "214 / 214 / 214", "Rings, text on dark"),
    ("Accent (light)", "#3E8DB5", "62 / 141 / 181", "Accent on white or light backgrounds"),
]


def make_workshop_brand():
    sw = "\n".join(f"""
    <figure class="swatch">
      <div class="chip" style="background:{hx}"></div>
      <div class="info">
        <h3>{name}</h3>
        <dl><dt>HEX</dt><dd>{hx}</dd><dt>RGB</dt><dd>{rgb}</dd><dt>Use</dt><dd>{use}</dd></dl>
        <button class="copy" type="button" data-copy="{hx}">Copy {hx}</button>
      </div>
    </figure>""" for name, hx, rgb, use in SWATCHES)

    panels = "".join(f"""
    <div class="gfx">
      <h3>{title}</h3>
      <div class="gfx-row">
        <figure class="bfig"><div class="bpanel dark"><img src="brand/{slug}-dark.svg" alt="{title}, for dark backgrounds"></div>
          <figcaption>For dark backgrounds</figcaption></figure>
        <figure class="bfig"><div class="bpanel white"><img src="brand/{slug}-light.svg" alt="{title}, for light backgrounds"></div>
          <figcaption>For white or light backgrounds</figcaption></figure>
      </div>
    </div>""" for slug, title, cap in GFX)

    assets = "\n".join(f"""
    <div class="asset">
      <div class="thumb {bg}"><img src="brand/{slug}-{v}.svg" alt="{title}, {v} version" loading="lazy"></div>
      <div class="meta"><h3>{title} ({v})</h3><p>{cap}</p>
        <p class="dl"><a href="brand/{slug}-{v}.svg" download>SVG</a><a href="brand/{slug}-{v}.png" download>PNG</a></p></div>
    </div>""" for slug, title, cap in GFX for v, bg in (("dark", "dark"), ("light", "white")))

    return f"""
<section class="brand-head">
  <div class="wrap">
    <p class="eyebrow">Workshop brand</p>
    <h1>OpenMBEE workshop brand guidelines</h1>
    <p class="intro">How to use the OpenMBEE Workshop 2027 badges, one for INCOSE IW and one for Caltech, on the web, slides and printed material. It follows the <a href="brand.html" style="color:#64DDFA">OpenMBEE brand guidelines</a>: same palette and typeface.</p>
    <ul class="brand-nav" aria-label="On this page">
      <li><a href="#badges">Workshop badges</a></li>
      <li><a href="#clear-space">Clear space and size</a></li>
      <li><a href="#colours">Colours</a></li>
      <li><a href="#typography">Typography</a></li>
      <li><a href="#usage">Usage</a></li>
      <li><a href="#downloads">Downloads</a></li>
    </ul>
  </div>
</section>

<div class="wrap">
  <section class="bsec" id="badges">
    <h2>Workshop badges</h2>
    <p class="note">The badge shows a document linked to a set of model blocks: engineering information generated from, and connected to, the model. The lettering follows the logo wordmark, with OPEN in a light weight and MBEE in bold. The two badges are identical except for the venue line. Each comes in a version for dark backgrounds and one for light backgrounds.</p>{panels}
  </section>

  <section class="bsec" id="clear-space">
    <h2>Clear space and minimum size</h2>
    <p class="note">Keep a margin of at least x around the badge, where x is one eighth of the badge width. Keep other logos, text and page edges outside it.</p>
    <div class="zone one">
      <img src="brand/openmbee-workshop-clear-space.svg" alt="OpenMBEE workshop badge with its clear space marked on all four sides" style="max-width:440px">
      <p class="label">x = 1/8 of the badge width</p>
    </div>
    <ul class="rules">
      <li>Minimum badge size: 96 px on screen, 25 mm in print. Below that the venue line stops being legible; use the OpenMBEE icon or plain text instead.</li>
      <li>Always scale proportionally.</li>
    </ul>
  </section>

  <section class="bsec" id="colours">
    <h2>Colours</h2>
    <p class="note">The three OpenMBEE primary colours, plus one accent for light backgrounds, where the light blue is too pale to read.</p>
    <div class="swatches four">{sw}
    </div>
<pre class="snippet"><code><span class="c">/* OpenMBEE workshop colours */</span>
:root {{
  --openmbee-dark-blue:  #10052F;
  --openmbee-light-blue: #64DDFA;
  --openmbee-grey:       #D6D6D6;
  --openmbee-accent:     #3E8DB5; <span class="c">/* light backgrounds only */</span>
}}</code></pre>
  </section>

  <section class="bsec" id="typography">
    <h2>Typography</h2>
    <p class="note">Use ABeeZee Regular, the OpenMBEE typeface, for workshop headings and body text. The lettering inside the badges is already converted to outlines, so it needs no font.</p>
    <div class="specimen" aria-label="ABeeZee type specimen">
      <p class="caps">OPENMBEE<br>2027 WORKSHOP</p>
      <p class="lower">at INCOSE IW &middot; at Caltech</p>
    </div>
    <p class="fontlink"><a href="https://fonts.google.com/specimen/ABeeZee" target="_blank" rel="noopener">Download ABeeZee from Google Fonts</a> <span class="muted">(open source, SIL Open Font License)</span></p>
  </section>

  <section class="bsec" id="usage">
    <h2>Usage</h2>
    <div class="bgrid">
      <div>
        <h3>Do</h3>
        <ul class="rules">
          <li>Use the badge that matches the venue you are promoting: INCOSE IW or Caltech.</li>
          <li>Use the dark version on dark or photographic backgrounds with enough contrast, and the light version on white or pale backgrounds.</li>
          <li>Write the name as <em>OpenMBEE Workshop 2027</em> in running text.</li>
        </ul>
      </div>
      <div>
        <h3>Don&rsquo;t</h3>
        <ul class="rules">
          <li>Recolour, stretch, rotate or add shadows or effects.</li>
          <li>Edit the year or venue text, or merge the two badges.</li>
          <li>Put the light version on a dark background, or the dark version on a pale one.</li>
          <li>Use the badge for other events without permission.</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="bsec" id="downloads">
    <h2>Downloads</h2>
    <p class="note">SVG files are vector and scale to any size. PNG files are 1400 px wide; the dark badges have a navy disc built in.</p>
    <div class="assets">{assets}
    </div>
    <p class="dl" style="margin-top:20px"><a href="brand/openmbee-workshop-brand-assets.zip" download>Download all workshop files (ZIP)</a></p>
    <p class="credit">These guidelines extend the <a href="brand.html">OpenMBEE brand guidelines</a>, designed by Robert Sheppard Design Limited. The workshop artwork was drawn for this site in the same palette. INCOSE and Caltech names are marks of their owners; the badge uses them only to name the venue.</p>
  </section>
</div>
"""

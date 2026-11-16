"""OpenSysML brand page (opensysml.org), derived from the OpenMBEE brand guidelines page."""

# slug, title, caption, dark-thumb, light-thumb
GFX = [
    ("opensysml-badge", "OpenSysML badge", "Primary mark"),
    ("opensysml-docgen", "DocGen Language lockup", "Wordmark lockup for the DocGen language"),
]

SWATCHES = [
    ("Dk Blue", "#10052F", "16 / 5 / 47", "Backgrounds, text on light"),
    ("Lt Blue", "#64DDFA", "100 / 221 / 250", "Accents on dark backgrounds"),
    ("Grey", "#D6D6D6", "214 / 214 / 214", "Rings, text on dark"),
    ("Accent (light)", "#3E8DB5", "62 / 141 / 181", "Accent on white or light backgrounds"),
]


def make_opensysml_brand():
    sw = "\n".join(f"""
    <figure class="swatch">
      <div class="chip" style="background:{hx}"></div>
      <div class="info">
        <h3>{name}</h3>
        <dl><dt>HEX</dt><dd>{hx}</dd><dt>RGB</dt><dd>{rgb}</dd><dt>Use</dt><dd>{use}</dd></dl>
        <button class="copy" type="button" data-copy="{hx}">Copy {hx}</button>
      </div>
    </figure>""" for name, hx, rgb, use in SWATCHES)

    panels = []
    for slug, title, cap in GFX:
        wide = slug == "opensysml-docgen"
        panels.append(f"""
    <div class="gfx">
      <h3>{title}</h3>
      <div class="gfx-row{' wide' if wide else ''}">
        <figure class="bfig"><div class="bpanel dark"><img src="brand/{slug}-dark.svg" alt="{title}, for dark backgrounds"></div>
          <figcaption>For dark backgrounds</figcaption></figure>
        <figure class="bfig"><div class="bpanel white"><img src="brand/{slug}-light.svg" alt="{title}, for light backgrounds"></div>
          <figcaption>For white or light backgrounds</figcaption></figure>
      </div>
    </div>""")

    assets = "\n".join(f"""
    <div class="asset">
      <div class="thumb {bg}"><img src="brand/{slug}-{v}.svg" alt="{title}, {v} version" loading="lazy"></div>
      <div class="meta"><h3>{title} ({label})</h3><p>{cap}</p>
        <p class="dl"><a href="brand/{slug}-{v}.svg" download>SVG</a><a href="brand/{slug}-{v}.png" download>PNG</a></p></div>
    </div>""" for slug, title, cap in GFX for v, bg, label in (("dark", "dark", "dark"), ("light", "white", "light")))

    return f"""
<section class="brand-head">
  <div class="wrap">
    <p class="eyebrow">OpenSysML brand</p>
    <h1>OpenSysML brand guidelines</h1>
    <p class="intro">How to use the OpenSysML badge and DocGen Language lockup for opensysml.org and its projects. It follows the <a href="brand.html" style="color:#64DDFA">OpenMBEE brand guidelines</a>: same palette and typeface.</p>
    <ul class="brand-nav" aria-label="On this page">
      <li><a href="#marks">Badge and lockup</a></li>
      <li><a href="#clear-space">Clear space and size</a></li>
      <li><a href="#colours">Colours</a></li>
      <li><a href="#typography">Typography</a></li>
      <li><a href="#usage">Usage</a></li>
      <li><a href="#third-party">SysML marks</a></li>
      <li><a href="#downloads">Downloads</a></li>
    </ul>
  </div>
</section>

<div class="wrap">
  <section class="bsec" id="marks">
    <h2>Badge and lockup</h2>
    <p class="note">The badge is the primary OpenSysML mark: four views of a model (requirements, functions, structure and behaviour) around an open hub, with the project name and opensysml.org. The DocGen Language lockup is used where the language itself is the subject. Each comes in a version for dark backgrounds and one for light backgrounds.</p>{"".join(panels)}
  </section>

  <section class="bsec" id="clear-space">
    <h2>Clear space and minimum size</h2>
    <p class="note">Keep a margin of at least x around the badge, where x is one eighth of the badge width. Keep other logos, text and page edges outside it.</p>
    <div class="zone one">
      <img src="brand/opensysml-clear-space.svg" alt="OpenSysML badge with its clear space marked on all four sides" style="max-width:440px">
      <p class="label">x = 1/8 of the badge width</p>
    </div>
    <ul class="rules">
      <li>Minimum badge size: 96 px on screen, 25 mm in print. Below that the small text stops being legible; use the OpenMBEE icon or plain text instead.</li>
      <li>Minimum DocGen lockup width: 200 px on screen, 50 mm in print.</li>
      <li>Always scale proportionally.</li>
    </ul>
  </section>

  <section class="bsec" id="colours">
    <h2>Colours</h2>
    <p class="note">The three OpenMBEE primary colours, plus one accent for light backgrounds, where the light blue is too pale to read.</p>
    <div class="swatches four">{sw}
    </div>
<pre class="snippet"><code><span class="c">/* OpenSysML brand colours */</span>
:root {{
  --opensysml-dark-blue:  #10052F;
  --opensysml-light-blue: #64DDFA;
  --opensysml-grey:       #D6D6D6;
  --opensysml-accent:     #3E8DB5; <span class="c">/* light backgrounds only */</span>
}}</code></pre>
  </section>

  <section class="bsec" id="typography">
    <h2>Typography</h2>
    <p class="note">Use ABeeZee Regular, the OpenMBEE typeface, for headings and body text. The lettering inside the badge and lockup is already converted to outlines, so it needs no font.</p>
    <div class="specimen" aria-label="ABeeZee type specimen">
      <p class="caps">OPENSYSML<br>DOCGEN LANGUAGE</p>
      <p class="lower">SysML v2 &middot; opensysml.org</p>
    </div>
    <p class="fontlink"><a href="https://fonts.google.com/specimen/ABeeZee" target="_blank" rel="noopener">Download ABeeZee from Google Fonts</a> <span class="muted">(open source, SIL Open Font License)</span></p>
  </section>

  <section class="bsec" id="usage">
    <h2>Usage</h2>
    <div class="bgrid">
      <div>
        <h3>Do</h3>
        <ul class="rules">
          <li>Use the dark version on dark or photographic backgrounds with enough contrast, and the light version on white or pale backgrounds.</li>
          <li>Link the badge to opensysml.org where it appears on the web.</li>
          <li>Write the name as <em>OpenSysML</em> in running text.</li>
        </ul>
      </div>
      <div>
        <h3>Don&rsquo;t</h3>
        <ul class="rules">
          <li>Recolour, stretch, rotate or add shadows or effects.</li>
          <li>Redraw the badge or change its text.</li>
          <li>Put the light version on a dark background, or the dark version on a pale one.</li>
          <li>Imply endorsement by OpenSysML or OpenMBEE without permission.</li>
        </ul>
      </div>
    </div>
  </section>

  <section class="bsec" id="third-party">
    <h2>SysML marks</h2>
    <p class="note">The SysML&reg; name and the SysML v2 logo belong to the Object Management Group (OMG) and are not covered by the OpenSysML or OpenMBEE licenses. The badge uses the words &ldquo;SysML v2&rdquo; only to name the language OpenSysML implements. Follow OMG&rsquo;s guidance before using its logo. See <a href="licenses.html">Licenses</a>.</p>
  </section>

  <section class="bsec" id="downloads">
    <h2>Downloads</h2>
    <p class="note">SVG files are vector and scale to any size. PNG files are 1400 px wide; the dark badge and lockup have a navy background built in.</p>
    <div class="assets">{assets}
    </div>
    <p class="dl" style="margin-top:20px"><a href="brand/opensysml-brand-assets.zip" download>Download all OpenSysML files (ZIP)</a></p>
    <p class="credit">These guidelines extend the <a href="brand.html">OpenMBEE brand guidelines</a>, designed by Robert Sheppard Design Limited. The OpenSysML artwork was drawn for this site in the same palette.</p>
  </section>
</div>
"""

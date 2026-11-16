"""OpenMBEE brand guidelines page (converted from OpenMBEE_brandguidelines.pdf)."""

SRC = "https://github.com/Open-MBEE/branding/blob/main/openmbee/guidelines/OpenMBEE_brandguidelines.pdf"

# name, caption, thumb background, svg basename
ASSETS = [
    ("Primary logo", "Full colour, for dark backgrounds", "dark", "openmbee-logo", "Gradient"),
    ("Horizontal logo", "Full colour, for dark backgrounds", "dark", "openmbee-logo-horizontal", "Gradient"),
    ("Icon", "Full colour, for dark backgrounds", "dark", "openmbee-icon", "Gradient"),
    ("Single colour (white)", "No gradients, for dark backgrounds", "dark", "openmbee-logo-white", "Flat"),
    ("Single colour (dark)", "No gradients, for white backgrounds only", "white", "openmbee-logo-dark", "Flat"),
    ("Icon (dark)", "Icon only, for light backgrounds", "white", "openmbee-icon-dark", "Flat"),
]
# slug, title, note, panel class for the second variant
GRAPHICS = [
    ("opensysml-badge", "OpenSysML badge",
     "Round badge for the OpenSysML project (SysML v2, opensysml.org). Use it on project pages, slides and stickers."),
    ("opensysml-docgen", "OpenSysML DocGen Language",
     "Lockup for the DocGen language: a SysML model generating documents."),
    ("openmbee-workshop-2027-caltech", "OpenMBEE 2027 Workshop at Caltech",
     "Same badge for the OpenMBEE Workshop 2027 held at Caltech."),
    ("openmbee-workshop-2027", "OpenMBEE 2027 Workshop at INCOSE IW",
     "Badge for the OpenMBEE Workshop 2027 at INCOSE IW. Use it with the workshop banner and event materials."),
]
PNG_W = {"openmbee-logo": 2000, "openmbee-logo-horizontal": 2000, "openmbee-logo-white": 2000,
         "openmbee-logo-dark": 2000, "openmbee-icon": 1024, "openmbee-icon-dark": 1024}

COLOURS = [
    ("Dk Blue", "#10052F", "100c / 90m / 65k", "16 / 5 / 47"),
    ("Lt Blue", "#64DDFA", "50c / 5y", "100 / 221 / 250"),
    ("Grey", "#D6D6D6", "14k", "214 / 214 / 214"),
]


def dl(base, svg_only=False):
    out = f'<a href="brand/{base}.svg" download>SVG</a>'
    if not svg_only:
        out += f'<a href="brand/{base}.png" download>PNG</a>'
    return f'<p class="dl">{out}</p>'


def graphics_html():
    out = []
    for slug, title, note in GRAPHICS:
        wide = slug == "opensysml-docgen"
        out.append(f"""
    <div class="gfx">
      <h3>{title}</h3>
      <p class="note">{note}</p>
      <div class="gfx-row{' wide' if wide else ''}">
        <figure class="bfig"><div class="bpanel dark"><img src="brand/{slug}-dark.svg" alt="{title}, for dark backgrounds"></div>
          <figcaption>Full colour, for dark backgrounds</figcaption>
          <p class="dl"><a href="brand/{slug}-dark.svg" download>SVG</a><a href="brand/{slug}-dark.png" download>PNG</a></p></figure>
        <figure class="bfig"><div class="bpanel white"><img src="brand/{slug}-light.svg" alt="{title}, for light backgrounds"></div>
          <figcaption>Dark ink, for white or light backgrounds</figcaption>
          <p class="dl"><a href="brand/{slug}-light.svg" download>SVG</a><a href="brand/{slug}-light.png" download>PNG</a></p></figure>
      </div>
    </div>""")
    return "\n".join(out)


def make_brand():
    swatches = "\n".join(f"""
    <figure class="swatch">
      <div class="chip" style="background:{hx}"></div>
      <div class="info">
        <h3>{name}</h3>
        <dl><dt>HEX</dt><dd>{hx}</dd><dt>RGB</dt><dd>{rgb}</dd><dt>CMYK</dt><dd>{cmyk}</dd></dl>
        <button class="copy" type="button" data-copy="{hx}">Copy {hx}</button>
      </div>
    </figure>""" for name, hx, cmyk, rgb in COLOURS)

    assets = "\n".join(f"""
    <div class="asset">
      <div class="thumb {bg}"><img src="brand/{base}.svg" alt="{name}" loading="lazy"></div>
      <div class="meta"><h3>{name}</h3><p>{cap}</p>{dl(base)}</div>
    </div>""" for name, cap, bg, base, _ in ASSETS)

    return f"""
<section class="brand-head">
  <div class="wrap">
    <p class="eyebrow">Brand guidelines</p>
    <h1>OpenMBEE brand guidelines</h1>
    <p class="intro">How to use the OpenMBEE logo, icon, colours and typeface, with the logo files ready to download.</p>
    <ul class="brand-nav" aria-label="On this page">
      <li><a href="#logo">Primary logo</a></li>
      <li><a href="#icon">Icon</a></li>
      <li><a href="#clear-zone">Clear zone</a></li>
      <li><a href="#colours">Colours</a></li>
      <li><a href="#typography">Typography</a></li>
      <li><a href="#variants">Logo variants</a></li>
      <li><a href="#graphics">Additional graphics</a></li>
      <li><a href="#downloads">Downloads</a></li>
    </ul>
  </div>
</section>

<div class="wrap">
  <section class="bsec" id="logo">
    <h2>Primary logos</h2>
    <p class="note">The logo works best against a dark background. This is the primary option.</p>
    <div class="bpanel dark stack">
      <img src="brand/openmbee-logo.svg" alt="OpenMBEE primary stacked logo" width="300">
      <img src="brand/openmbee-logo-horizontal.svg" alt="OpenMBEE horizontal logo" width="420">
    </div>
    <div class="dl"><span>Download:</span><a href="brand/openmbee-logo.svg" download>Stacked SVG</a><a href="brand/openmbee-logo-horizontal.svg" download>Horizontal SVG</a></div>
  </section>

  <section class="bsec" id="icon">
    <h2>Logo usage: using the icon</h2>
    <p class="note">An icon version can be used in isolation in certain applications, for instance social media or discreet branding where repeating the primary logo would be overkill (such as in the footer of every page in a presentation).</p>
    <div class="tiles">
      <figure class="tile">
        <div class="art"><div class="circle"><img src="brand/openmbee-icon.svg" alt="OpenMBEE icon in a circle"></div></div>
        <figcaption>Social media</figcaption>
      </figure>
      <figure class="tile">
        <div class="art"><div class="rounded"><img src="brand/openmbee-icon.svg" alt="OpenMBEE icon as an app icon"></div></div>
        <figcaption>App icon</figcaption>
      </figure>
      <figure class="tile">
        <div class="art plain"><img src="brand/openmbee-icon-dark.svg" alt="OpenMBEE icon, dark single colour"></div>
        <figcaption>Icon only (light backgrounds)</figcaption>
      </figure>
    </div>
  </section>

  <section class="bsec" id="clear-zone">
    <h2>Logo usage: clear zone</h2>
    <p class="note">To ensure the logo stands out, keep a minimum isolation zone around it.</p>
    <div class="zone">
      <img src="brand/clear-zone.svg" alt="Diagram of the logo with its clear zone marked around it">
      <p class="label">Clear zone = height of text plus space to icon</p>
    </div>
  </section>

  <section class="bsec" id="colours">
    <h2>Primary colours</h2>
    <div class="swatches">{swatches}
    </div>
<pre class="snippet"><code><span class="c">/* OpenMBEE brand colours */</span>
:root {{
  --openmbee-dark-blue:  #10052F;
  --openmbee-light-blue: #64DDFA;
  --openmbee-grey:       #D6D6D6;
}}</code></pre>
  </section>

  <section class="bsec" id="typography">
    <h2>Typography</h2>
    <p class="note">The OpenMBEE typeface is ABeeZee Regular.</p>
    <div class="specimen" aria-label="ABeeZee type specimen">
      <p class="caps">ABCDEFGHIJKLMNOPQRS<br>TUVWXYZ</p>
      <p class="lower">abcdefghijklmnopqrstuvwxyz</p>
    </div>
    <p class="fontlink"><a href="https://fonts.google.com/specimen/ABeeZee" target="_blank" rel="noopener">Download ABeeZee from Google Fonts</a> <span class="muted">(open source, SIL Open Font License)</span></p>
  </section>

  <section class="bsec" id="variants">
    <h2>Logo variants</h2>
    <p class="note">Single colour option without gradients:</p>
    <div class="bpanel dark"><img src="brand/openmbee-logo-white.svg" alt="OpenMBEE single colour white logo" width="240"></div>
    <p class="note">Single colour option without gradients, for use on a white background only:</p>
    <div class="bpanel white"><img src="brand/openmbee-logo-dark.svg" alt="OpenMBEE single colour dark logo" width="240"></div>
  </section>

  <section class="bsec" id="graphics">
    <h2>Additional graphics</h2>
    <p class="note">Project and event graphics drawn in the OpenMBEE palette (dark blue, light blue, grey). Lettering is converted to outlines, so the files look the same on any machine.</p>{graphics_html()}
    <p class="dl" style="margin-top:20px"><a href="brand/openmbee-additional-graphics.zip" download>Download all additional graphics (ZIP)</a></p>
  </section>

  <section class="bsec" id="downloads">
    <h2>Downloads</h2>
    <p class="note">SVG files are vector and scale to any size. PNG files have transparent backgrounds.</p>
    <div class="assets">{assets}
    </div>
    <p class="dl" style="margin-top:20px"><a href="brand/openmbee-brand-assets.zip" download>Download all logo files (ZIP)</a></p>
    <p class="credit">Looking for OpenSysML? See the <a href="opensysml-brand.html">OpenSysML brand guidelines</a>. Workshop badges are in the <a href="workshop-brand.html">workshop brand guidelines</a>. Brand guidelines designed by Robert Sheppard Design Limited. This page is an HTML conversion of the
    <a href="{SRC}" target="_blank" rel="noopener">original PDF</a> in the OpenMBEE branding repository.</p>
  </section>
</div>
"""

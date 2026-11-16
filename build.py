#!/usr/bin/env python3
"""Generate the static OpenMBEE site (GitHub Pages ready).

Edit NAV / PAGES below, then run:  python3 build.py
The menu is defined once and injected into every page, so nothing drifts.
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).parent
WIKI = "https://github.com/Open-MBEE/open-mbee.github.io/wiki/"

# (label, href, children). children items: (label, href, external) or None for a divider.
NAV = [
    ("Home", "index.html", None),
    ("About", None, [
        ("About Us", "about.html", False),
        ("Impacts", "impacts.html", False),
        ("Publications", WIKI + "Publications", True),
        ("Sponsors", "sponsors.html", False),
    ]),
    ("NumFOCUS Project", "numfocus.html", None),
    ("Contribute", WIKI + "Contribute", None),
    ("Participate", "participate.html", None),
    ("Projects", None, [
        ("opensysml.org", "https://opensysml.org", True),
        ("oosem.opensysml.org", "https://oosem.opensysml.org", True),
        ("flexo-mms.openmbee.org", "https://flexo-mms.openmbee.org", True),
        ("runtime.opensysml.org", "https://runtime.opensysml.org", True),
    ]),
    ("Partners", "partners.html", None),
    ("Community", None, [
        ("Slack", "https://openmbee.slack.com", True),
        ("YouTube", "https://www.youtube.com/channel/UCC4Ucy6P86ozz3pT01H7fmA", True),
        ("LinkedIn", "https://www.linkedin.com/company/openmbee/", True),
        ("Google Group", "https://groups.google.com/forum/#!forum/openmbee", True),
        ("Instagram", "https://www.instagram.com/openmbee", True),
        ("Facebook", "https://facebook.com/openmbee/", True),
        ("Twitter", "https://twitter.com/openmbee", True),
        None,
        ("Code of Conduct", "code-of-conduct.html", False),
        ("Governance", "governance.html", False),
        ("Leadership", "leadership.html", False),
        ("Licenses", "licenses.html", False),
        ("Brand Guidelines", "brand.html", False),
        ("OpenSysML Brand", "opensysml-brand.html", False),
        ("Workshop Brand", "workshop-brand.html", False),
        None,
        ("INCOSE", "https://www.omgwiki.org/MBSE/doku.php?id=mbse:ecosystems", True),
        ("NumFOCUS", "https://numfocus.org/", True),
    ]),
    ("Events", None, [
        ("workshops.openmbee.org", "https://workshops.openmbee.org", True),
    ]),
]

FAVICON = "brand/favicon.svg"

LOGO = '<img class="logo-img" src="brand/openmbee-logo-horizontal.svg" alt="OpenMBEE" width="154" height="38">'


def link(label, href, external=False):
    ext = ' target="_blank" rel="noopener"' if external else ""
    return f'<a href="{escape(href, quote=True)}"{ext}>{escape(label)}</a>'


def nav_html():
    items = []
    for label, href, children in NAV:
        if children is None:
            ext = href.startswith("http")
            items.append(f'<li>{link(label, href, False)}</li>' if not ext else f'<li>{link(label, href, False)}</li>')
            continue
        sub = []
        for c in children:
            if c is None:
                sub.append('<li class="sep" role="separator"></li>')
            else:
                sub.append(f"<li>{link(c[0], c[1], c[2])}</li>")
        items.append(
            f'<li class="has-sub"><button type="button" aria-expanded="false" aria-haspopup="true">{escape(label)}'
            f'<svg viewBox="0 0 10 6" aria-hidden="true"><path d="M1 1l4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></button>'
            f'<ul class="sub">{"".join(sub)}</ul></li>'
        )
    return "\n".join(items)


FONT_LINKS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
              '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
              '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=ABeeZee&display=swap">\n')


SYSML_LOGO_SM = '<img class="sysml-logo" src="img/sysmlv2-logo.png" alt="" width="36" height="35">'


def page(title, body, description, cls="", head_extra=""):
    full_title = "OpenMBEE — Open foundations for digital engineering" if title == "Home" else f"{title} · OpenMBEE"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(full_title)}</title>
<meta name="description" content="{escape(description, quote=True)}">
<link rel="icon" href="{FAVICON}">
<link rel="license" href="licenses.html">
{FONT_LINKS}<link rel="stylesheet" href="css/style.css">
{head_extra}</head>
<body class="{cls}">
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap bar">
    <a class="brand" href="index.html" aria-label="OpenMBEE home">{LOGO}</a>
    <button class="nav-toggle" type="button" aria-label="Menu" aria-expanded="false" aria-controls="site-nav"><span></span><span></span><span></span></button>
    <nav id="site-nav" aria-label="Main"><ul>
{nav_html()}
    </ul></nav>
  </div>
</header>
<aside class="banner" aria-label="Announcement">
  <div class="wrap banner-in">
    <span class="banner-tag">Registration and call for participation open</span>
    <p><strong>OpenMBEE Workshop 2027</strong> at <strong>INCOSE IW 2027</strong> and at <strong>Caltech</strong> (February 3&ndash;5, 2027).</p>
    <a class="banner-link" href="https://workshops.openmbee.org" target="_blank" rel="noopener">Details &rarr;</a>
  </div>
</aside>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap foot">
    <div>
      <a class="brand" href="index.html">{LOGO}</a>
      <p class="muted">Connected engineering information for a connected world.</p>
    </div>
    <div>
      <h4>Contact</h4>
      <p>openmbee (at) openmbee.org</p>
      <p class="muted small">The NumFOCUS logo is a trademark of <a href="https://numfocus.org/" target="_blank" rel="noopener">NumFOCUS</a>.</p>
      <p class="muted small sysml-note">{SYSML_LOGO_SM}<span>SysML&reg; and the SysML v2 logo are trademarks of the <a href="https://www.omg.org/" target="_blank" rel="noopener">Object Management Group</a> (OMG).</span></p>
    </div>
    <div>
      <h4>Build on OpenMBEE</h4>
      <p><a href="https://github.com/Open-MBEE" target="_blank" rel="noopener">GitHub organization</a><br>
      <a href="https://flexo-mms-deployment-guide.readthedocs.io/en/latest/index.html" target="_blank" rel="noopener">Flexo MMS docs</a><br>
      <a href="https://mms-reference-implementation.readthedocs.io/en/latest/index.html" target="_blank" rel="noopener">Execubots MMS docs</a><br>
      <a href="https://runtime.opensysml.org" target="_blank" rel="noopener">OpenSysML docs</a></p>
    </div>
  </div>
  <div class="wrap license-bar">
    <span class="lic-label">Dual licensed</span>
    <a class="lic-pill" href="https://www.apache.org/licenses/LICENSE-2.0" target="_blank" rel="noopener license">Apache License 2.0</a>
    <span class="lic-and" aria-hidden="true">+</span>
    <a class="lic-pill" href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener license">Creative Commons CC BY 4.0</a>
    <span class="lic-text">Apache 2.0 for code, CC BY 4.0 for media and content. <a href="licenses.html">License details</a></span>
  </div>
</footer>
<script src="js/site.js"></script>
</body>
</html>
"""


def inner(title, html, description, badge="", wide=False):
    body = f'<section class="page-head"><div class="wrap{" head-flex" if badge else ""}"><h1>{escape(title)}</h1>{badge}</div></section>\n<div class="wrap prose{" wide" if wide else ""}">\n{html}\n</div>'
    return page(title, body, description)


# ---------------------------------------------------------------- home
import sys
sys.path.insert(0, str(ROOT))
from home import make_home
from brand import make_brand
from opensysml_brand import make_opensysml_brand
from workshop_brand import make_workshop_brand
HOME = make_home(WIKI)

# ---------------------------------------------------------------- inner pages
def code(text):
    return '<pre class="snippet"><code>' + escape(text.strip("\n")) + '</code></pre>'


LIC_FILES = """my-repo/
  LICENSE              <- Apache License 2.0 text (code)
  LICENSE-CC-BY-4.0    <- CC BY 4.0 text (media and documentation)
  README.md            <- states which license covers what
  src/                 <- code: Apache-2.0
  docs/  images/       <- media: CC-BY-4.0"""

LIC_README = """## License

Code in this repository is licensed under the Apache License 2.0 (see LICENSE).
Documentation, images, models and other media are licensed under the
Creative Commons Attribution 4.0 International license, CC BY 4.0
(see LICENSE-CC-BY-4.0).

SPDX-License-Identifier: Apache-2.0 AND CC-BY-4.0"""

LIC_APACHE = """Copyright <year> <copyright owner>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License."""

LIC_SPDX = """// SPDX-License-Identifier: Apache-2.0            (code, short form)
<!-- SPDX-License-Identifier: CC-BY-4.0 -->          (documentation and media)"""

LIC_MEDIA = """"<title>" by <author>, <source URL>, is licensed under CC BY 4.0
(https://creativecommons.org/licenses/by/4.0/).

Short form:  (c) <year> OpenMBEE contributors, CC BY 4.0"""

LIC_META = '"license": "Apache-2.0 AND CC-BY-4.0"'

LICENSES_HTML = (
    '<p class="lead-dark">OpenMBEE prefers a <strong>dual license</strong>: the <strong>Apache License 2.0</strong> for code and the '
    '<strong>Creative Commons Attribution 4.0 (CC BY 4.0)</strong> license for media and content.</p>'
    '<div class="dual">'
    '<div class="dual-card"><span class="tag">For code</span><h2>Apache License 2.0</h2>'
    '<p>A permissive open source license with an explicit patent grant. Our preferred license for software: source code, scripts, plugins, build files and configuration.</p>'
    '<p><a href="https://www.apache.org/licenses/LICENSE-2.0" target="_blank" rel="noopener license">Read the Apache 2.0 license &rarr;</a></p></div>'
    '<div class="dual-plus" aria-hidden="true">+</div>'
    '<div class="dual-card"><span class="tag">For media and content</span><h2>Creative Commons Attribution 4.0</h2>'
    '<p>Free to share and adapt, including commercially, as long as you give appropriate credit and indicate changes. Our preferred license for documentation, models, images, diagrams, video and other media.</p>'
    '<p><a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener license">Read the CC BY 4.0 license &rarr;</a></p></div>'
    '</div>'
    '<h2>Using other licenses</h2>'
    '<p>Repositories are <strong>not required</strong> to use this standard, but every OpenMBEE repository <strong>does need to use an open source license</strong>. '
    'If a repository uses a different open source license, say so clearly in its <code>LICENSE</code> file and README.</p>'
    '<h2>Recommended marking</h2>'
    '<p>Repositories that follow the OpenMBEE standard should mark the dual license in these ways.</p>'
    '<h3>1. License files</h3>'
    '<p>Put the full text of each license in the repository root.</p>' + code(LIC_FILES) +
    '<h3>2. README</h3>'
    '<p>Add a License section that says which license covers what.</p>' + code(LIC_README) +
    '<h3>3. Source files</h3>'
    '<p>Put the standard Apache 2.0 notice at the top of each source file, or at least an SPDX identifier.</p>' + code(LIC_APACHE) + code(LIC_SPDX) +
    '<h3>4. Media and documentation</h3>'
    '<p>Credit the work where it is reused or published, ideally with title, author, source and license.</p>' + code(LIC_MEDIA) +
    '<h3>5. Package metadata</h3>'
    '<p>Use an SPDX expression in package files such as <code>package.json</code>, <code>pom.xml</code> or <code>pyproject.toml</code>. '
    'Use <code>AND</code> because different parts of the repository fall under different licenses.</p>' + code(LIC_META) +
    '<h2>Attribution</h2>'
    '<p>Please credit OpenMBEE and link to <a href="https://www.openmbee.org">openmbee.org</a> or the project repository when you reuse our work.</p>'
    '<h2>Trademarks and third-party marks</h2>'
    '<p>These licenses do not cover the OpenMBEE name and logo (see the <a href="brand.html">brand guidelines</a>), nor third-party marks such as the SysML&reg; name and SysML v2 logo (Object Management Group) or the NumFOCUS logo.</p>'
)


PAGES = {
    "about.html": inner("About Us", """
<p>OpenMBEE is an open community built around an open source Model-Based Engineering Environment. The concept is to create an integrated environment for engineering that is driven around connected models. Such environments inherently serve multiple modeling languages as well as a variety of techniques for model checking, simulation, document generation etc. The core concept is to use transclusion technology to create unified technical information with an authoritative source.</p>
<p>OpenMBEE has a variety of open source projects supporting this pursuit as well as contributed open source models. The intent is that more open source models and model libraries will flourish as the community grows. Another distinctive quality is that the open source software on OpenMBEE includes plugins or extensions for commercial tools. This supports the idea to create a unified environment based on a variety of commodity software. OpenMBEE prefers a dual license: Apache 2.0 for code and Creative Commons Attribution 4.0 (CC BY 4.0) for media and content. Anyone is welcome to contribute; there are regular meetings online and face to face.</p>
<p>OpenMBEE software provides a platform for modeling that utilizes the Model Management System (MMS) that can be accessed from rich SysML desktop clients like MagicDraw, light-weight web-based client like View Editor, mathematical computation programs like Mathematica, and any other tool that can utilize RESTful web services. It provides infrastructure for versioning, workflow management, and access control. OpenMBEE software facilitates multi-tool and multi-repository integration across engineering, computing, and management disciplines. OpenMBEE software provides the core allowing tracking relations between heterogeneous data sources in a linked data architecture using transclusion technology. System models are constructed, queried and rendered following the view and viewpoint paradigm. The novel element being the use of transclusion structures to weave a digital fabric of references between models.</p>
""", "OpenMBEE is an open community built around an open source Model-Based Engineering Environment."),

    "impacts.html": inner("Impacts", """
<p>OpenMBEE has impacted the engineering of robotic spacecraft and large telescopes, demonstrating the approach of a model-based environment for large complex systems.</p>
<ul><li>Industry</li><li>Academia</li><li>Standards</li><li>Aerospace</li></ul>
<p>OpenMBEE software and models have been applied to several international projects. COMODO has been used for the ESO Very Large Telescope, the Very Large Telescope Interferometer, and the Extremely Large Telescope (ELT) control systems, generating production quality applications.</p>
<p>The ESO model libraries for instrumentation have been used on the ELT project for design and implementation of the instrument control system.</p>
<p>MMS, VE, and the MDKs have been used for JPL flight projects such as Mars2020, Europa Clipper, Europa Lander, Mars Sample Return, and Asteroid Redirect Retrieval Mission, creating and maintaining hundreds of engineering documents from models with millions of elements.</p>
<p>The Thirty Meter Telescope Observatory has been using MMS, VE, and MDKs for creating engineering documentation from executable SysML models. SERC used MMS, VE, and MDKs for its NAVAIR surrogate pilot project for sign-off handling of documents.</p>
""", "Where OpenMBEE has been applied: JPL flight projects, ESO telescopes, the Thirty Meter Telescope and more."),

    "numfocus.html": inner("NumFOCUS Project", """
<p>As of 2020 OpenMBEE is an official <a href="https://numfocus.org/" target="_blank" rel="noopener">NumFOCUS</a> project.</p>
<p>NumFOCUS is a nonprofit organization dedicated to supporting and maintaining open source projects. NumFOCUS provides a stable, independent, and professional home for the open source projects powering contemporary scientific inquiry and business processes. They aim to ensure that funding and resources are available to sustain projects in the scientific data stack over the long haul.</p>
<p>OpenMBEE is a <a href="https://numfocus.org/sponsored-projects" target="_blank" rel="noopener">NumFOCUS Sponsored Project</a>. NumFOCUS supports these projects by connecting them to the growing NumFOCUS community, providing elevated visibility through the organization and granting additional funding.</p>
<p>Fiscally sponsored projects, such as OpenMBEE, formally become part of NumFOCUS. NumFOCUS provides a number of services for fiscally sponsored projects, including financial administration, operational and legal support. Fiscally sponsored projects are also eligible to use NumFOCUS resources and infrastructure to help raise money for the project.</p>
<p><a class="btn primary" href="https://numfocus.org/donate-to-openmbee" target="_blank" rel="noopener">Donate to OpenMBEE</a></p>
""", "OpenMBEE is an official NumFOCUS fiscally sponsored project."),

    "partners.html": inner("Partners", """
<p class="lead-dark">OpenMBEE works within a wider community of organizations and standards. These are the partners that matter most to us.</p>
<div class="partners">
  <article class="partner">
    <span class="tag">Who we aspire to support</span>
    <h2>INCOSE</h2>
    <p>The International Council on Systems Engineering is the professional home of the systems engineering community. OpenMBEE aspires to support INCOSE and its members with open source tools, models and practices for model-based systems engineering and digital engineering.</p>
    <p class="links"><a href="https://www.incose.org/" target="_blank" rel="noopener">incose.org &rarr;</a></p>
  </article>
  <article class="partner">
    <span class="tag">A key standard we follow</span>
    <h2>OMG</h2>
    <p>The Object Management Group develops the SysML v2 and KerML standards, and the SysML v2 API Services Specification, that OpenMBEE&rsquo;s OpenSysML and Flexo MMS follow. OMG is among the key standards bodies we build on.</p>
    <p class="links"><a href="https://www.omg.org/" target="_blank" rel="noopener">omg.org &rarr;</a></p>
  </article>
  <article class="partner">
    <span class="tag">Our sponsor</span>
    <h2>NumFOCUS</h2>
    <p>NumFOCUS is the nonprofit open source foundation that sponsors OpenMBEE. Since 2020 OpenMBEE has been an official NumFOCUS Sponsored Project, which connects us to the NumFOCUS community and provides visibility and additional funding.</p>
    <p class="links"><a href="https://numfocus.org/" target="_blank" rel="noopener">numfocus.org &rarr;</a> <a href="numfocus.html">OpenMBEE as a NumFOCUS project &rarr;</a></p>
  </article>
</div>
""", "OpenMBEE partners: INCOSE, OMG and NumFOCUS."),

    "participate.html": inner("Participate", """
<p class="lead-dark">OpenMBEE is an open community, and anyone is welcome to join in. Here is where to talk with us, find the tools, and get your hands on the code.</p>
<h2>General community resources</h2>
<div class="resources">
  <a class="res" href="https://groups.google.com/u/2/a/openmbee.org/g/community" target="_blank" rel="noopener"><h3>Google Group</h3><p>The community discussion list for announcements and questions.</p><span class="res-go">Join the list &rarr;</span></a>
  <a class="res" href="https://join.slack.com/t/openmbee/shared_invite/zt-32hx8t2yp-ffifkzTCY0EvelMtM~A48g" target="_blank" rel="noopener"><h3>Slack</h3><p>Real-time chat with the OpenMBEE community.</p><span class="res-go">Join Slack &rarr;</span></a>
  <a class="res" href="https://calendar.google.com/calendar/u/0?cid=Y19iMTMzNzdmMmU4Nzg2OWVhZTk0NjEyMzZkZmEyNmFkNDkwYWNjNWQ3MjE2ZjQ0ZWQ4ZWMzYzRkNzJlNTA5YmI1QGdyb3VwLmNhbGVuZGFyLmdvb2dsZS5jb20" target="_blank" rel="noopener"><h3>Community calendar</h3><p>Meetings and community events.</p><span class="res-go">View calendar &rarr;</span></a>
  <a class="res" href="https://drive.google.com/drive/folders/1-0gZYOUMf-ht56co9OumzvWxhS2C90rC" target="_blank" rel="noopener"><h3>Google Drive</h3><p>Shared community files.</p><span class="res-go">Open folder &rarr;</span></a>
  <a class="res" href="https://www.youtube.com/channel/UCC4Ucy6P86ozz3pT01H7fmA" target="_blank" rel="noopener"><h3>YouTube</h3><p>The OpenMBEE video channel.</p><span class="res-go">Watch &rarr;</span></a>
</div>
<h2>SysML developer resources</h2>
<p>OpenSysML is the SysML v2 focused part of the community. See the <a href="https://github.com/Open-MBEE/opensysml.github.io/wiki/OpenSysML-Wiki" target="_blank" rel="noopener">OpenSysML Wiki</a> for more.</p>
<div class="resources">
  <a class="res" href="https://groups.google.com/u/2/a/openmbee.org/g/opensysml" target="_blank" rel="noopener"><h3>OpenSysML Google Group</h3><p>Discussion list for OpenSysML and SysML v2 development.</p><span class="res-go">Join the list &rarr;</span></a>
  <a class="res" href="https://join.slack.com/t/openmbee/shared_invite/zt-32hx8t2yp-ffifkzTCY0EvelMtM~A48g" target="_blank" rel="noopener"><h3>Slack</h3><p>OpenSysML shares the OpenMBEE Slack workspace.</p><span class="res-go">Join Slack &rarr;</span></a>
  <a class="res" href="https://sysml-public.starforge.app/" target="_blank" rel="noopener"><h3>Starforge SysML v2 Web Modeler</h3><p>A public instance of the SysML v2 Web Modeler to try.</p><span class="res-go">Try it &rarr;</span></a>
  <a class="res" href="https://experimental.starforge.app/" target="_blank" rel="noopener"><h3>Starforge Flexo MMS instance</h3><p>An experimental Flexo MMS instance.</p><span class="res-go">Explore &rarr;</span></a>
</div>
<p><strong>Syside development licenses</strong> are offered to OpenMBEE members. See the <a href="https://github.com/Open-MBEE/open-mbee.github.io/wiki/OpenMBEE-Sponsors" target="_blank" rel="noopener">OpenMBEE Sponsors</a> page or contact openmbee (at) openmbee.org.</p>
<h2>Software developer resources</h2>
<div class="resources">
  <a class="res" href="https://github.com/Open-MBEE" target="_blank" rel="noopener"><h3>GitHub</h3><p>All OpenMBEE source code.</p><span class="res-go">Browse the code &rarr;</span></a>
  <a class="res" href="https://search.maven.org/search?q=OpenMBEE" target="_blank" rel="noopener"><h3>Maven Central</h3><p>Published Java artifacts.</p><span class="res-go">Search artifacts &rarr;</span></a>
  <a class="res" href="https://hub.docker.com/u/openmbee" target="_blank" rel="noopener"><h3>Docker Hub</h3><p>Container images for OpenMBEE services.</p><span class="res-go">View images &rarr;</span></a>
  <a class="res" href="https://github.com/Open-MBEE/open-mbee.github.io/wiki/OpenMBEE-documentation" target="_blank" rel="noopener"><h3>User guides</h3><p>OpenMBEE documentation.</p><span class="res-go">Read the guides &rarr;</span></a>
</div>
<h2>Related organizations</h2>
<p><a href="https://numfocus.org/project/openmbee" target="_blank" rel="noopener">NumFOCUS</a> &middot;
<a href="https://www.incose.org/" target="_blank" rel="noopener">INCOSE</a> &middot;
<a href="https://www.omg.org/sysml/" target="_blank" rel="noopener">OMG SysML</a> &middot;
<a href="partners.html">All partners</a></p>
""", "How to participate in OpenMBEE and OpenSysML: community channels, SysML developer resources and software developer resources.", wide=True),

    "sponsors.html": inner("Sponsors", """
<p class="lead-dark">OpenMBEE is a <a href="numfocus.html">NumFOCUS Sponsored Project</a> that supports model-based engineering through community-developed software, standards-based infrastructure and reusable engineering methods.</p>
<p>Commercial sponsors fund open source development, maintenance, documentation and community growth through sponsorship agreements, while the core project stays open and accessible. Thank you to the sponsors who help sustain OpenMBEE.</p>
<div class="sponsors">
  <article class="partner">
    <span class="tag">SysML v2 development licenses</span>
    <h2>Sensmetry / Syside</h2>
    <p>Provides SysML v2 development licenses to OpenMBEE members, on the condition that the resulting artifacts, such as code and models, are contributed to OpenMBEE under the Apache 2.0 license.</p>
    <p class="links"><a href="https://sensmetry.com/syside/" target="_blank" rel="noopener">Visit Syside &rarr;</a></p>
  </article>
  <article class="partner">
    <span class="tag">Hosted services</span>
    <h2>Planetary Utilities</h2>
    <p>Hosts free Flexo MMS and SysML v2 Web Modeler services on its infrastructure for OpenMBEE members. See the <a href="participate.html">Participate</a> page for the available resources.</p>
    <p class="links"><a href="https://planetaryutilities.com" target="_blank" rel="noopener">Visit Planetary Utilities &rarr;</a></p>
  </article>
</div>
<h2>Become a sponsor</h2>
<p>To discuss sponsoring OpenMBEE, contact openmbee (at) openmbee.org.</p>
""", "OpenMBEE sponsors: Sensmetry/Syside and Planetary Utilities, who support the NumFOCUS-sponsored OpenMBEE project."),

    "code-of-conduct.html": inner("Code of Conduct", """
<p>OpenMBEE participants and leadership both fully support a culture of professional courteous treatment and respect.</p>
<h2>OpenMBEE Code of Conduct</h2>
<p>OpenMBEE has adopted the NumFOCUS code of conduct.</p>
<p>Be kind to others. Do not insult or put down others. Behave professionally. Remember that harassment and sexist, racist, or exclusionary jokes are not appropriate for NumFOCUS.</p>
<p>All communication should be appropriate for a professional audience including people of many different backgrounds. Sexual language and imagery is not appropriate.</p>
<p>NumFOCUS is dedicated to providing a harassment-free community for everyone, regardless of gender, sexual orientation, gender identity and expression, disability, physical appearance, body size, race, or religion. We do not tolerate harassment of community members in any form.</p>
<p>Thank you for helping make this a welcoming, friendly community for all.</p>
<p>More information can be found here: <a href="https://numfocus.org/code-of-conduct" target="_blank" rel="noopener">NumFOCUS Code of Conduct</a></p>
<h2>OpenMBEE Contributor Code of Conduct</h2>
<p>OpenMBEE has adopted the Contributor Covenant. More information can be found here: <a href="https://www.contributor-covenant.org" target="_blank" rel="noopener">Contributor Covenant</a></p>
""", "OpenMBEE community code of conduct."),

    "governance.html": inner("Governance", """
<p>OpenMBEE governance document: <a href="https://docs.google.com/document/d/130xswMFFdBJ9vFUSH6iEjKcPN1NAsBdcKJAZjsTGYxM" target="_blank" rel="noopener">Governance</a></p>
""", "OpenMBEE governance."),

    "leadership.html": inner("Leadership", """
<p>The OpenMBEE Leadership Team meets regularly to guide the OpenMBEE community and manage the release of its open source products.</p>
<p>For more information, contact <a href="mailto:openmbee@gmail.com">openmbee@gmail.com</a></p>
""", "OpenMBEE leadership team."),

    "licenses.html": inner("Licenses", LICENSES_HTML, "OpenMBEE license standard: Apache 2.0 for code, CC BY 4.0 for media and content, with recommended marking.", wide=True),
}

PAGES["index.html"] = page("Home", HOME,
    "OpenMBEE: an open source model hub (MMS), tool integrations (MDKs) and an open SysML v2 implementation (OpenSysML) for digital engineering.", "home")



PAGES["brand.html"] = page("Brand Guidelines", make_brand(),
    "OpenMBEE brand guidelines: logos, icon, clear zone, colours, typography and downloadable logo files.",
    "brand-page")

PAGES["opensysml-brand.html"] = page("OpenSysML Brand Guidelines", make_opensysml_brand(),
    "OpenSysML brand guidelines: badge, DocGen Language lockup, clear space, colours, typography and downloadable files.",
    "brand-page")

PAGES["workshop-brand.html"] = page("Workshop Brand Guidelines", make_workshop_brand(),
    "OpenMBEE Workshop 2027 brand guidelines: INCOSE IW and Caltech badges, clear space, colours, typography and downloadable files.",
    "brand-page")


def main():
    for name, content in PAGES.items():
        (ROOT / name).write_text(content, encoding="utf-8")
        print("wrote", name)
    (ROOT / ".nojekyll").write_text("")


if __name__ == "__main__":
    main()

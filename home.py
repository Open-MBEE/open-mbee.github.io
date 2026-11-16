"""Front-page markup for the OpenMBEE site (imported by build.py)."""

# Architecture diagram: tools contain MDKs, which contain OpenSysML; MDKs connect to the MMS hub
HUB_SVG = """<svg class="arch" viewBox="0 0 520 412" role="img" aria-labelledby="arch-t arch-d">
<title id="arch-t">How OpenMBEE's three pillars fit together</title>
<desc id="arch-d">MDKs are embedded in the tools engineers already use, such as Cameo, VS Code and Jupyter, and each MDK carries the OpenSysML runtime. The MDKs connect to MMS, the model hub, which holds SysML, RDF and OWL, and GraphQL interfaces.</desc>
<g class="tool"><rect x="20" y="12" width="152" height="172" rx="14"/><text class="t" x="96" y="34" text-anchor="middle">Cameo</text>
  <g class="mdk"><rect x="30" y="46" width="132" height="128" rx="10"/><text class="h" x="96" y="67" text-anchor="middle">MDK</text><text class="s" x="96" y="83" text-anchor="middle">sync · DocGen</text>
    <g class="osys"><rect x="40" y="96" width="112" height="66" rx="8"/><text class="h2" x="96" y="124" text-anchor="middle">OpenSysML</text><text class="s2" x="96" y="143" text-anchor="middle">SysML v2 · KerML</text></g></g></g>
<g class="tool"><rect x="184" y="12" width="152" height="172" rx="14"/><text class="t" x="260" y="34" text-anchor="middle">VS Code</text>
  <g class="mdk"><rect x="194" y="46" width="132" height="128" rx="10"/><text class="h" x="260" y="67" text-anchor="middle">MDK</text><text class="s" x="260" y="83" text-anchor="middle">extension</text>
    <g class="osys"><rect x="204" y="96" width="112" height="66" rx="8"/><text class="h2" x="260" y="124" text-anchor="middle">OpenSysML</text><text class="s2" x="260" y="143" text-anchor="middle">SysML v2 · KerML</text></g></g></g>
<g class="tool"><rect x="348" y="12" width="152" height="172" rx="14"/><text class="t" x="424" y="34" text-anchor="middle">Jupyter</text>
  <g class="mdk"><rect x="358" y="46" width="132" height="128" rx="10"/><text class="h" x="424" y="67" text-anchor="middle">MDK</text><text class="s" x="424" y="83" text-anchor="middle">kernel</text>
    <g class="osys"><rect x="368" y="96" width="112" height="66" rx="8"/><text class="h2" x="424" y="124" text-anchor="middle">OpenSysML</text><text class="s2" x="424" y="143" text-anchor="middle">SysML v2 · KerML</text></g></g></g>
<g class="flow-l"><line x1="96" y1="184" x2="96" y2="224"/><line x1="260" y1="184" x2="260" y2="224"/><line x1="424" y1="184" x2="424" y2="224"/></g>
<g class="mms"><rect x="20" y="224" width="480" height="172" rx="18"/>
  <text class="h big" x="260" y="258" text-anchor="middle">MMS</text>
  <text class="s" x="260" y="280" text-anchor="middle">The model hub · version · branch · tag</text>
  <g class="iface"><rect x="34" y="294" width="144" height="56" rx="10"/><text x="106" y="328" text-anchor="middle">SysML</text></g>
  <g class="iface"><rect x="188" y="294" width="144" height="56" rx="10"/><text x="260" y="328" text-anchor="middle">RDF / OWL</text></g>
  <g class="iface"><rect x="342" y="294" width="144" height="56" rx="10"/><text x="414" y="328" text-anchor="middle">GraphQL</text></g>
  <text class="s dim" x="260" y="378" text-anchor="middle">REST &amp; SPARQL APIs · access control</text></g>
</svg>"""


def make_home(WIKI):
    return f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="eyebrow">Open source digital engineering</p>
      <h1>Open foundations for <span class="grad">digital engineering</span>.</h1>
      <p class="lead">OpenMBEE connects the tools, models and teams behind complex systems: a model hub to manage them, integrations to bring your tools in, and an open implementation of SysML v2, a central language for digital engineering.</p>
      <div class="cta">
        <a class="btn primary" href="#platform">Explore the platform</a>
        <a class="btn ghost" href="#get-started">Get started</a>
        <a class="btn ghost" href="https://github.com/Open-MBEE" target="_blank" rel="noopener">GitHub</a>
      </div>
      <ul class="chips"><li><a class="chip-link" href="licenses.html">Apache 2.0 + CC BY 4.0</a></li><li class="sysml"><img class="sysml-logo" src="img/sysmlv2-logo.png" alt="SysML v2" width="24" height="23">SysML v2 &amp; KerML</li><li>Version-controlled models</li><li>Open APIs</li></ul>
    </div>
    <div class="hero-art">{HUB_SVG}</div>
  </div>
</section>


<section class="block" id="platform">
  <div class="wrap">
    <p class="eyebrow dark">The platform</p>
    <h2>Three open pillars, one connected system.</h2>
    <p class="sub-lead">Use them together, or adopt them one at a time. Each is open source and built to work with the others.</p>
    <div class="pillars">
      <article class="pillar p-mms">
        <span class="badge">The hub</span>
        <h3>MMS</h3>
        <p class="role">Model Management System</p>
        <p>Version control for structured engineering data: branching, tagging, access control and open REST and SPARQL APIs, so every tool and team works from one source of truth.</p>
        <p class="links"><a href="#mms">Explore MMS →</a></p>
      </article>
      <article class="pillar p-mdk">
        <span class="badge">Development integrations</span>
        <h3>MDKs</h3>
        <p class="role">Model Development Kits</p>
        <p>Tool integrations embedded where engineers already work, such as Cameo, VS Code and Jupyter. They sync models with MMS and generate documents from models with DocGen, with the OpenSysML runtime built in.</p>
        <p class="links"><a href="#mdks">Explore MDKs →</a></p>
      </article>
      <article class="pillar p-lang">
        <img class="sysml-logo corner" src="img/sysmlv2-logo.png" alt="SysML v2" width="72" height="70">
        <span class="badge">Language foundations</span>
        <h3>OpenSysML</h3>
        <p class="role">Open source SysML v2</p>
        <p>An open implementation of SysML v2 and KerML (parser, runtime, language server, notebook kernel and client libraries) built into the MDKs, so every tool shares a central, standard language for digital engineering.</p>
        <p class="links"><a href="#opensysml">Explore OpenSysML →</a></p>
      </article>
    </div>
  </div>
</section>

<section class="block alt" id="mms">
  <div class="wrap">
    <p class="eyebrow dark">Pillar 1 · MMS, the hub</p>
    <h2>One hub. Every model, version and tool.</h2>
    <p class="sub-lead">Digital engineering means many tools and teams touching the same system definition. MMS is the layer that keeps them consistent, traceable and open.</p>
    <div class="cards">
      <article class="card"><div class="ico">⑂</div><h3>Git for engineering data</h3><p>Commit, branch and tag model data with full CRUD over a versioned repository, so you can see what changed, compare it, and return to any baseline.</p></article>
      <article class="card"><div class="ico">⇄</div><h3>Open, standard APIs</h3><p>RESTful web services for model access. The Flexo architecture adds SPARQL and Graph Store Protocol endpoints, and a service implementing the OMG SysML v2 API.</p></article>
      <article class="card"><div class="ico">⌘</div><h3>Works with your tools</h3><p>Desktop SysML clients like MagicDraw, the web-based View Editor, Mathematica, Python and Java clients, or anything that can call a web service.</p></article>
      <article class="card"><div class="ico">❏</div><h3>Documents and notebooks</h3><p>Generate documents from models with the view and viewpoint approach, and store and search Jupyter Lab notebooks alongside the model.</p></article>
      <article class="card"><div class="ico">◈</div><h3>Graph-native models</h3><p>Flexo MMS stores models as RDF graphs and can diff and manage anything expressible as RDF, not only a single vendor's model format.</p></article>
      <article class="card"><div class="ico">⛨</div><h3>Controlled and deployable</h3><p>Access control and multi-tenant collaboration, LDAP-capable authentication in Flexo, and sample Docker Compose and Kubernetes deployments to run it yourself.</p></article>
    </div>
  </div>
</section>

<section class="block" id="flavors">
  <div class="wrap">
    <p class="eyebrow dark">MMS architectures</p>
    <h2>Pick the MMS that fits your data.</h2>
    <p class="sub-lead">Flexo is built for RDF graphs; Execubots is the long-supported JSON-document implementation. Flexo MMS is not a drop-in replacement for Execubots MMS.</p>
    <div class="duo">
      <article class="panel feature">
        <span class="tag">Graph-native</span>
        <h3>Flexo MMS</h3>
        <p>Models as RDF graphs, with SPARQL and Graph Store Protocol endpoints for loading, updating and querying, plus management endpoints for orgs, repos and branches. Includes auth and store services.</p>
        <ul><li>Native RDF, graph diff</li><li>Flexo SysML v2 service (beta), an implementation of the OMG SysML v2 API Services Specification</li><li>Docker Compose and Kubernetes samples</li></ul>
        <p class="links"><a href="https://flexo-mms-deployment-guide.readthedocs.io/en/latest/index.html" target="_blank" rel="noopener">Documentation →</a> <a href="https://github.com/Open-MBEE/flexo-mms-deployment" target="_blank" rel="noopener">Deployment repo →</a></p>
      </article>
      <article class="panel">
        <span class="tag muted-tag">Long-term support</span>
        <h3>Execubots MMS</h3>
        <p>Models as JSON documents behind RESTful web services for CRUD, branching and tagging, built from modular Spring components you can pick and choose.</p>
        <ul><li>Reference implementation (MMSRI) for a ready-made REST API</li><li>Jupyter notebook storage and search</li><li>Python client on PyPI (mms-python-client)</li></ul>
        <p class="links"><a href="https://mms-reference-implementation.readthedocs.io/en/latest/index.html" target="_blank" rel="noopener">Documentation →</a> <a href="https://github.com/Open-MBEE/exec-mmsri" target="_blank" rel="noopener">Source →</a></p>
      </article>
    </div>
  </div>
</section>

<section class="block alt" id="mdks">
  <div class="wrap split">
    <div>
      <p class="eyebrow dark">Pillar 2 · MDKs, development integrations</p>
      <h2>Bring your tools to the hub.</h2>
      <p>Model Development Kits are tool-specific integrations. Their primary purposes are to sync models with the MMS and to implement the DocGen language, which lets modelers dynamically generate documents from models using the view and viewpoint concept.</p>
      <p>MDKs are embedded where engineers already work, such as Cameo, a VS Code extension and a Jupyter kernel, and they carry the OpenSysML runtime with them. Engineers keep working in the language and tool they prefer, while their work is versioned, shared and documented across other tools.</p>
      <p class="links"><a href="https://github.com/Open-MBEE/exec-cameo-mdk" target="_blank" rel="noopener">Cameo MDK on GitHub →</a> <a href="impacts.html">MDKs on flight projects →</a></p>
    </div>
    <ul class="points">
      <li><h3>Sync with MMS</h3><p>Push and pull model data between your modeling tool and the versioned repository.</p></li>
      <li><h3>Documents from models</h3><p>DocGen turns model content into engineering documents, so documents stay current as the model changes.</p></li>
      <li><h3>Next generation: MDK2</h3><p>The OpenSysML Runtime Environment and Development Kit (REDK) is the second generation of the MDK, with a Cameo plugin in its repository.</p></li>
    </ul>
  </div>
</section>

<section class="block" id="opensysml">
  <div class="wrap">
    <p class="eyebrow dark">Pillar 3 · OpenSysML, language foundations</p>
    <div class="sysml-head"><img class="sysml-logo" src="img/sysmlv2-logo.png" alt="SysML v2" width="84" height="82"><h2>SysML v2: a central language for digital engineering.</h2></div>
    <p class="sub-lead">OpenSysML is an open source implementation of SysML v2 and KerML, written in Go. It gives tools, services and engineers a shared, executable definition of system structure, behavior and requirements.</p>
    <div class="cards">
      <article class="card"><div class="ico">⌥</div><h3>Parser and libraries</h3><p>A parser based on the OMG grammars, with the OMG standard library and OpenSysML extension libraries.</p></article>
      <article class="card"><div class="ico">▶</div><h3>Executable runtime</h3><p>Instantiate parts, evaluate expressions with units, run actions and state machines, and check requirements.</p></article>
      <article class="card"><div class="ico">&gt;_</div><h3>Command line and REPL</h3><p>Model, execute and check interactively from the <code>sysml</code> command.</p></article>
      <article class="card"><div class="ico">✎</div><h3>Language server</h3><p>Diagnostics, hover, go-to-definition, completion and formatting, with a VS Code extension.</p></article>
      <article class="card"><div class="ico">❖</div><h3>Jupyter kernel</h3><p>Run SysML cells in notebooks alongside analysis and documentation.</p></article>
      <article class="card"><div class="ico">⇆</div><h3>Client libraries and service</h3><p>Clients for Go, Python, TypeScript, Java, Rust, Julia and MATLAB/Octave, plus a gRPC service.</p></article>
    </div>
    <p class="links after"><a href="https://github.com/Open-MBEE/OpenSysML" target="_blank" rel="noopener">OpenSysML on GitHub →</a> <a href="https://runtime.opensysml.org" target="_blank" rel="noopener">Runtime documentation →</a> <a href="https://github.com/Open-MBEE/toaster" target="_blank" rel="noopener">Executable tutorial →</a> <a href="https://flexo-mms.openmbee.org" target="_blank" rel="noopener">Flexo MMS →</a></p>
  </div>
</section>

<section class="block alt">
  <div class="wrap">
    <p class="eyebrow dark">How it fits together</p>
    <h2>From language to finished deliverable.</h2>
    <ol class="flow">
      <li><span class="n">1</span><h3>Describe</h3><p>Capture system structure, behavior and requirements in SysML v2, with OpenSysML tooling to parse, run and check it.</p></li>
      <li><span class="n">2</span><h3>Integrate</h3><p>MDKs and clients connect your modeling tools to the hub, keeping tools and repository in step.</p></li>
      <li><span class="n">3</span><h3>Manage</h3><p>MMS versions every change, supports branching and tagging, and controls who can see and edit what.</p></li>
      <li><span class="n">4</span><h3>Use</h3><p>Generate documents, run analyses, build apps and dashboards from the same governed data through open APIs.</p></li>
    </ol>
  </div>
</section>

<section class="block dark-band" id="get-started">
  <div class="wrap qs">
    <div>
      <p class="eyebrow">Get started</p>
      <h2>Start with the piece you need.</h2>
      <p class="sub-lead light">Run an MMS hub on your own machine with Docker Compose, try the SysML v2 API service, or explore the OpenSysML runtime and language tooling.</p>
      <div class="cta">
        <a class="btn primary" href="https://flexo-mms-deployment-guide.readthedocs.io/en/latest/local_quickstart.html" target="_blank" rel="noopener">Flexo MMS quickstart</a>
        <a class="btn ghost light" href="https://github.com/Open-MBEE/flexo-mms-sysmlv2/tree/develop/docker-compose" target="_blank" rel="noopener">Flexo SysML v2 beta</a>
        <a class="btn ghost light" href="https://github.com/Open-MBEE/OpenSysML" target="_blank" rel="noopener">Try OpenSysML</a>
      </div>
    </div>
    <pre class="code" aria-label="Clone the deployment repository"><code><span class="c"># MMS: get the sample deployment files</span>
git clone https://github.com/Open-MBEE/flexo-mms-deployment
cd flexo-mms-deployment/docker-compose

<span class="c"># then follow the quickstart for env configs and the init file</span></code></pre>
  </div>
</section>

<section class="block">
  <div class="wrap">
    <p class="eyebrow dark">Around the platform</p>
    <h2>More from the OpenMBEE ecosystem.</h2>
    <div class="cards three">
      <article class="card"><h3><a href="https://github.com/Open-MBEE/sysmlv2-web-modeler" target="_blank" rel="noopener">SysML v2 Web Modeler</a></h3><p>A standalone Java web service for SysML v2 graphical rendering and textual editing against a SysML v2 API backend.</p></article>
      <article class="card"><h3><a href="{WIKI}Models-and-Cookbooks" target="_blank" rel="noopener">OpenSE Cookbook</a></h3><p>A compendium of best practices and lessons learned for performing engineering tasks with modeling languages and tools.</p></article>
      <article class="card"><h3><a href="https://github.com/Open-MBEE/toaster" target="_blank" rel="noopener">Toaster tutorial</a></h3><p>An executable tutorial on recursive system decomposition with SysML v2 and OpenSysML.</p></article>
    </div>
  </div>
</section>

<section class="block alt">
  <div class="wrap wild">
    <div>
      <p class="eyebrow dark">In the wild</p>
      <h2>Proven on some of the hardest systems built.</h2>
      <p>MMS, View Editor and the MDKs have been used on JPL flight projects including Mars 2020, Europa Clipper, Europa Lander and Mars Sample Return, creating and maintaining hundreds of engineering documents from models with millions of elements.</p>
      <p>The Thirty Meter Telescope SysML model is an industrial-scale application of OpenMBEE, used for system-level behavior simulation and state-dependent power and mass roll-ups, built with an extension of INCOSE's Object Oriented Systems Engineering Method (OOSEM).</p>
      <p class="links"><a href="impacts.html">See more impacts →</a></p>
    </div>
    <aside class="numfocus">
      <h3>Proud recipient of NumFOCUS fiscal support</h3>
      <p>OpenMBEE is a fiscally sponsored project of <a href="https://numfocus.org/" target="_blank" rel="noopener">NumFOCUS</a>, a nonprofit dedicated to supporting the open source scientific computing community.</p>
      <a class="btn primary small" href="https://numfocus.org/donate-to-openmbee" target="_blank" rel="noopener">Support OpenMBEE</a>
    </aside>
  </div>
</section>

<section class="block join">
  <div class="wrap center">
    <h2>Build the digital thread with us.</h2>
    <p class="sub-lead">Anyone is welcome to contribute. There are regular meetings online and in person.</p>
    <div class="cta center">
      <a class="btn primary" href="{WIKI}Contribute" target="_blank" rel="noopener">Contribute</a>
      <a class="btn ghost" href="participate.html">Participate</a>
      <a class="btn ghost" href="https://openmbee.slack.com" target="_blank" rel="noopener">Join Slack</a>
    </div>
  </div>
</section>
"""

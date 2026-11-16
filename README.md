# OpenMBEE website (GitHub Pages)

Static site, no framework or build tooling needed to host it.

## Deploy
1. Copy these files to the root of the Pages repo (for example `Open-MBEE/open-mbee.github.io`, branch `master`), or to a new repo.
2. Repo Settings → Pages → Deploy from a branch → select the branch and `/ (root)`.
3. Custom domain: add a `CNAME` file containing the hostname (the current site's CNAME file is 16 bytes, which matches `www.openmbee.org`; confirm before overwriting it) and set the domain in Pages settings.

## Edit
- The menu and all page content live in `build.py`. After editing, run `python3 build.py` to regenerate the `.html` files (standard library only).
- Styles: `css/style.css`. Menu behavior: `js/site.js`.

## Still to add from the existing site
- Real logo (`images/openmbee-logo.svg`) and favicon set: the new site uses a simple drawn wordmark and an inline favicon. Swap the `LOGO` / `FAVICON` constants in `build.py` when you have the files.
- Menu items that point to the GitHub wiki (Publications, Sponsors, Contribute, Participate, Models & Cookbooks) are unchanged.

## Brand guidelines page

`brand.html` is an HTML conversion of the OpenMBEE brand guidelines PDF (content lives in `brand.py`).
Logo artwork is in `brand/` (SVG extracted from the PDF's vector art, plus PNG exports and `openmbee-brand-assets.zip`).
It appears under Community > Brand Guidelines. The ABeeZee typeface is loaded from Google Fonts on that page only;
to self-host it, drop the font files into `fonts/` and replace `BRAND_FONT` in `build.py` with an `@font-face` rule.

## Licensing

The site states the OpenMBEE license preference: Apache 2.0 for code and CC BY 4.0 for media and content, with recommended marking on `licenses.html` (footer bar, `licenses.html`, home hero chip). Edit `build.py` to change the CC version or wording.

## Additional brand graphics

`graphics.py` generates the OpenSysML badge, OpenSysML DocGen Language lockup and OpenMBEE 2027 Workshop badge
(dark and light versions, SVG) into `brand/`; PNG exports come from `rsvg-convert -w 1400`. Lettering is outlined from Inter
because ABeeZee was not available when they were drawn: point `FONT_DIR`/`FONTS` at ABeeZee and re-run for exact brand lettering.

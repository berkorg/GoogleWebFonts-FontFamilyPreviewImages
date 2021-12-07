# Google Web Fonts - Font Family Preview Images

This repo contains images that are representations of all the different Google
Fonts. We needed this for our app [Stencil](https://getstencil.com), since we
allow our users to search through Google Fonts (via their API). But we
(obviously) wanted/needed to provide them with a preview of what the font looked
like.

We could have loaded the fonts into memory and then shown those, but that didn't
seem ideal.

### Note
If you're interested in a hosted version of the screenshot you see below
(allowing your users to trigger a modal, and a button-click bubbling up an event
that contains the URL of the corresponding `woff2` file), please let me know:
[onassar@gmail.com](mailto:onassar@gmail.com)

### Screenshot of how our app uses the images in this repo:
![](https://i.imgur.com/4bm2ixQ.png)

### Why are there so many files?
While Google Fonts currently provides thousands of different font variations,
there are many-more actual images. This is because Google Fonts routinely
updates fonts from one version to another (eg. v5 to v6). We then re-render the
images to ensure the preview we show our users is accurate.

I've decided to leave those files in the repo for posterity's sake: you never
know what people will need :)

### Sizes
At the moment, I'm only providing preview images that have a `font-size` value
of `48px`. The width respects the native width of the font. To ensure a sharp
display, I'd suggest you hardcode the preview thumb at a maximum height of
`24px`.

### Naming convention of files:
Two examples: `ABeeZee-400.v10.png` and `Cabin-400italic.v10.png`  
The format is pretty straight-forward:
- The font name (non-hyphens, non-alphabetic and non-numeric characters are removed)
- A dash (`-`)
- The font-weight
- If the font is an italicized version, after the font, the word `italic` is added
- The version number, preceded by the letter `v`

The regular expression I use to strip out the name-characters is:
`/[^A-Za-z0-9\-]/`

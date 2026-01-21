# Sherpa Documentation

This is a minimal Jekyll project configured to build on Netlify.

## Local development

Make sure you have Ruby and Bundler installed, then run:

```bash
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000 in your browser.

## Deploying to Netlify

1. Push this folder to a Git repository (or make it the root of a new repo).
2. Create a new site on Netlify from that repository.
3. In Netlify build settings:
   - **Build command**: `bundle exec jekyll build`
   - **Publish directory**: `_site`
4. Deploy the site.


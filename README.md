# Sherpa Documentation

This Jekyll project contains Sherpa documentation written in Markdown and is configured to build on GitHub Pages.

## Local development

### Editing the Markdown files

Clone the repository and create a branch:

```bash
git clone https://github.com/EscapeTechnology/sherpa-docs.git
cd sherpa-docs
git checkout -b my-branch
```

You can do a similar thing using VSCode or SourceTree if you are more comfortable with a GUI.

Once you have created a branch, you can now edit the Markdown files. When you have finished, push your changes to GitHub and the publicly available site will automatically rebuilt when you your changes have been approved and merged into the main branch. 

### Building the site

If you want to preview your changes locally you can build the site and run a local server:

Make sure you have Ruby and Bundler installed, then run:

```bash
bundle install
bundle exec jekyll serve --watch
```

Then open http://localhost:4000/sherpa-docs/ in your browser.

When you make changes to the Markdown files the site will automatically rebuild.

## Setting up GitHub Pages

Below is a very brief guide on setting up GitHub Pages for this repository:

1. Go to the repository for this documentation site.
2. In the repository settings, navigate to **Pages**.
3. Under **Build and deployment > Source**, select **GitHub Actions**.
4. The site will automatically build and deploy whenever you push to the `main` branch.

You only have to do the above once.

The public site will be available at https://escapetechnology.github.io/sherpa-docs/



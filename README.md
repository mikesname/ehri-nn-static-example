EHRI National Node website resources
====================================

This repository contains resources for generating a website for
an EHRI National Node.

The static site on Github should be republished automatically when
pushed to `main`, via the `pelican.yml` workflow in the .github
directory. However, to do some manually run:

    pelican content -s publishconf.py -o output
    ghp-import output -b gh-pages
    git push origin gh-pages

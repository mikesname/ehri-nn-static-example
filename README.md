EHRI National Node website resources
====================================

This repository contains resources for generating a website for
an EHRI National Node.

To publish to a `gh-pages` branch run:

    pelican content -s publishconf.py -o output
    ghp-import output -b gh-pages
    git push origin gh-pages

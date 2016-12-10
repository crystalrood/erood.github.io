#!/bin/bash

# sets the working directory to the current directory
cd "$(dirname "$0")"

# converts all iPython Notebook files to basic html
for f in *.ipynb; do ipython nbconvert --to html --template basic $f; done

for f in *.html; do python convert_nb_to_post.py $f; done

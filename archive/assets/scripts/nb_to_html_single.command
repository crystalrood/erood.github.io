#!/bin/bash

# By Chris Albon
# March 4, 2015

# This script converts a single iPython Notebook files to basic html.

cd "$(dirname "$0")"

ipython nbconvert --to html --template basic EXAMPLE.ipynb


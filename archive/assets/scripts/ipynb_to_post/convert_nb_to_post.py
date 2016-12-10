#!/usr/bin/python
from bs4 import BeautifulSoup
import sys

filename = str(sys.argv[1])

header_before_title = '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">'
header_title = '<title>REPLACE_ME</title>'
header_after_header = '<meta name="description" content=""><meta name="viewport" content="width=device-width, initial-scale=1.0"><link href="../css/normalize.css" rel="stylesheet" media="all"> <link href="../css/styles.css" rel="stylesheet" media="all">     <link href="assets/css/notebooks.css" rel="stylesheet" media="all">
    <link href='https://fonts.googleapis.com/css?family=Crimson+Text' rel='stylesheet' type='text/css'> <link href=\'http://fonts.googleapis.com/css?family=Source+Serif+Pro:400,700\' rel=\'stylesheet\' type=\'text/css\'> <!--[if lt IE 9]><script src="js/html5shiv-printshiv.js" media="all"></script><![endif]--> </head> <body> <header role="banner"> <div class="row"> <h2><a href="http://chrisalbon.com">Chris Albon</a></h2> <nav role="navigation"> <a href="html/miscellaneous/about.html">About</a> | <a href="https://github.com/chrisalbon">GitHub</a> | <a href="https://twitter.com/chrisalbon">Twitter</a> </nav> </div> </header> <div class="wrap"> <main role="main"> <div class="notebook"> <!-- end of header section --> <!-- PASTE IPYTHON NOTEBOOK BELOW THIS LINE -->'
footer = '<!-- PASTE IPYTHON NOTEBOOK ABOVE THIS LINE --> <!-- start of footer section --> </div> </main> </div> <footer role="contentinfo"> Copyright &copy; Chris Albon, <time datetime="2015">2015</time> </footer> <!-- Load Google Analytics --> <script> (function(i,s,o,g,r,a,m){i[\'GoogleAnalyticsObject\']=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o), m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m) })(window,document,\'script\',\'//www.google-analytics.com/analytics.js\',\'ga\'); ga(\'create\', \'UA-66582-32\', \'auto\'); ga(\'send\', \'pageview\'); </script> <!-- End of Google Analytics --> <!-- Loading mathjax macro --> <!-- Load mathjax --> <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML"></script> <!-- MathJax configuration --> <script type="text/x-mathjax-config"> MathJax.Hub.Config({tex2jax: {inlineMath: [ [\'$\',\'$\'], ["\\(","\\)"] ], displayMath: [ [\'$$\',\'$$\'], ["\\[","\\]"] ], processEscapes: true, processEnvironments: true }, // Center justify equations in code and markdown cells. Elsewhere // we use CSS to left justify single line equations in code cells. displayAlign: \'center\', "HTML-CSS": {styles: {\'.MathJax_Display\': {"margin": 0}}, linebreaks: { automatic: true } } }); </script> <!-- End of mathjax configuration --> </body> </html>'

# Open notebook html file as f
with open(filename, "r") as f:
    # Read file as notebook
    notebook = f.read()
    # convert the notebook file as soup
    soup = BeautifulSoup(notebook)
    # Find the title of the notebook
    title = soup.find("h1").text.strip('¶')
    # Replace the post's placeholder title with the notebook's title
    header_title = header_title.replace('REPLACE_ME', title)
# Close the file
f.close()

# Open the file
with open(filename, 'w') as modified:
    # Wipe it clean and rewrite everything in the desired order
    modified.write(header_before_title + header_title + header_after_header + notebook + footer)
# Close the file
f.close()


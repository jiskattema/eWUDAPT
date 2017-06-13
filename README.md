# eWUDAPT portal

This is basic website made for the lorentz center workshop [eWUDAPT: Bringing eScience to Urban Climate Mapping and Modelling](https://www.lorentzcenter.nl/lc/web/2017/892/info.php3?wsid=892&venue=Snellius)

![eWUDAPT poster](content/images/poster.png?raw=true "Poster")

## Installation

1. set up a virutal environment for the python packages
```bash
mkdir eWUDAPT && cd eWUDAPT
virtualenv .
. env/bin/activate
```

2. install pelican and markdown and dependencies
```bash
pip install -r requirements.txt
```

3. install the theme
```bash
git clone https://github.com/yuex/pelican-chameleon theme
```

4. Build the static website
```bash
make html
```

5. The output directory now contains the full website. You can host it using your preferred server, or for development use the built-in webserver:
```bash
cd output
python -m pelican.server
``e

# Plots

Plots should be placed in the content/images directory.
Naming scheme: ```usecase??_stage?_variable.jpg```

# Quick links

* [Markdown primer](https://daringfireball.net/projects/markdown/basics)

* [Adding images to pelican blog posts in markdown](http://docs.getpelican.com/en/3.6.3/content.html#linking-to-static-files)

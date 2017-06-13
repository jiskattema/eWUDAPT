# eWUDAPT portal

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
```

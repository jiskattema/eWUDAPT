#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jisk Attema'
SITENAME = u'eWUDAPT'
SITEURL = 'eWUDAPT' # for hosting on gh-pages

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'

# using https://github.com/yuex/pelican-chameleon
THEME = './theme'

# see https://bootswatch.com/united/
BS3_THEME = 'https://bootswatch.com/united/bootstrap.min.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
        )

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

MENUITEMS = [
    ('Home', '/introduction.html'),
    ('Models', [
        ('Output', '/output.html'),
        ('Model1', '/models/model01.html'),
        ]),
    ('Usecase1', [
        ('Description', '/usecases/usecase01.html'),
        ('Stage 1', '/plots?usecase=01&stage=1'),
        ('Stage 2', '/plots?usecase=01&stage=2'),
        ('Stage 3', '/plots?usecase=01&stage=3'),
        ]),
    ('Usecase2', [
        ('Description', '/usecases/usecase02.html'),
        ('Stage 1', '/plots?usecase=02&stage=1'),
        ('Stage 2', '/plots?usecase=02&stage=2'),
        ('Stage 3', '/plots?usecase=02&stage=3'),
        ]),
    ('Archives', [
        ('Tags', '/tags.html'),
        ('Categories', '/categories.html'),
        ('Chronological', '/archives.html'),
        ]),
    ('Contact', [
        ('Email', 'mailto: my@email.to'),
        ('Github', 'http://url-to-github-page'),
        ]),
    ]

DEFAULT_PAGINATION = 10

# these directories are copied directly to the output dir
STATIC_PATHS = ['images', 'docs']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

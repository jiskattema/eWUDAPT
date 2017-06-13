#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jisk Attema'
SITENAME = u'eWUDAPT'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'

# using https://github.com/yuex/pelican-chameleon
THEME = './theme'

# see https://bootswatch.com/united/
BS3_THEME = 'http://bootswatch.com/united/bootstrap.min.css'

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
         ('You can modify those links in your config file', '#'),)

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
        ('Description', '/usecase01'),
        ('Stage 1', '/usecase01/stage1'),
        ('Stage 2', '/usecase01/stage2'),
        ('Stage 3', '/usecase01/stage3'),
        ]),
    ('Usecase2', [
        ('Description', '/usecase02'),
        ('Stage 1', '/usecase02/stage1'),
        ('Stage 2', '/usecase02/stage2'),
        ('Stage 3', '/usecase02/stage3'),
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

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

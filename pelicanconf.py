#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Martin Fitzpatrick'
AUTHOR_EMAIL = u'martin.fitzpatrick@gmail.com'
SITENAME = u'Martin Fitzpatrick'
SITESUBTITLE = u' Bioinformatics | Immunology | Python | Web '
SITEURL = 'http://martinfitzpatrick.name'

FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/atom.xml'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

PLUGIN_PATH = '/home/spenglr/pelican-plugins'
PLUGINS = [
        'gravatar',
        'related_posts',
        'pelican_youtube',
#        'pelican.plugins.github_activity',
#        'pelican.plugins.gzip_cache',   
        'sitemap',
        ]
        

FILES_TO_COPY = ( ('extra/robots.txt', 'robots.txt'),
                  ('extra/favicon.ico', 'favicon.ico'),
                  ('extra/.htaccess', '.htaccess'), )

# Blogroll
LINKS =  (
            ('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
            ('Python.org', 'http://python.org'),
        )

# Social widget
SOCIAL = (
          ('RSS', 'rss', '%s/%s' % (FEED_DOMAIN, FEED_ATOM) ),
#          ('Facebook', 'facebook', 'https://facebook.com/research.abl.es'),
          ('Google+', 'google-plus', 'https://plus.google.com/115539678583643563408/?rel=author'),
          ('LinkedIn', 'linkedin', 'uk.linkedin.com/in/martinfitzp'),
          ('ORCID', 'orcid', 'http://orcid.org/0000-0002-0695-1988'),
          ('Twitter', 'twitter', 'https://twitter.com/mfitzp'),
          ('ResearchGate', 'researchgate', 'https://www.researchgate.net/profile/Martin_Fitzpatrick/'),
          ('Github', 'github', 'https://github.com/mfitzp'),
        )

DEFAULT_PAGINATION = 10

TYPOGRIFY = True
DISPLAY_CATEGORIES_ON_MENU = True
GITHUB_ACTIVITY_FEED = 'https://github.com/mfitzp.atom'


SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'monthly',
        'pages': 'monthly'
    }
}


ARTICLE_URL = 'article/{slug}'
ARTICLE_SAVE_AS = 'article/{slug}.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}.html'


DISQUS_SITENAME = 'golifescience'
GOOGLE_ANALYTICS = 'UA-341253-5'
GITHUB_URL = 'https://github.com/mfitzp'

TWITTER_USERNAME = 'mfitzp'

THEME = 'theme'

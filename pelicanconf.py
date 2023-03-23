import datetime

AUTHOR = 'EHRI'
SITENAME = 'EHRI-UK'
SITEURL = ''
COUNTRY_CODE = 'UK'
SITE_TITLE = 'United Kingdom'
COPYRIGHT_YEAR = datetime.datetime.now().year
COPYRIGHT_HOLDER = "EHRI Consortium"

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ('About', 'about'),
    ('Partners', 'partners'),
    ('Fellowships & Training', 'training'),
    ('Services', 'services'),
    ('Contact', 'contact'),
    )

DEFAULT_PAGINATION = False

THEME = 'ehri-theme'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

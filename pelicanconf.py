import datetime

AUTHOR = 'EHRI'
SITENAME = 'EHRI-UK'
SITEURL = ''
COUNTRY_CODE = 'UK'
SITE_TITLE = 'The UK National Holocaust Research Infrastructure'
COPYRIGHT_YEAR = datetime.datetime.now().year

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ('Home', ''),
    ('About EHRI-UK', 'about'),
    ('EHRI Services', 'services'),
    ('Contact Us', 'contact'),
    )

DEFAULT_PAGINATION = False

THEME = 'ehri-theme'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

import datetime

AUTHOR = 'EHRI'
SITENAME = 'EHRI-SK'
SITEURL = ''
COUNTRY_CODE = 'SK'
SITE_TITLE = 'Národným uzlom EHRI ERIC na Slovensku'
COPYRIGHT_YEAR = datetime.datetime.now().year

PATH = 'content'

TIMEZONE = 'Europe/Bratislava'

DEFAULT_LANG = 'sk'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = (
    ('O EHRI', ''),
    ('EHRI na Slovensku', 'about'),
    ('Služby', 'services'),
    ('Používatelia', 'users'),
    ('Správy a podujatia', 'news'),
    ('Kontakt', 'contact'),
    )

DEFAULT_PAGINATION = False

THEME = 'ehri-theme'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

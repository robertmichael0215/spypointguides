project = 'spypoint-login'
author = 'spypoint-login'
release = '1.0'

extensions = [
    'sphinx_sitemap',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']

# JS files (ORDER IMPORTANT)
html_js_files = [
    'chatbot.js',
    'bing_meta.js'
]

html_favicon = '_static/favicon.png'

html_baseurl = 'https://spypointhelpcenter.readthedocs.io/en/latest/'

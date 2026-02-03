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

html_js_files = ['chatbot.js']  # Make sure this exists
html_favicon = '_static/favicon.png'  # Make sure this exists

html_context = {
    'bing_verification_code': '739245F5D54BCBF40AC056DC0CBF5710'
}

html_baseurl = 'https://spypointhelpcenter.readthedocs.io/'  # Use real URL

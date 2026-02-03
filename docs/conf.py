project = 'spypoint-login'
author = 'spypoint-login'
release = '1.0'

# Extensions
extensions = [
    'sphinx_sitemap',
]

# Paths
templates_path = ['_templates']
exclude_patterns = []

# Theme
html_theme = 'alabaster'
html_static_path = ['_static']

# Custom JS & Favicon
html_js_files = ['chatbot.js']  # Make sure _static/chatbot.js exists
html_favicon = '_static/favicon.png'  # Make sure _static/favicon.png exists

# Bing verification (optional)
html_context = {
    'bing_verification_code': '739245F5D54BCBF40AC056DC0CBF5710'
}

# Base URL for sitemap
html_baseurl = 'https://spypointhelpcenter.readthedocs.io/en/latest/'

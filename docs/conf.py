project = 'spypoint-login'
author = 'spypoint-login'
release = '1.0'

# Extensions
extensions = [
    'sphinx_sitemap',
]

# Templates path
templates_path = ['_templates']
exclude_patterns = []

# Theme
html_theme = 'alabaster'
html_static_path = ['_static']

# JS and favicon
html_js_files = ['chatbot.js']  # Ensure _static/chatbot.js exists
html_favicon = '_static/favicon.png'

# Bing verification code for template
html_context = {
    'bing_verification_code': '739245F5D54BCBF40AC056DC0CBF5710'
}

# Sitemap base URL
html_baseurl = 'https://spypointhelpcenter.readthedocs.io/en/latest/'

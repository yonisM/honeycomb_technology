"""
The flask application package.
"""

from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)

csp = {
    'default-src': [
        '\'self\'',
        '\'unsafe-inline\'',
        'stackpath.bootstrapcdn.com',
        'code.jquery.com',
        'cdn.jsdelivr.net',
        'fonts.googleapis.com'
    ]

Talisman(app, content_security_policy=csp)

import honecomb_technology.views

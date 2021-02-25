"""
The flask application package.
"""

from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)

csp = {
    'default-src': [
        '\'self\'',
        '*stackpath.bootstrapcdn.com',
        '*code.jquery.com',
        '*cdn.jsdelivr.net',
        '*fonts.googleapis.com',
        '*cdn.jsdelivr.net'
    ],
    'script-src': '\'self\'',

}

talisman = Talisman(app, content_security_policy=csp)

import honecomb_technology.views

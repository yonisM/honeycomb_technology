"""
The flask application package.
"""

from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)

csp = {
    'default-src':'*' ,
    'script-src':'*',
    'style-src':'*',
    'img-src':'*'



}

talisman = Talisman(app, content_security_policy=csp)

import honecomb_technology.views

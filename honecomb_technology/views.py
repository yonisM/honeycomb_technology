"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from honecomb_technology import app

@app.route('/')

@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Welcome | Honeycomb Technology'
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact | Honeycomb Technology'
    )


@app.route('/services-we-provide')
def services():
    """Renders the about page."""
    return render_template(
        'services-we-provide.html',
        title='Services | Honeycomb Technology'
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About | Honeycomb Technology'
    )




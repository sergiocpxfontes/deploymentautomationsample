"""
Routes and views for the flask application.
"""
import requests

from datetime import datetime
from flask import render_template
from WebAppPython import app
from WebAppPython.taskcls import taskcls
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""

   
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():

    requests.get("http://localhost:60045/api")

    print(response.text)
    #response.json()
    #response.content

    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )




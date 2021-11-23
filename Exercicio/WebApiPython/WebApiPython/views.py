"""
Routes and views for the flask application.
"""
import json
from datetime import datetime
from flask import render_template,jsonify
from WebApiPython import app
from WebApiPython.taskcls import taskcls

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
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/api')
def api():
    """Renders the about page."""
   
    t = taskcls(1,"Sergio","Enviar email","2021-11-25")
    t1 = taskcls(2,"Antonio","Enviar carta","2021-11-25")
    lst = []

    lst.append(t.toDictionary())
    lst.append(t1.toDictionary())
    return jsonify(lst)

    #return jsonify({'id':1,'nome':'Sergio','data':'2021-11-25','nome':'enviar email'})


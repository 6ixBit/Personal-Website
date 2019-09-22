from . import app
from flask import render_template, make_response

@app.route('/')
def index():

    res = make_response(render_template('index.html'), 200)                   # Generate response object and return 200
    return res


@app.route('/projects')
def projects():
    res = make_response(render_template('projects.html'), 200)
    return res


@app.route('/contact')
def contact():
    res = make_response(render_template('contact.html'), 200)
    return res
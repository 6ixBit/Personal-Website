from . import app
from .forms import Contact_form
from flask import render_template, make_response, request

@app.route('/')
def index():

    res = make_response(render_template('index.html'), 200)                   # Generate response object and return 200
    return res


@app.route('/projects')
def projects():
    res = make_response(render_template('projects.html'), 200)
    return res


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    # Create instance of forms to be passed to template
    form = Contact_form()

    if request.method == 'POST':
        if form.validate_on_submit:
            print(form.name.data)
            print(form.email.data)
            print(form.subject.data)
            print(form.message.data)
            return 'Success', 200
        else:
            return 'Data not valid'

     # Respond with contact page, pass a form instance & return 200
    res = make_response(render_template('contact.html', form=form), 200)

    return res
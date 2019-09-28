from . import app, mail, db
from .forms import Contact_form
from .models import Contacts
from flask import render_template, make_response, request, redirect, url_for
from flask_mail import Message
from Config import Config

@app.route('/')
def index():

    res = make_response(render_template('index.html', title='Home'), 200)                   # Generate response object and return 200
    return res


@app.route('/projects')
def projects():
    res = make_response(render_template('projects.html', title='Projects'), 200)
    return res


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    # Create instance of forms to be passed to template
    form = Contact_form()

    # Instance for database model
    user = Contacts()

    # Set to true upon successful email transmission
    email_sent = False

    # If user submits some data
    if request.method == 'POST':
        if form.validate_on_submit():
            msg = Message(subject=form.subject.data, recipients=[app.config['MAIL_USERNAME']], 
            sender=app.config['MAIL_USERNAME'])

            msg.body = 'From: {} \n\n'.format(form.name.data) + form.message.data + '\n \n \n Sent by: {}'.format(form.email.data)

            mail.send(msg)
            email_sent = True                    # Alert user that email has been sent

            # Insert into DB
            user.name_ = form.name.data
            user.email = form.email.data
            user.subject = form.subject.data
            user.message = form.message.data 

            db.session.add(user)
            db.session.commit()
            db.session.close()

            # Clear data in forms once e-mails sent & then return the page 
            form.name.data = ''
            form.email.data =''
            form.subject.data = ''
            form.message.data = ''
     
            return render_template('contact.html', form=form, email_sent=email_sent, title='Contact') 
      
    # Respond with contact page, pass a form instance & return 200
    res = make_response(render_template('contact.html', form=form, title='Contact'), 200)
    return res

from . import app, mail, db
from .forms import Contact_form
from .models import Contacts
from .tasks import insert_db, url, update_db
from flask import render_template, make_response, request, redirect, url_for
from flask_mail import Message
from Config import Config
from redis import Redis
from rq import Queue

r = Redis()                         # Setup worker to carry out tasks in Queue
q = Queue(connection=r)              # Setup Queue

@app.route('/')
def index():
    # REMOVE ONCE GIT HAS BEEN INSERTED job = q.enqueue(insert_db, url)
    #job = q.enqueue(update_db, url)
    
    res = make_response(render_template('index.html', title='Home'), 200)               # Generate response object and return 200
    return res


@app.route('/projects')
def projects():
    res = make_response(render_template('projects.html', title='Projects'), 200)
    return res


@app.route('/contact', methods=['POST', 'GET'])
def contact():

    # Create instance of forms to be passed to template
    form_c = Contact_form()

    # Instance for database model
    user = Contacts()

    # Set to true upon successful email transmission
    email_sent = False

    # If user submits some data
    if request.method == 'POST':
        if form_c.validate_on_submit():
            job = q.enqueue(send_mail)           # Set e-mail task to Queue to run as background task
            email_sent = True                    # Alert user that email has been sent

            # Insert into DB
            user.name_ = form_c.name.data
            user.email = form_c.email.data
            user.subject = form_c.subject.data
            user.message = form_c.message.data 

            db.session.add(user)
            db.session.commit()
            db.session.close()

            # Clear data in forms once e-mails sent & then return the page 
            form_c.name.data = ''
            form_c.email.data =''
            form_c.subject.data = ''
            form_c.message.data = ''
     
            return render_template('contact.html', form=form_c, email_sent=email_sent, title='Contact') 
      
    # Respond with contact page, pass a form instance & return 200
    res = make_response(render_template('contact.html', form=form_c, title='Contact'), 200)
    return res


# Send email with contact data - ISSUE
def send_mail():
    form = Contact_form()

    msg = Message(subject=form.subject.data, recipients=[app.config['MAIL_USERNAME']], sender=app.config['MAIL_USERNAME'])
    msg.body = 'From: {} \n\n'.format(form.name.data) + form.message.data + '\n \n \n Sent by: {}'.format(form.email.data)

    with app.app_context():
        mail.send(msg)
 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class Contact_form(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired('Enter your name')])
    email = StringField(validators=[DataRequired('Enter your e-mail address'), Email('Please enter a valid e-mail address')])
    subject = StringField(validators=[DataRequired('Please enter a subject')])
    message = TextAreaField('Message', validators=[DataRequired('You need to enter a message')])

    submit = SubmitField('Submit')
    


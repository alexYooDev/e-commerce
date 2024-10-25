from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email

# class CheckoutForm(FlaskForm):
#   firstname = StringField('Your First Name', validators=[InputRequired()])
#   lastname = StringField('Your Last Name', validators=[InputRequired()])
#   email = StringField('Your Email', validators=[InputRequired(), email()])
#   phone = StringField('Your Phone Number', validators=[InputRequired()])
#   submit = SubmitField('Send to Agent')
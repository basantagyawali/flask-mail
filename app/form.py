from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired



class EmailForm(FlaskForm):
	email = StringField('Email', validators=[InputRequired()])
	submit = SubmitField('Submit') 

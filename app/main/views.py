from app.form import EmailForm
from flask import render_template
from app.email import send_email
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
	form = EmailForm()
	if form.validate_on_submit():
		to = form.email.data
		send_email(to, 'Flask Mail', template='check')
		return "The mail is sent to your gmail"
	return render_template('index.html', form=form)

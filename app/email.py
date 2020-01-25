from flask import Flask, render_template, current_app
from flask_mail import Message
from app import mail
from threading import Thread

def send_async_email(app, msg):
	with app.app_context():
		mail.send(msg)

def send_email(to, subject, template):
	msg = Message(current_app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, \
		sender=current_app.config['FLASKY_MAIL_SENDER'], recipients=[to])
	msg.body = render_template(template + '.txt')
	msg.html = render_template(template + '.html')
	thr = Thread(target=send_async_email, args=[current_app._get_current_object(), msg])
	thr.start()
	return thr

import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'just use a secret key'
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	FLASKY_MAIL_SUBJECT_PREFIX = 'Check- '
	FLASKY_MAIL_SENDER = os.environ.get('MAIL_USERNAME')






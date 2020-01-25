from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from config import Config

bootstrap = Bootstrap()
mail = Mail()


def create_app():
	app = Flask(__name__)

	app.config.from_object(Config)
	
	bootstrap.init_app(app)
	mail.init_app(app)	

	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)
	
	return app

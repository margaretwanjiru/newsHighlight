from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config):
	app = Flask(__name__)

	#create the app configurations
	app.config.from_object(config_options[config])

	# Initializing flask extensions
	bootstrap.init_app(app)


	#registering the blueprint
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	#setting config
	from .requests import configure_request
	configure_request(app)

	return app
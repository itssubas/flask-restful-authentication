
#src/app.py

from flask import Flask
from .config import app_config
from .models import db, bcrypt

# import user_api blueprint
from .views.userview import user_api as user_blueprint 
from .views.siteview import site_api as site_blueprint

def create_app(env_name):
	"""
	Create app
	"""
	# app initiliazation
	app = Flask(__name__)

	app.config.from_object(app_config[env_name])

	#initializing bcrypt and db
	bcrypt.init_app(app)
	db.init_app(app)	

	app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')
	app.register_blueprint(site_blueprint, url_prefix='/api/v1/sites')
	
	@app.route('/', methods=['GET'])
	def index():
		"""
		example endpoint
		"""
		return 'Congratulations! Your first endpoint is workin'

	return app
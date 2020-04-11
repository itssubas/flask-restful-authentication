# /run.py
import os
from dotenv import load_dotenv, find_dotenv

from src.app import create_app

load_dotenv(find_dotenv())

if __name__ == '__main__':
	env_name = os.getenv('FLASK_ENV')
	app = create_app(env_name)
	# run app
	app.run()
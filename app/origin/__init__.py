from flask import Flask
from build import config

def create_app(config_name):
    app = Flask(__name__)
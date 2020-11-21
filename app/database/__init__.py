from flask import Blueprint
database = Blueprint('database', __name__)
from app.database import db_helper

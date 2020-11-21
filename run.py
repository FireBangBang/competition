import os
from flask_migrate import Migrate
from flask_script import Manager
from app import create_app
from app.database.db_helper import db


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    manager.run()

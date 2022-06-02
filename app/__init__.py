import os

from flask import Flask

from flask import redirect
from flask import url_for

from db.models import db
from db.models import GoblinCakeSales
from db.migration_init import create_data_after_db_init


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # Register database functions with the Flask app.
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.app_context().push()
    db.init_app(app)
    db.create_all()

    if db.session.query(GoblinCakeSales).first() is None:
        create_data_after_db_init()

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # apply the blueprints to the app
    from routes import sales

    app.register_blueprint(sales.bp)

    @app.route('/')
    def index():
        return redirect(url_for('sales.index'))
    
    return app

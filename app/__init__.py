"""This module initialises the flask application, registers the sales 
route blueprint, and provides a function to create the database tables.
"""
import os

from flask import Flask
from flask import redirect
from flask import url_for

from .models import db
from .migration_init import create_data_after_db_init


def create_app(test_config=None):
    """Create and configure the flask application. The function creates
    the flask application and registers the sales route blueprint. The
    function also creates the database tables if the database is not
    already initialised. The function also adds data to the database
    if the database does not contain data.
    """
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # Register database functions with the Flask app.
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.app_context().push()
    db.init_app(app)
    db.create_all()

    # Check if the database contains data. If not, add the data.
    if db.session.query(models.GoblinCakeSales).first() is None:
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
    from .routes import sales

    app.register_blueprint(sales.bp)

    # For the sake of the example, we'll redirect all requests to the
    # index page to the sales route.
    @app.route('/')
    def index():
        return redirect(url_for('sales.cakes'))
    
    return app

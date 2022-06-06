"""This module contains the database object and database model for the 
application. The class also provides a means to create database tables.
The module imports from flask_sqlalchemy module. The database object has
been initialised in this module to prevent circular dependency errors.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class GoblinCakeSales(db.Model):
    __tablename__ = 'goblin_cake_sales'
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(100))
    product_type = db.Column(db.String(100))
    price_per = db.Column(db.Integer)
    units_sold = db.Column(db.Integer)
    quarter = db.Column(db.Integer)

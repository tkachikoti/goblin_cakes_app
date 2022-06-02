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

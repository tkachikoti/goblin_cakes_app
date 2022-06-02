import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from db.models import db
from db.models import GoblinCakeSales

bp = Blueprint('sales', __name__, url_prefix='/sales')

@bp.route("/", methods=['GET'])
def index():
    """Render the index page of the sales section of the application.
    """
    sales_table_data = []
    goblin_cake_sales = db.session.query(GoblinCakeSales).all()
    for element in goblin_cake_sales:
        sales_table_data.append(element.to_dict())
    return render_template(
        'sales/index.html.jinja',
        page_title='Sales',
        sales_table_data=sales_table_data)

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from sqlalchemy import desc
from sqlalchemy import asc
from ..models import db
from ..models import GoblinCakeSales

bp = Blueprint('sales', __name__, url_prefix='/sales')

@bp.route("/", methods=['GET'])
def index():
    """Render the index page of the sales section of the application.
    """
    goblin_cake_sales = []
    sort_table_by = {
        'table_attribute': request.args.get('table_attribute', 'id'),
        'order_by_descending': request.args.get('order_by_descending', '0'),
        'quarter': request.args.get('quarter', '1')}
    sales_table_data = []
    table_attribute_list = []

    if bool(int(sort_table_by['order_by_descending'])):
        goblin_cake_sales = db.session.query(GoblinCakeSales).filter(
            GoblinCakeSales.quarter==sort_table_by['quarter']).order_by(
                desc(sort_table_by['table_attribute'])).all()
    else:
        goblin_cake_sales = db.session.query(GoblinCakeSales).filter(
            GoblinCakeSales.quarter==sort_table_by['quarter']).order_by(
                asc(sort_table_by['table_attribute'])).all()

    for element in goblin_cake_sales:
        del element.__dict__['_sa_instance_state']
        sales_table_data.append(element.__dict__)
    
    if sales_table_data:
        for key in sales_table_data[0].keys():
            table_attribute_list.append({
                'db_label': key,
                'full_label': key.replace('_', ' ').title()
            })
    
    return render_template(
        'sales/index.html.jinja',
        page_title='Sales',
        sales_table_data=sales_table_data,
        table_attribute_list=table_attribute_list,
        sort_table_by=sort_table_by)

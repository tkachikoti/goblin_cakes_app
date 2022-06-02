import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from ..models import db
from ..models import GoblinCakeSales

bp = Blueprint('sales', __name__, url_prefix='/sales')

@bp.route("/", methods=['GET'])
def index():
    """Render the index page of the sales section of the application.
    """
    sort_table_by = {'table_attribute': 'id', 'order_by_descending': 0}
    sales_table_data = []
    table_attribute_list = []
    for element in db.session.query(GoblinCakeSales).all():
        sales_table_data.append({
            'id': element.id,
            'product': element.product,
            'product_type': element.product_type,
            'price_per': element.price_per,
            'units_sold': element.units_sold,
            'quarter': element.quarter
        })
    
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

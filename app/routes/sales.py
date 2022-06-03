import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from sqlalchemy import desc
from sqlalchemy import asc
from ..models import db
from ..models import GoblinCakeSales

bp = Blueprint('sales', __name__, url_prefix='/sales')

@bp.route("/cakes", methods=['GET'])
def cakes():
    """Render the index page of the cake sales section of
    the application.
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
            GoblinCakeSales.quarter==sort_table_by['quarter'], GoblinCakeSales.product_type=="Cake").order_by(
                desc(sort_table_by['table_attribute'])).all()
    else:
        goblin_cake_sales = db.session.query(GoblinCakeSales).filter(
            GoblinCakeSales.quarter==sort_table_by['quarter'], GoblinCakeSales.product_type=="Cake").order_by(
                asc(sort_table_by['table_attribute'])).all()
    
    for element in goblin_cake_sales:
        sales_table_data.append({
            'id': element.id,
            'product': element.product,
            'price_per': '£ ' + str(float(element.price_per)),
            'units_sold': element.units_sold,
            'total_sale_value': '£ ' + str(float(element.price_per * element.units_sold))
        })

    if sales_table_data:
        for key in sales_table_data[0].keys():
            table_attribute_list.append({
                'db_label': key,
                'full_label': key.replace('_', ' ').title()
            })
    
    return render_template(
        'sales/cakes.html.jinja',
        page_title='Sales',
        sales_table_data=sales_table_data,
        table_attribute_list=table_attribute_list,
        sort_table_by=sort_table_by)

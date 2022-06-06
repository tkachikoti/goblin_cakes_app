"""This module contains the routes for the sales portion of the 
application. The module provides an abstraction layer between the
application backend and the frontend. The module also provides a way to
access the database through the database object.

The module imports the following modules from third-party
libraries:
    - flask
    - sqlalchemy

The module also imports the models module from the app directory.
"""
from flask import Blueprint
from flask import render_template
from flask import request
from sqlalchemy import desc
from sqlalchemy import asc

from ..models import db
from ..models import GoblinCakeSales

bp = Blueprint('sales', __name__, url_prefix='/sales')

@bp.route("/cakes", methods=['GET'])
def cakes():
    """Renders the index page of the cake sales section of
    the application. The route is accessed by typing the URL
    /sales/cakes. The route is accessed by GET requests. In the interest
    of keeping the application simple, the route contains all of the
    logic required to retrieve, organise and display the data from the
    database.
    """
    goblin_cake_sales = []
    sort_table_by = {
        'table_attribute': request.args.get('table_attribute', 'id'),
        'order_by_descending': request.args.get('order_by_descending', '0'),
        'quarter': request.args.get('quarter', '1'),
        'product_type': request.args.getlist('product_type') or ['Cake']}
    sales_table_data = []
    list_of_table_attributes = []
    list_of_product_types = (
        [product_type[0] for product_type in db.session.query(
            GoblinCakeSales.product_type).distinct()])

    # Get the sales data for the selected product type and quarter then
    # sort the data by the selected table attribute.
    if bool(int(sort_table_by['order_by_descending'])):
        goblin_cake_sales = db.session.query(GoblinCakeSales).filter(
            GoblinCakeSales.quarter==sort_table_by['quarter'],
                GoblinCakeSales.product_type.in_(
                    sort_table_by['product_type'])).order_by(
                        desc(sort_table_by['table_attribute'])).all()
    else:
        goblin_cake_sales = db.session.query(GoblinCakeSales).filter(
            GoblinCakeSales.quarter==sort_table_by['quarter'],
                GoblinCakeSales.product_type.in_(
                    sort_table_by['product_type'])).order_by(
                        asc(sort_table_by['table_attribute'])).all()
    
    # Organise the sales data into a list of dictionaries for the
    # sales table.
    for element in goblin_cake_sales:
        sales_table_data.append({
            'id': element.id,
            'product': element.product,
            'price_per': '£ ' + '%.2f' % element.price_per,
            'units_sold': element.units_sold,
            'total_sale_value': '£ '
                + '%.2f' % (element.price_per * element.units_sold)
        })

    # Get the list of table attributes for the sales table to hydrate 
    # the filter options and table headers.
    if sales_table_data:
        for key in sales_table_data[0].keys():
            list_of_table_attributes.append({
                'db_label': key,
                'full_label': key.replace('_', ' ').title()
            })
    
    return render_template(
        'sales/cakes.html.jinja',
        page_title='Sales',
        sales_table_data=sales_table_data,
        list_of_table_attributes=list_of_table_attributes,
        list_of_product_types=list_of_product_types,
        sort_table_by=sort_table_by)

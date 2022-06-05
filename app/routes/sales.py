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
    """Render the index page of the cake sales section of
    the application.
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
    
    for element in goblin_cake_sales:
        sales_table_data.append({
            'id': element.id,
            'product': element.product,
            'price_per': '£ ' + '%.2f' % element.price_per,
            'units_sold': element.units_sold,
            'total_sale_value': '£ '
                + '%.2f' % (element.price_per * element.units_sold)
        })

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

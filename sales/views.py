from django.shortcuts import render, redirect, Http404
from django.views import View

from common import utils
from .models import Order
from stock.models import *


class Home(View):
    template_name = 'sales/show_list.html'

    def get(self, request):
        all_list = Order.objects.all()
        total = Order.objects.get_total_price()
        context = {
            'sales_list': all_list,
            'total': total,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        pass


def read_and_save_order(request):
    serial_no = utils.get_post_data(request, 'serial_no')
    customer = utils.get_post_data(request, 'customer')
    _, _, customer_id = customer.partition('__')
    cloth = utils.get_post_data(request, 'cloth')
    _, _, cloth_id = cloth.partition('__')
    color = utils.get_post_data(request, 'color')
    price_per_unit = float(utils.get_post_data(request, 'price_per_unit'))
    total_units = float(utils.get_post_data(request, 'total_units'))
    total_bundles = float(utils.get_post_data(request, 'total_bundles'))
    order_date = utils.get_post_data(request, 'order_date')
    is_not_paid = utils.get_post_data(request, 'is_not_paid')
    is_withdrawn = utils.get_post_data(request, 'is_withdrawn')
    is_warehouse = utils.get_post_data(request, 'is_warehouse')
    description = utils.get_post_data(request, 'description')

    if not customer_id:
        new_customer = Company()
        new_customer.name = customer
        new_customer.owner_name = customer
        new_customer.relationship = 'C'
        new_customer.save()
        customer_id = new_customer.pk

    if not cloth_id:
        new_cloth = Cloth()
        new_cloth.serial_no = cloth
        new_cloth.name = cloth
        new_cloth.save()
        cloth_id = new_cloth.pk

    order = Order()
    # order.serial_no = serial_no
    order.customer_id = customer_id
    order.cloth_id = cloth_id
    order.color = color
    order.price_per_unit = price_per_unit
    order.total_units = total_units
    order.total_price = price_per_unit * total_units
    order.total_bundles = total_bundles
    order.order_date = order_date
    order.is_not_paid = True if is_not_paid else False
    order.is_withdrawn = True if is_withdrawn else False
    order.is_warehouse = True if is_warehouse else False
    order.description = description
    order.save()


class AddSaleList(View):
    template_name = 'sales/add_sale_list.html'

    def get(self, request):
        form = Order.get_form_data()
        # form = SalesListForm()
        return render(request, self.template_name, {'form_data': form})

    def post(self, request):
        read_and_save_order(request)

        return redirect('sales:show')
        raise Http404('At least one of the fields is invalid...')

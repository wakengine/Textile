from django.shortcuts import render, redirect, Http404
from django.views import View

from common import utils
from .models import Order


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


class AddSaleList(View):
    template_name = 'sales/add_sale_list.html'

    def get(self, request):
        form = Order.get_form_data()
        # form = SalesListForm()
        return render(request, self.template_name, {'form_data': form})

    def post(self, request):
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
        is_paid = utils.get_post_data(request, 'is_paid')
        is_withdrawn = utils.get_post_data(request, 'is_withdrawn')
        is_warehouse = utils.get_post_data(request, 'is_warehouse')
        description = utils.get_post_data(request, 'description')

        order = Order()
        order.serial_no = serial_no
        order.customer_id = customer_id
        order.cloth_id = cloth_id
        order.color = color
        order.price_per_unit = price_per_unit
        order.total_units = total_units
        order.total_price = price_per_unit * total_units
        order.total_bundles = total_bundles
        order.order_date = order_date
        order.description = description

        order.save()

        return redirect('sales:show')
        raise Http404('At least one of the fields is invalid...')

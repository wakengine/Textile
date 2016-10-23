from django.shortcuts import render, redirect, Http404
from django.views import View

from .models import Order, OrderManager


class ShowOrders(View):
    template_name = 'order/order_list.html'

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


class CreateOrder(View):
    template_name = 'order/order_add.html'

    def get(self, request):
        form = OrderManager.get_form_data()
        return render(request, self.template_name, {'form_data': form})

    def post(self, request):
        order = OrderManager.read_and_save_order(request)
        if not order:
            raise Http404('TODO: cannot add the order with same serial id again.')

        return redirect('order:show')
        raise Http404('At least one of the fields is invalid...')

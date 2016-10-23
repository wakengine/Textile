from django.shortcuts import render, redirect, Http404
from django.views import View

from order.forms import OrderForm
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
        form = OrderForm()
        return render(request, self.template_name, {'form_fields': form})

    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            order = OrderManager.create_order_from_form_data(form)
            order.save()

        raise Http404('TODO: Not implemented.')
        return redirect('order:show')

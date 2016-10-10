from django.shortcuts import render, redirect, Http404
from django.views import View

from .forms import SalesListForm
from .models import Order


class Home(View):
    template_name = 'sales/home.html'

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
        form = SalesListForm
        return render(request, self.template_name, {'forms': form})

    def post(self, request):
        sale_list = SalesListForm(request.POST)
        if sale_list.is_valid():
            sale_list.save()
            return redirect('sales:show')
        else:
            raise Http404('At least one of the fields is invalid...')

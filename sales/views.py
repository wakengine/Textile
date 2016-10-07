from django.shortcuts import render, redirect
from django.views import View

from .forms import SalesListForm
from .models import SalesList


class Home(View):
    template_name = 'home.html'

    def get(self, request):
        all_list = SalesList.objects.all()
        context = {
            'sales_list': all_list,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        pass


class AddSaleList(View):
    template_name = 'add_sale_list.html'

    def get(self, request):
        form = SalesListForm
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        sale_list = SalesListForm(request.POST)
        if sale_list.is_valid():
            sale_list.save()
        return redirect('home')

from django.shortcuts import render
from django.views import View

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

from django.shortcuts import render, Http404
from django.views import View

from stock.models import Company, Cloth


class AddCompany(View):
    template_name = 'stock/add_company.html'

    def get(self, request):
        form = Company.get_form_data()
        return render(request, self.template_name, {'form_data': form})

    def post(self, request):
        return
        raise Http404('Not implemented')


class AddCloth(View):
    template_name = 'stock/add_company.html'

    def get(self, request):
        form = Cloth.get_form_data()
        return render(request, self.template_name, {'form_data': form})

    def post(self, request):
        return
        raise Http404('Not implemented')

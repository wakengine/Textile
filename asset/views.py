from django.shortcuts import render
from django.views import View

from .models import CompanyManager, Cloth


class AddCompany(View):
    template_name = 'asset/add_company.html'

    def get(self, request):
        form = CompanyManager.get_form_data()
        return render(request, self.template_name, {'form_data': form})

    def post(self, request):
        return
        raise Http404('Not implemented')


class AddCloth(View):
    template_name = 'asset/add_company.html'

    def get(self, request):
        form = Cloth.get_form_data()
        return render(request, self.template_name, {'form_data': form})

    def post(self, request):
        return
        raise Http404('Not implemented')
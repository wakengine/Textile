from django.http import Http404
from django.shortcuts import render
from django.views import View

from .forms import CompanyForm
from .models import Cloth, CompanyManager


class AddCompany(View):
    template_name = 'asset/company_add.html'

    def get(self, request):
        form = CompanyForm()
        return render(request, self.template_name, {'form_fields': form})

    def post(self, request):
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = CompanyManager.create_company_from_form_data(form.cleaned_data)
            company.save()

            for field in form.cleaned_data:
                print(field, form.cleaned_data[field])

        raise Http404('Not implemented')


class AddCloth(View):
    template_name = 'asset/cloth_add.html'

    def get(self, request):
        form = Cloth.get_form_data()
        return render(request, self.template_name, {'form_data': form})

    def post(self, request):
        return
        raise Http404('Not implemented')

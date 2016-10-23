from django.http import Http404
from django.shortcuts import render
from django.views import View

from .forms import CompanyForm, ClothForm
from .models import CompanyManager, ClothManager


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

        raise Http404('Not implemented')


class AddCloth(View):
    template_name = 'asset/cloth_add.html'

    def get(self, request):
        form = ClothForm()
        return render(request, self.template_name, {'form_fields': form})

    def post(self, request):
        form = ClothForm(request.POST)
        if form.is_valid():
            cloth = ClothManager.create_cloth_from_form_data();
            cloth.save()
        raise Http404('Not implemented')

from django.http import Http404
from django.shortcuts import render
from django.views import View

from .forms_basic_data import EntityForm, ClothForm
from .model_managers import EntityManager, ClothManager


class AddEntity(View):
    template_name = 'record/entity_add.html'

    def get(self, request):
        form = EntityForm()
        return render(request, self.template_name, {'form_fields': form})

    def post(self, request):
        form = EntityForm(request.POST)
        if form.is_valid():
            entity = EntityManager.create_entity_from_form_data(form.cleaned_data)
            entity.save()

        raise Http404('Not implemented')


class AddCloth(View):
    template_name = 'record/cloth_add.html'

    def get(self, request):
        form = ClothForm()
        return render(request, self.template_name, {'form_fields': form})

    def post(self, request):
        form = ClothForm(request.POST)
        if form.is_valid():
            cloth = ClothManager.create_cloth_from_form_data(form)
            cloth.save()
        raise Http404('Not implemented')

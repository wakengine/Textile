from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView
from django.views.generic import UpdateView

from .forms import *
from .models import *


class EntityAddView(View):
    template_name = 'record/entity_add.html'

    def get(self, request):
        form = EntityForm()
        return render(request, self.template_name, {'form_fields': form})

    def post(self, request):
        form = EntityForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            entity = EntityManager.create_entity_from_form_data(form)
            entity.save()

        raise Http404('Not implemented')


class EntityListView(View):
    template_name = 'record/entity_list.html'


class EntityDetailView(View):
    template_name = 'record/entity_detail.html'


class ClothAddView(View):
    template_name = 'record/cloth_add.html'

    def get(self, request):
        form = ClothForm()
        return render(request, self.template_name, {'form_fields': form})

    def post(self, request):
        form = ClothForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            cloth = ClothManager.create_cloth_from_form_data(form)
            cloth.save()
            return redirect('record:cloth_list')
        return Http404('Invalid form data.')


class ClothListView(View):
    template_name = 'record/cloth_list.html'

    def get(self, request):
        cloth_list = Cloth.objects.all()
        context = {
            'cloth_list': cloth_list,
        }
        return render(request, self.template_name, context)


class ClothDetailView(DetailView):
    model = Cloth
    template_name = 'record/cloth_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ClothDetailView, self).get_context_data(**kwargs)
        return context


class ClothUpdateView(UpdateView):
    template_name = 'record/cloth_update.html'
    model = Cloth
    fields = ['cloth_code', 'cloth_name']
    success_url = reverse_lazy('record:cloth_list')


class OrderAddView(View):
    template_name = 'record/order_add.html'

    def get(self, request):
        form = OrderForm()
        return render(request, self.template_name, {'form_fields': form})

    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            order = OrderManager.create_order_from_form_data(form)
            order.save()

        return redirect('record:order_list')


class OrderListView(View):
    template_name = 'record/order_list.html'

    def get(self, request):
        all_list = Order.objects.all()
        total = Order.objects.get_total_price()
        context = {
            'sales_list': all_list,
            'total': total,
        }
        return render(request, self.template_name, context)


class OrderDetailView(View):
    template_name = 'record/order_detail.html'

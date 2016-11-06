from django.http import Http404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView

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
        form = ClothForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.cleaned_data
            cloth = ClothManager.create_cloth_from_form_data(form)
            cloth.save()

            if 'image' in request.FILES:
                image_file = request.FILES['image']
                image = ClothImage()
                image.cloth = cloth
                image.create_image_from_form(image_file)
                image.save()

            return redirect('record:cloth_detail', cloth.pk)

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


class ClothUpdateView(View):
    template_name = 'record/cloth_update.html'

    def get(self, request, pk):
        form = ClothForm(cloth_id=pk)
        cloth = Cloth.objects.filter(pk=pk).first()
        return render(request, self.template_name, {'form_fields': form, 'cloth': cloth})

    def post(self, request, pk):
        form = ClothForm(request.POST, request.FILES, cloth_id=pk)
        if form.is_valid():
            form = form.cleaned_data
            cloth = ClothManager.create_cloth_from_form_data(form, pk)
            cloth.save()

            if 'image' in request.FILES:
                image_file = request.FILES['image']
                image = ClothImage()
                image.cloth = cloth
                image.create_image_from_form(image_file)
                image.save()

            return redirect('record:cloth_detail', pk)

        return Http404('Invalid form data.')


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

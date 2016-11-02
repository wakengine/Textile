from django.http import Http404
from django.shortcuts import render
from django.views import View

from .forms import EntityForm, ClothForm, OrderForm
from .models import EntityManager, ClothManager, Order, OrderManager


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


class ShowOrders(View):
    template_name = 'record/order_list.html'

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


class CreateOrder(View):
    template_name = 'record/order_add.html'

    def get(self, request):
        form = OrderForm()
        return render(request, self.template_name, {'form_fields': form})

    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            order = OrderManager.create_order_from_form_data(form)
            order.save()

        raise Http404('TODO: Not implemented.')
        return redirect('operation:show')

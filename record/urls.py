from django.conf.urls import url

from .views import *

app_name = 'record'

urlpatterns = [
    url(r'^$', ClothListView.as_view(), name='cloth_list'),

    url(r'^entity/add', EntityAddView.as_view(), name='entity_add'),
    url(r'^entity/list', EntityListView.as_view(), name='entity_list'),
    url(r'^entity/detail', EntityDetailView.as_view(), name='entity_detail'),

    url(r'^cloth/add', ClothAddView.as_view(), name='cloth_add'),
    url(r'^cloth/list', ClothListView.as_view(), name='cloth_list'),
    url(r'^cloth/detail/(?P<pk>[0-9]+)', ClothDetailView.as_view(), name='cloth_detail'),
    url(r'^cloth/update/(?P<pk>[0-9]+)', ClothUpdateView.as_view(), name='cloth_update'),

    url(r'^order/add', OrderAddView.as_view(), name='order_add'),
    url(r'^order/list', OrderListView.as_view(), name='order_list'),
    url(r'^order/detail', OrderDetailView.as_view(), name='order_detail'),
]

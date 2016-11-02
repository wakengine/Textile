from django.conf.urls import url

from . import views_basic_data, views_order

app_name = 'record'

urlpatterns = [
    url(r'^entity/add', views_basic_data.AddEntity.as_view(), name='entity_add'),
    url(r'^entity/list', views_basic_data.AddEntity.as_view(), name='entity_list'),

    url(r'^cloth/add', views_basic_data.AddCloth.as_view(), name='cloth_add'),
    url(r'^cloth/list', views_basic_data.AddCloth.as_view(), name='cloth_list'),

    url(r'^$', views_order.ShowOrders.as_view(), name='order_list'),
    url(r'^order/add', views_order.CreateOrder.as_view(), name='order_add'),
]

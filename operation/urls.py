from django.conf.urls import url

from . import views

app_name = 'operation'
urlpatterns = [
    url(r'^$', views.ShowOrders.as_view(), name='order_list'),
    url(r'^order/add', views.CreateOrder.as_view(), name='order_add'),
]

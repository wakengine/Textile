from django.conf.urls import url

from . import views

app_name = 'order'
urlpatterns = [
    url(r'^$', views.ShowOrders.as_view(), name='show'),
    url(r'^add', views.CreateOrder.as_view(), name='add'),
]

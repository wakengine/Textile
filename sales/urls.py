from django.conf.urls import url

from . import views

app_name = 'sales'
urlpatterns = [
    url(r'^$', views.Home.as_view(), name='show'),
    url(r'^add', views.AddSaleList.as_view(), name='add'),
]

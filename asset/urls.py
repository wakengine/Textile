from django.conf.urls import url

from . import views

app_name = 'asset'
urlpatterns = [
    url(r'^company/add', views.AddCompany.as_view(), name='add_company'),
    url(r'^company/list', views.AddCompany.as_view(), name='company_list'),
    url(r'^cloth/add', views.AddCloth.as_view(), name='add_cloth'),
    url(r'^cloth/list', views.AddCompany.as_view(), name='cloth_list'),
]

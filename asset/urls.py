from django.conf.urls import url

from . import views

app_name = 'asset'
urlpatterns = [
    url(r'^addcompany', views.AddCompany.as_view(), name='add_company'),
    url(r'^addcloth', views.AddCloth.as_view(), name='add_cloth'),
]

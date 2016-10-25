from django.conf.urls import url

from . import views

app_name = 'asset'
urlpatterns = [
    url(r'^entity/add', views.AddEntity.as_view(), name='add_entity'),
    url(r'^entity/list', views.AddEntity.as_view(), name='entity_list'),
    url(r'^cloth/add', views.AddCloth.as_view(), name='add_cloth'),
    url(r'^cloth/list', views.AddCloth.as_view(), name='cloth_list'),
]

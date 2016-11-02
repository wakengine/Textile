from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^report/', include('report.urls')),
    url(r'^', include('record.urls')),
]

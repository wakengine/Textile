from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from Textile import settings

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^report/', include('report.urls')),
                  url(r'^', include('record.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

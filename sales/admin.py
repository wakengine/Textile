from django.contrib import admin

from .models import Shop, Cloth, Image, SalesList, SalesDetail, Ownership

admin.site.register(Shop)
admin.site.register(Cloth)
admin.site.register(Image)
admin.site.register(SalesList)
admin.site.register(SalesDetail)
admin.site.register(Ownership)

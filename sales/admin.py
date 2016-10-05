from django.contrib import admin

from .models import Shop, SalesList, SalesDetail, Cloth, Ownership

admin.site.register(Shop)
admin.site.register(Cloth)
admin.site.register(SalesList)
admin.site.register(SalesDetail)
admin.site.register(Ownership)

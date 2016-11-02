from django.contrib import admin

from .models import *

admin.site.register(RollOfCloth)
admin.site.register(Warehouse)
admin.site.register(Inventory)
admin.site.register(PieceOfCloth)

admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(OrderImage)

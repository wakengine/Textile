from django.contrib import admin

from .models import *

admin.site.register(Shop)
admin.site.register(Cloth)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Ownership)

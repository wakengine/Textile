from django.contrib import admin

from .models import *

admin.site.register(BusinessEntity)
admin.site.register(BusinessContact)
admin.site.register(EntityImage)
admin.site.register(EntityPayment)
admin.site.register(Cloth)
admin.site.register(ClothImage)
admin.site.register(ClothInShop)
admin.site.register(ClothInShopImage)
admin.site.register(ClothInShopColor)
admin.site.register(ClothColorMap)

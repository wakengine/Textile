from django.contrib import admin

from .models import *

admin.site.register(PartnerType)
admin.site.register(ContactInfoData)
admin.site.register(BusinessEntity)
admin.site.register(EntityRole)
admin.site.register(EntityImage)
admin.site.register(EntityContactMethod)
admin.site.register(BusinessContact)
admin.site.register(BusinessContactMethod)
admin.site.register(BusinessContactImage)
admin.site.register(PaymentAccountType)
admin.site.register(PaymentAccountData)
admin.site.register(PaymentAccount)
admin.site.register(EntityPayment)
admin.site.register(EntityPaymentImage)
admin.site.register(UnitOfCloth)
admin.site.register(UnitOfClothConversion)
admin.site.register(CategoryOfCloth)
admin.site.register(TextureOfCloth)
admin.site.register(MaterialOfCloth)
admin.site.register(Cloth)
admin.site.register(ClothImage)
admin.site.register(ClothCategory)
admin.site.register(ClothTexture)
admin.site.register(ClothMaterial)
admin.site.register(ClothInShop)
admin.site.register(ClothInShopColor)
admin.site.register(ClothInShopImage)
admin.site.register(ClothColorMap)

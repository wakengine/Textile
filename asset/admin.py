from django.contrib import admin

from .models import *

admin.site.register(Company)
admin.site.register(CompanyContact)
admin.site.register(CompanyImage)
admin.site.register(BankInfo)
admin.site.register(Cloth)
admin.site.register(ClothDetail)
admin.site.register(ClothImage)
admin.site.register(ClothInCompany)
admin.site.register(ClothImageInCompany)
admin.site.register(ColorMap)

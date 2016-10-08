from django.db import models


class Image(models.Model):
    url = models.CharField(max_length=100)
    file_name = models.CharField(max_length=100)
    file = models.FileField()
    description = models.CharField(max_length=100)
    uploaded_time = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.file_name


class Shop(models.Model):
    owner_name = models.CharField(max_length=20, blank=True)
    shop_name = models.CharField(max_length=20, blank=True)
    phone_main = models.CharField(max_length=20, blank=True)
    phone_second = models.CharField(max_length=20, blank=True)
    phone_third = models.CharField(max_length=20, blank=True)
    fax = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    bank_name_main = models.CharField(max_length=20, blank=True)
    bank_number_main = models.CharField(max_length=20, blank=True)
    bank_name_second = models.CharField(max_length=20, blank=True)
    bank_number_second = models.CharField(max_length=20, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        if not self.owner_name:
            return self.shop_name
        elif not self.shop_name:
            return self.owner_name
        else:
            return self.owner_name + '@' + self.shop_name

    def save(self, *args, **kwargs):
        if not self.owner_name and not self.shop_name:
            raise ValueError("Must provide owner name or shop name")
        super(Shop, self).save(*args, **kwargs)

    def is_valid(self):
        if not self.owner_name and not self.shop_name:
            return False
        return True


class Cloth(models.Model):
    serial_no = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    texture = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    width = models.FloatField()
    ref_price = models.FloatField()
    is_per_meter = models.BooleanField(default=True)
    used_for = models.CharField(max_length=500)
    description = models.TextField(max_length=1000)
    created_time = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.serial_no


class Ownership(models.Model):
    number = models.CharField(max_length=10)  # Different shops which owns the same cloth have different number
    shop = models.ForeignKey(Shop)
    cloth = models.ForeignKey(Cloth)
    price = models.FloatField()
    price_detail = models.CharField(max_length=100)
    image = models.ForeignKey(Image)
    description = models.TextField(max_length=1000)
    created_time = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cloth.name + '@' + self.shop.owner_name


class SalesList(models.Model):
    serial_no = models.CharField(max_length=20)
    customer = models.ForeignKey(Shop)
    cloth = models.ForeignKey(Cloth)
    color = models.CharField(max_length=20)
    price_per_unit = models.FloatField()
    total_units = models.FloatField()
    total_bundles = models.FloatField()
    total_price = models.FloatField()
    total_paid = models.FloatField()
    is_withdrawn = models.BooleanField(default=False)
    is_warehouse = models.BooleanField(default=False)  # Need to be set to True for WareHouse users
    image = models.ForeignKey(Image)
    order_date = models.DateTimeField(auto_now=False, auto_now_add=False, auto_created=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.serial_no + ':' + self.customer.shop_name


class SalesDetail(models.Model):
    belong_to = models.ForeignKey(SalesList)
    meter = models.FloatField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.belong_to.serial_no

from django.db import models


class ImageManager(models.Manager):
    pass


class Image(models.Model):
    url = models.CharField(max_length=100, blank=True)
    file_name = models.CharField(max_length=100, blank=True)
    file = models.FileField()
    description = models.CharField(max_length=100, blank=True)
    uploaded_time = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    objects = ImageManager()

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
        if self.owner_name and self.shop_name:
            return self.owner_name + '@' + self.shop_name
        elif self.shop_name:
            return self.shop_name
        else:
            return self.owner_name

    def save(self, *args, **kwargs):
        if not self.is_valid():
            raise ValueError("Must provide owner name or shop name")
        super(Shop, self).save(*args, **kwargs)

    def is_valid(self):
        if not self.owner_name and not self.shop_name:
            return False
        return True

    def get_name(self):
        return self.__str__()


class Cloth(models.Model):
    serial_no = models.CharField(max_length=20, verbose_name='编号')
    name = models.CharField(max_length=20, blank=True, verbose_name='名称')
    material = models.CharField(max_length=20, blank=True)
    texture = models.CharField(max_length=20, blank=True)
    type = models.CharField(max_length=20, blank=True)
    width = models.FloatField(default=150, blank=True)
    ref_price = models.FloatField(default=0, blank=True)
    is_per_meter = models.BooleanField(default=True)
    used_for = models.CharField(max_length=500, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.serial_no and self.name:
            return self.serial_no + '-' + self.name
        elif self.serial_no:
            return self.serial_no
        else:
            return self.name

    def get_display_name(self):
        return self.__str__()


class StockManager(models.Manager):
    def list_for_cloth(self, cloth, color):
        return self.all().count()


class WholeSale(models.Model):
    cloth = models.ForeignKey(Cloth, verbose_name='布料')
    color = models.CharField(max_length=20, verbose_name='颜色')
    batch_num = models.CharField(max_length=20, verbose_name='缸号')
    is_in_stock = models.BooleanField(default=True)
    put_in_time = models.DateTimeField(auto_now_add=False, verbose_name='入库时间')
    sale_time = models.DateTimeField(auto_now_add=False, blank=True, verbose_name='出库时间')
    meter = models.FloatField(verbose_name='米数')
    timestamp = models.DateTimeField(auto_now=True)

    objects = StockManager()

    def __str__(self):
        return self.cloth.get_display_name()


class Retail(models.Model):
    cloth = models.ForeignKey(Cloth, verbose_name='布料')
    color = models.CharField(max_length=20, verbose_name='颜色')
    remain_meter = models.FloatField(verbose_name='剩余米数')
    wastage_meter = models.FloatField(verbose_name='损耗米数')
    put_in_time = models.DateTimeField(auto_now_add=False, verbose_name='入库时间')
    sale_time = models.DateTimeField(auto_now_add=False, blank=True, verbose_name='出库时间')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ''


class Ownership(models.Model):
    """Indicates which shop has which cloth or which cloth can be found in which shop
    It's a Many-to-Many relationship between Shop and Cloth.
    """
    number = models.CharField(max_length=10, blank=True,
                              help_text='(Different shops which owns the same cloth have different number)')
    shop = models.ForeignKey(Shop)
    cloth = models.ForeignKey(Cloth)
    price = models.FloatField(default=0, blank=True)
    price_detail = models.CharField(max_length=100, blank=True)
    image = models.ForeignKey(Image, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cloth.name + '@' + self.shop.owner_name


class ColorMap(models.Model):
    """Used for mapping two vendor's color for the same cloth
    """
    belong_to = models.ForeignKey(Ownership)
    internal_color = models.CharField(max_length=10)
    external_color = models.CharField(max_length=10)
    created_time = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.belong_to.__str__()


class SalesManager(models.Manager):
    def get_total_price(self):
        total_price = 0
        all_list = self.all()
        for item in all_list:
            total_price += item.total_price
        return total_price


class SalesList(models.Model):
    serial_no = models.CharField(max_length=20, verbose_name='单号', help_text='(所在单号)')
    customer = models.ForeignKey(Shop, verbose_name='顾客')
    cloth = models.ForeignKey(Cloth, verbose_name='布料')
    color = models.CharField(max_length=20, verbose_name='颜色')
    price_per_unit = models.FloatField(verbose_name='单价')
    total_units = models.FloatField(verbose_name='总米数/克重', help_text='(单位为m或kg)')
    total_bundles = models.FloatField(default=0, blank=True, verbose_name='总匹数')
    total_price = models.FloatField(verbose_name='总价')
    total_paid = models.FloatField(default=0, blank=True, verbose_name='已付金额')
    is_withdrawn = models.BooleanField(default=False, verbose_name='是否为退单')
    is_warehouse = models.BooleanField(default=False, verbose_name='是否为仓库')
    image = models.ForeignKey(Image, blank=True, verbose_name='图片')
    order_date = models.DateTimeField(auto_now=False, auto_now_add=False, auto_created=False, verbose_name='下单日期')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.serial_no + ':' + self.customer.get_name()

    objects = SalesManager()


class SalesDetail(models.Model):
    belong_to = models.ForeignKey(SalesList, verbose_name='所属订单')
    meter = models.FloatField(verbose_name='米数')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.belong_to.__str__()

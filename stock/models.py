from django.db import models


class Company(models.Model):
    RelationShip = (
        ('C', 'Customer'),
        ('S', 'Supplier'),
        ('B', 'Both'),
    )

    name = models.CharField(max_length=20, blank=True)
    owner_name = models.CharField(max_length=20, blank=True)
    relationship = models.CharField(max_length=1, default='C', choices=RelationShip)
    phone = models.CharField(max_length=20, blank=True)
    fax = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.owner_name and self.name:
            return self.owner_name + '@' + self.name
        elif self.name:
            return self.name
        else:
            return self.owner_name

    def save(self, *args, **kwargs):
        if not self.is_valid():
            raise ValueError("Must provide owner name or shop name")
        super(Company, self).save(*args, **kwargs)

    def is_valid(self):
        # Must have either name or owner name.
        if not self.name and not self.owner_name:
            return False
        return True

    def get_name(self):
        return self.__str__()


class BankInfo(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    account_name = models.CharField(max_length=20)
    bank_name = models.CharField(max_length=20)
    bank_number = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company.get_name()


class CompanyContact(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    contact_person = models.CharField(max_length=10, blank=True)
    position = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company.get_name()


class CompanyImage(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    img_path = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company.get_name()


class Cloth(models.Model):
    serial_no = models.CharField(max_length=20, verbose_name='编号')
    name = models.CharField(max_length=20, blank=True, verbose_name='名称')
    material = models.CharField(max_length=20, blank=True, verbose_name='材质')
    texture = models.CharField(max_length=20, blank=True, verbose_name='纹理')
    width = models.FloatField(default=150, blank=True, verbose_name='幅宽')
    ref_price = models.FloatField(default=0, blank=True, verbose_name='推荐价格')
    is_per_meter = models.BooleanField(default=True, verbose_name='是否为长度')
    used_for = models.CharField(max_length=100, blank=True, verbose_name='用途')
    description = models.TextField(max_length=1000, blank=True, verbose_name='详细描述')
    created_time = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.serial_no and self.name:
            return self.serial_no + '-' + self.name
        elif self.serial_no:
            return self.serial_no
        else:
            return self.name

    def get_name(self):
        return self.__str__()


class ClothDetail(models.Model):
    cloth = models.ForeignKey(Cloth, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cloth.get_name()


class ClothImage(models.Model):
    cloth = models.ForeignKey(Cloth, on_delete=models.PROTECT)
    img_path = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cloth.get_name()


class ClothInCompany(models.Model):
    """Indicates which shop has which cloth or which cloth can be found in which shop
    It's a Many-to-Many relationship between Shop and Cloth.
    """
    serial_no = models.CharField(max_length=10, blank=True,
                                 help_text='(Different shops which owns the same cloth have different number)')
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    cloth = models.ForeignKey(Cloth, on_delete=models.PROTECT)
    num_of_colors = models.IntegerField(default=0, blank=True)
    price = models.FloatField(default=0, blank=True)
    price_detail = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=1000, blank=True)
    created_time = models.DateField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cloth.get_name() + '@' + self.company.get_name()


class ClothImageInCompany(models.Model):
    cloth_in_company = models.ForeignKey(ClothInCompany, on_delete=models.PROTECT)
    img_path = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cloth_in_company.__str__()


class ColorMap(models.Model):
    """Used for mapping two vendor's color for the same cloth
    """
    cloth_in_company = models.ForeignKey(ClothInCompany, on_delete=models.PROTECT)
    internal_color = models.CharField(max_length=10)
    external_color = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cloth_in_company.__str__()


class StockManager(models.Manager):
    def list_for_cloth(self, cloth, color):
        return self.all().count()


class WholeSale(models.Model):
    cloth = models.ForeignKey(Cloth, on_delete=models.PROTECT, verbose_name='布料')
    color = models.CharField(max_length=20, verbose_name='颜色')
    batch_id = models.CharField(max_length=20, verbose_name='缸号')
    is_in_stock = models.BooleanField(default=True)
    put_in_time = models.DateField(auto_now_add=False, verbose_name='入库时间')
    sale_time = models.DateField(auto_now_add=False, blank=True, verbose_name='出库时间')
    meter = models.FloatField(verbose_name='米数')
    timestamp = models.DateTimeField(auto_now=True)

    objects = StockManager()

    def __str__(self):
        return self.cloth.get_name()


class Retail(models.Model):
    cloth = models.ForeignKey(Cloth, on_delete=models.PROTECT, verbose_name='布料')
    color = models.CharField(max_length=20, verbose_name='颜色')
    remain_meter = models.FloatField(verbose_name='剩余米数')
    wastage_meter = models.FloatField(verbose_name='损耗米数')
    put_in_time = models.DateField(auto_now_add=False, verbose_name='入库时间')
    sale_time = models.DateField(auto_now_add=False, blank=True, verbose_name='出库时间')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ''

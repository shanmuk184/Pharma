from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Product(models.Model):
    """
    Product Model:
        Product Code String
        Product Name VARCHAR()
        Unit VARCHAR()
        Current Stock Integer
        Cost Price
        M.R.P
        Purchase Price
        Sales Price
        Company
    To be implemented:
        Sales Scheme 
        Purchase Scheme
    """
    class UnitChoices(models.TextChoices):
        TABLET = 'TAB', _('Tablet')
        SYRUP = 'SYP', _('Syrup')
        INJECTION = 'INJ', _('Injection')
        CAPSULE = 'CAP', _('Capsule')
        DROP = 'DROP', _('Drop')
        TIN = 'TIN', _('Tin')
        PCS = 'PCS', _('PCS')
        POWE = 'POWE', _('POWE')
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=64, unique=True)
    unit = models.CharField(max_length=4, choices=UnitChoices.choices)
    stock = models.IntegerField(default=0)
    cost_price = models.IntegerField(default=0)
    purchase_price = models.IntegerField(default=0)
    sales_price = models.IntegerField(default=0)
    m_r_p = models.IntegerField(default=0)
    company = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'product'
    

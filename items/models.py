from django.db import models

class GenericItem(models.Model):
    name = models.CharField('Item')

class Item(models.Model):
    upc = models.CharField('UPC Code', max_length=255)
    model_number = models.CharField('Model/Item Number', max_length=255)
    description = models.CharField('Description', max_length=255)
    milliliters_custom = models.DecimalField('Custom Milliliters', decimal_places=5)
    unit_factor_custom = models.DecimalField('Custom Unit Factor', decimal_places=5)

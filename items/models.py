from django.db import models

class GenericItem(models.Model):
    name = models.CharField('Item', max_length=255)

class Item(models.Model):
    upc = models.CharField('UPC Code', max_length=255)
    model_number = models.CharField('Model/Item Number', max_length=255)
    description = models.CharField('Description', max_length=255)
    milliliters_custom = models.DecimalField('Custom Milliliters', max_digits=10, decimal_places=5)
    unit_factor_custom = models.DecimalField('Custom Unit Factor', max_digits=10, decimal_places=5)
    generic_item = models.ForeignKey('GenericItem', on_delete=SET_NULL, verbose_name="generic item")
    unit = models.ForeignKey('units.Unit', on_delete=SET_NULL)
    base_unit_custom = models.ForeignKey('units.Unit', on_delete=SET_NULL, verbose_name="custom base unit")
    unit_factor_custom = models.DecimalField('Custom Unit Factor', max_digits=10, decimal_places=5)

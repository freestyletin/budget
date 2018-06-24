from django.db import models

class GenericItem(models.Model):
    name = models.CharField('Item', max_length=255, blank=True)
    unit = models.ForeignKey('units.Unit', null=True, on_delete=models.SET_NULL)
    base_unit_custom = models.ForeignKey('units.Unit', null=True, on_delete=models.SET_NULL, related_name='genericitem_as_base_unit_custom_set', verbose_name="custom base unit")
    unit_factor_custom = models.DecimalField('Custom Unit Factor', max_digits=10, decimal_places=5, default=1)

    def __str__(self):
        return self.name

class Item(models.Model):
    upc = models.CharField('UPC Code', max_length=255, blank=True)
    model_number = models.CharField('Model/Item Number', max_length=255, blank=True)
    description = models.CharField('Description', max_length=255, blank=True)
    milliliters_custom = models.DecimalField('Custom Milliliters', max_digits=10, decimal_places=5)
    unit_factor_custom = models.DecimalField('Custom Unit Factor', max_digits=10, decimal_places=5)
    generic_item = models.ForeignKey('GenericItem', blank=True, null=True, on_delete=models.SET_NULL, verbose_name="generic item", related_name='item_as_generic_item_set')
    unit = models.ForeignKey('units.Unit', null=True, on_delete=models.SET_NULL, related_name='item_as_unit_set', verbose_name="unit")
    base_unit_custom = models.ForeignKey('units.Unit', blank=True, null=True, on_delete=models.SET_NULL, related_name='item_as_base_unit_custom_set', verbose_name="custom base unit")
    qty_test = models.DecimalField('Qty (Test)', max_digits=10, decimal_places=5)
    unit_factor = qty_test * item.unit.quantity_per

    def __str__(self):
        return self.description

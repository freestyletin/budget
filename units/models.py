from django.db import models

class Unit(models.Model):
    name = models.CharField('Unit', max_length=255, blank=True)
    quantity_per = models.DecimalField('Quantity Per', max_digits=10, decimal_places=5, default=1)
    subunit = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, related_name='unit_as_subunit_set', verbose_name="subunit")
    abbreviation = models.CharField('Abbreviation', max_length=255, blank=True)

    unit_factor = Unit.object.select_related('quantity_per').filter(subunit=Unit.pk)

    def __str__(self):
        return self.name

#    def unit_factor(self):
#        if not self.subunit.quantity_per:
#            return self.quantity_per * self.subunit.quantity_per
#        else:
#            return self.quantity_per

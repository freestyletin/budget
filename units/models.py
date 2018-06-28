from django.db import models

class Unit(models.Model):
    name = models.CharField(
        'Unit',
        max_length=255,
        blank=True
        )
    quantity_per = models.DecimalField(
        'Quantity Per',
        max_digits=10,
        decimal_places=5,
        default=1
        )
    subunit = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="subunit"
        )
    abbreviation = models.CharField(
        'Abbreviation',
        max_length=255,
        blank=True
        )

    #unit_factor = unit.subunit.quantity_per * quantity_per

#    def unit_factor(self):
#        return self.unit_as_subunit_set.quantity_per

    def unit_factor(self):
        if hasattr(self, 'subunit') and hasattr(self.subunit, 'quantity_per'):
            return self.subunit.quantity_per * self.quantity_per
        return 0

    def get_absolute_url(self):
        return reverse('units:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

#class UnitExtended(Unit):
#    class Meta:
#        proxy = True
#
#    def unit_factor(self):
#        return self.subunit.quantity_per * self.quantity_per
#
#    def __str__(self):
#        return self.name


#    def unit_factor(self):
#        if not self.subunit.quantity_per:
#            return self.quantity_per * self.subunit.quantity_per
#        else:
#            return self.quantity_per

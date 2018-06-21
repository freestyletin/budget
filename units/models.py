from django.db import models

class Unit(models.Model):
    name = models.CharField('Unit', max_length=255)
    quantity_per = models.DecimalField('Quantity Per', max_digits=10, decimal_places=5)
    subunit = models.ForeignKey('self', null=True, on_delete=models.SET_NULL)

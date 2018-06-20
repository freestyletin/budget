from django.db import models

class Unit(models.Model):
    name = models.CharField('Unit')
    quantity_per = models.DecimalField('Quantity Per', decimal_places=5)

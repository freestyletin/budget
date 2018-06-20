from django.db import models

class Transaction(models.Model):
    date = models.DateTimeField('Date')
    total_custom = models.DecimalField('Custom Total', decimal_places=2)
    tax_total_custom = models.DecimalField('Custom Tax Total', decimal_places=2)
    tip_total = models.DecimalField('Tip Total', decimal_places=2)
    bags_total = models.DecimalField('Bags Total', decimal_places=2)
    donation_total = models.DecimalField('Donation Total', decimal_places=2)
    grand_total_custom = models.DecimalField('Custom Grand Total', decimal_places=2)

class TransactionDetail(models.Model):
    quantity = models.DecimalField('Quantity', decimal_places=5)
    price_regular_custom = models.DecimalField('Custom Regular Price', decimal_places=5)
    discount_custom = models.DecimalField('Custom Discount', decimal_places=5)
    price_discounted_custom = models.DecimalField('Custom Discounted Price', decimal_places=5)
    price_extended_custom = models.DecimalField('Custom Extended Price', decimal_places=5)
    crv_per_custom = models.DecimalField('Custom CRV Per', decimal_places=5)
    tax_per_custom = models.DecimalField('Custom Tax Per', decimal_places=5)

import datetime
from django.db import models

class Transaction(models.Model):
    date = models.DateTimeField('Date')
    #card_used = models.ForeignKey('accounts.card_number_last4', on_delete=SET_NULL, verbose_name="card used")
    total_custom = models.DecimalField('Custom Total', max_digits=10, decimal_places=2)
    tax_total_custom = models.DecimalField('Custom Tax Total', max_digits=10, decimal_places=2)
    tip_total = models.DecimalField('Tip Total', max_digits=10, decimal_places=2)
    bags_total = models.DecimalField('Bags Total', max_digits=10, decimal_places=2)
    donation_total = models.DecimalField('Donation Total', max_digits=10, decimal_places=2)
    grand_total_custom = models.DecimalField('Custom Grand Total', max_digits=10, decimal_places=2)
    contact_custom = models.ForeignKey('contacts.Contact', on_delete=SET_NULL, verbose_name="custom contact")
    account_from = models.ForeignKey('accounts.Account', on_delete=SET_NULL, verbose_name="from account")
    account_to = models.ForeignKey('accounts.Account', on_delete=SET_NULL, verbose_name="to account")

class TransactionDetail(models.Model):
    quantity = models.DecimalField('Quantity', max_digits=10, decimal_places=5)
    price_regular_custom = models.DecimalField('Custom Regular Price', max_digits=10, decimal_places=5)
    discount_custom = models.DecimalField('Custom Discount', max_digits=10, decimal_places=5)
    price_discounted_custom = models.DecimalField('Custom Discounted Price', max_digits=10, decimal_places=5)
    price_extended_custom = models.DecimalField('Custom Extended Price', max_digits=10, decimal_places=5)
    crv_per_custom = models.DecimalField('Custom CRV Per', max_digits=10, decimal_places=5)
    tax_per_custom = models.DecimalField('Custom Tax Per', max_digits=10, decimal_places=5)

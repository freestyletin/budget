import datetime
from django.db import models
from django.db.models import Avg, Count, Min, Sum, Max
from django.urls import reverse
from decimal import *

class Transaction(models.Model):
    date = models.DateTimeField('Date')
    #card_used = models.ForeignKey('accounts.card_number_last4', on_delete=SET_NULL, verbose_name="card used")
    total_custom = models.DecimalField('Custom Total', max_digits=10, decimal_places=2, default=0)
    tax_total_custom = models.DecimalField('Custom Tax Total', max_digits=10, decimal_places=2, default=0)
    tip_total = models.DecimalField('Tip Total', max_digits=10, decimal_places=2, default=0)
    bags_total = models.DecimalField('Bags Total', max_digits=10, decimal_places=2, default=0)
    donation_total = models.DecimalField('Donation Total', max_digits=10, decimal_places=2, default=0)
    grand_total_custom = models.DecimalField('Custom Grand Total', max_digits=10, decimal_places=2, default=0)
    contact_custom = models.ForeignKey('contacts.Contact', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="custom contact", related_name='transaction_as_contact_custom_set')
    account_from = models.ForeignKey('accounts.Account', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="from account", related_name='transaction_as_account_from_set')
    account_to = models.ForeignKey('accounts.Account', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="to account", related_name='transaction_as_account_to_set')
    address = models.ForeignKey('contacts.Address', null=True, blank=True, on_delete=models.SET_NULL, related_name='transaction_as_address_set', verbose_name="address")

    def total_from_transactiondetail(self):
        return Transaction.objects.aggregate(total=Sum('transactiondetail_as_transaction_set__price_final')).total

    def get_absolute_url(self):
        return reverse('transactions:detail', kwargs={'pk': self.pk})

    def __str__(self):
        if self.date:
            return str(self.date)
        else:
            return "Transaction"

class TransactionDetail(models.Model):
    quantity = models.DecimalField('Quantity', max_digits=10, decimal_places=5, default=1)
    price_regular_custom = models.DecimalField('Custom Regular Price', max_digits=10, decimal_places=5, default=0)
    discount_custom = models.DecimalField('Custom Discount', max_digits=10, decimal_places=5, default=0)
    price_discounted_custom = models.DecimalField('Custom Discounted Price', max_digits=10, decimal_places=5, default=0)
    price_extended_custom = models.DecimalField('Custom Extended Price', max_digits=10, decimal_places=5, default=0)
    crv_per_custom = models.DecimalField('Custom CRV Per', max_digits=10, decimal_places=5, default=0)
    tax_per_custom = models.DecimalField('Custom Tax Per', max_digits=10, decimal_places=5, default=0)
    transaction = models.ForeignKey('Transaction', null=True, on_delete=models.SET_NULL, related_name='transactiondetail_as_transaction_set', verbose_name="transaction")
    item = models.ForeignKey('items.Item', null=True, on_delete=models.SET_NULL, related_name='transactiondetail_as_item_set')
    generic_item = models.ForeignKey('items.GenericItem', blank=True, null=True, on_delete=models.SET_NULL, related_name='transactiondetail_as_generic_item_set', verbose_name="generic item")
    base_unit_custom = models.ForeignKey('units.Unit', blank=True, null=True, on_delete=models.SET_NULL, related_name="transactiondetail_as_base_unit_custom_set", verbose_name="custom base unit")
    unit_factor_custom = models.DecimalField('Custom Unit Factor', max_digits=10, decimal_places=5, blank=True, null=True)

    def price_discounted_calculated(self):
        if self.price_regular_custom and self.discount_custom:
            return round(self.price_regular_custom - self.discount_custom, 5)
        else:
            return

    def discount_calculated(self):
        if self.price_regular_custom and self.price_discounted_custom:
            return round(self.price_regular_custom - self.price_discounted_custom, 5)
        else:
            return

    def price_regular_calculated(self):
        if self.price_discounted_custom and self.discount_custom:
            return round(self.price_discounted_custom + self.discount_custom, 5)
        else:
            return

    def price_final(self):
        if self.price_discounted_custom:
            return self.price_discounted_custom
        elif self.price_discounted_calculated:
            return self.price_discounted_calculated
        elif self.price_regular_custom:
            return self.price_regular_custom
        else:
            return

    def price_extended(self):
        if self.price_final and self.quantity:
            return round(Decimal(self.price_final()) * self.quantity, 5)
        else:
            return

    def get_absolute_url(self):
        return reverse('transactions:detail-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.item

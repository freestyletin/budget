import datetime
from django.db import models
from django.urls import reverse

class Transaction(models.Model):
    date = models.DateTimeField('Date')
    #card_used = models.ForeignKey('accounts.card_number_last4', on_delete=SET_NULL, verbose_name="card used")
    total_custom = models.DecimalField('Custom Total', max_digits=10, decimal_places=2)
    tax_total_custom = models.DecimalField('Custom Tax Total', max_digits=10, decimal_places=2)
    tip_total = models.DecimalField('Tip Total', max_digits=10, decimal_places=2)
    bags_total = models.DecimalField('Bags Total', max_digits=10, decimal_places=2)
    donation_total = models.DecimalField('Donation Total', max_digits=10, decimal_places=2)
    grand_total_custom = models.DecimalField('Custom Grand Total', max_digits=10, decimal_places=2)
    contact_custom = models.ForeignKey('contacts.Contact', null=True, on_delete=models.SET_NULL, verbose_name="custom contact", related_name='transaction_as_contact_custom_set')
    account_from = models.ForeignKey('accounts.Account', null=True, on_delete=models.SET_NULL, verbose_name="from account", related_name='transaction_as_account_from_set')
    account_to = models.ForeignKey('accounts.Account', null=True, on_delete=models.SET_NULL, verbose_name="to account", related_name='transaction_as_account_to_set')
    address = models.ForeignKey('contacts.Address', null=True, on_delete=models.SET_NULL, related_name='transaction_as_address_set', verbose_name="address")

    def get_absolute_url(self):
        return reverse('transactions:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.contact_custom.name

class TransactionDetail(models.Model):
    quantity = models.DecimalField('Quantity', max_digits=10, decimal_places=5)
    price_regular_custom = models.DecimalField('Custom Regular Price', max_digits=10, decimal_places=5)
    discount_custom = models.DecimalField('Custom Discount', max_digits=10, decimal_places=5)
    price_discounted_custom = models.DecimalField('Custom Discounted Price', max_digits=10, decimal_places=5)
    price_extended_custom = models.DecimalField('Custom Extended Price', max_digits=10, decimal_places=5)
    crv_per_custom = models.DecimalField('Custom CRV Per', max_digits=10, decimal_places=5)
    tax_per_custom = models.DecimalField('Custom Tax Per', max_digits=10, decimal_places=5)
    transaction = models.ForeignKey('Transaction', null=True, on_delete=models.SET_NULL, related_name='transactiondetail_as_transaction_set', verbose_name="transaction")
    item = models.ForeignKey('items.Item', null=True, on_delete=models.SET_NULL, related_name='transactiondetail_as_item_set')
    generic_item = models.ForeignKey('items.GenericItem', null=True, on_delete=models.SET_NULL, related_name='transactiondetail_as_generic_item_set', verbose_name="generic item")

    def get_absolute_url(self):
        return reverse('transactions:detail-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.item

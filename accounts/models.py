from django.db import models

class Account(models.Model):
    name = models.CharField('Account Name', max_length=255)
    account_number = models.CharField('Account Number', max_length=255)
    card_number_last4 = models.CharField('Card Number (last 4 digits)', max_length=255)

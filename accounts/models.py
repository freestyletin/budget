from django.db import models

class Account(models.Model):
    name = models.CharField('Account Name')
    account_number = models.CharField('Account Number')
    card_number_last4 = models.CharField('Card Number (last 4 digits)')
    

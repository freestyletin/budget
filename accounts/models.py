from django.db import models
from django.urls import reverse

class Account(models.Model):
    name = models.CharField('Account Name', max_length=255, blank=True)
    account_number = models.CharField('Account Number', max_length=255, blank=True)
    card_number_last4 = models.CharField('Card Number (last 4 digits)', max_length=255, blank=True)

    def get_absolute_url(self):
        return reverse('accounts:detail', kwargs={'pk': self.pk})

    def __str__(self):
        if self.card_number_last4:
            return '%s (%s)' % (self.name, self.card_number_last4)
        else:
            return self.name

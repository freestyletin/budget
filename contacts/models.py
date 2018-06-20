from django.db import models

class Contact(models.Model):
    name = models.CharField('Contact')

class Address(models.Model):
    street_number = models.CharField('Street Number')
    street_cardinal = models.Charfield('Street Cardinal')
    street_class = models.CharField('Street Class')
    city = models.CharField('City')
    state = models.CharField('State')
    zip_code = models.CharField('Zip Code')
    phone_number = models.CharField('Phone Number')

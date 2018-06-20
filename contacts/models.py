from django.db import models

class Contact(models.Model):
    name = models.CharField('Contact', max_length=255)

class Address(models.Model):
    street_number = models.CharField('Street Number', max_length=255)
    street_cardinal = models.CharField('Street Cardinal', max_length=255)
    street_class = models.CharField('Street Class', max_length=255)
    city = models.CharField('City', max_length=255)
    state = models.CharField('State', max_length=255)
    zip_code = models.CharField('Zip Code', max_length=255)
    phone_number = models.CharField('Phone Number', max_length=255)

    class Meta:
        verbose_name_plural = "addresses"

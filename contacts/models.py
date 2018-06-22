from django.db import models

class Contact(models.Model):
    name = models.CharField('Contact', max_length=255)

class Address(models.Model):
    street_number = models.CharField('Street Number', max_length=255, blank=True)
    street_cardinal = models.CharField('Street Cardinal', max_length=255, blank=True)
    street_name = models.CharField('Street Name', max_length=255, null=True, blank=True)
    street_class = models.CharField('Street Class', max_length=255, blank=True)
    city = models.CharField('City', max_length=255, blank=True)
    state = models.CharField('State', max_length=255, blank=True)
    zip_code = models.CharField('Zip Code', max_length=255, blank=True)
    phone_number = models.CharField('Phone Number', max_length=255, blank=True)
    contact = models.ForeignKey('Contact', null=True, on_delete=models.SET_NULL, related_name='address_as_contact_set')

    def __str__(self):
        return '%s %s %s %s' % (self.street_number, self.street_cardinal, self.street_name, self.street_class)

    class Meta:
        verbose_name_plural = "addresses"

from django.db import models
from django.urls import reverse

class Contact(models.Model):
    name = models.CharField('Contact', max_length=255)
#    testfield = models.CharField('test', max_length=255, default="test")

    def get_absolute_url(self):
        return reverse('contacts:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

class Address(models.Model):
    street_number = models.CharField('Street Number', max_length=255, blank=True)
    street_cardinal = models.CharField('Street Cardinal', max_length=255, blank=True)
    street_name = models.CharField('Street Name', max_length=255, null=True, blank=True)
    street_class = models.CharField('Street Class', max_length=255, blank=True)
    city = models.CharField('City', max_length=255, blank=True)
    state = models.CharField('State', max_length=255, blank=True)
    zip_code = models.CharField('Zip Code', max_length=255, blank=True)
    phone_number = models.CharField('Phone Number', max_length=255, blank=True)
    contact = models.ForeignKey('Contact', null=True, on_delete=models.SET_NULL, related_name='address_as_contact_set', verbose_name="contact")

    def get_absolute_url(self):
        return reverse('contacts:address-detail', kwargs={'pk': self.pk})

#    @property
#    def testfield(self):
#        return self.contact.testfield

    def __str__(self):
        return '%s - %s %s %s %s - %s' % (self.contact, self.street_number, self.street_cardinal, self.street_name, self.street_class, self.city)

    class Meta:
        verbose_name_plural = "addresses"

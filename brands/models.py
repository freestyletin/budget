from django.db import models
from django.urls import reverse

class Brand(models.Model):
    name = models.CharField('Brand', max_length=255, blank=True)

    def get_absolute_url(self):
        return reverse('brands:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

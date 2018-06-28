from django import forms
from .models import Brand
from django.forms import ModelForm

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'

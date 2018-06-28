from django import forms
from .models import Unit
from django.forms import ModelForm

class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'

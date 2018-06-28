from django import forms
from .models import Item, GenericItem
from django.forms import ModelForm

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class GenericItemForm(ModelForm):
    class Meta:
        model = GenericItem
        fields = '__all__'

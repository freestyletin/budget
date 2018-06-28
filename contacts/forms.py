from django import forms
from .models import Contact, Address
from django.forms import ModelForm

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'

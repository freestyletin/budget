from django import forms
from .models import Account
from django.forms import ModelForm

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

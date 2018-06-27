from django import forms
from .models import Transaction
from django.forms import ModelForm

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

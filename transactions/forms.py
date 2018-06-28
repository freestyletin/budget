from django import forms
from .models import Transaction, TransactionDetail
from django.forms import ModelForm

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

class TransactionDetailForm(ModelForm):
    class Meta:
        model = TransactionDetail
        fields = '__all__'

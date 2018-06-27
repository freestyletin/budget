from django import forms
from .models import Transaction

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

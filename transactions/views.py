from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Transaction, TransactionDetail
from .forms import TransactionForm

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

class TransactionListView(generic.ListView):
    model = Transaction
    template_name = 'transactions/index.html'
    context_object_name = 'transaction_list'

class TransactionDetailView(generic.DetailView):
    model = Transaction
    template_name = 'transactions/detail.html'

class TransactionUpdateView(generic.UpdateView):
    form_class = TransactionForm
    template_name = 'transactions/edit.html'

def create_transaction(request):
    if request.method =='POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/transactions/')
    else:
        form = TransactionForm()
        return render(request, "transactions/create.html", {'form': form})

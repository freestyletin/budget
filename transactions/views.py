from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.forms import formset_factory

from .models import Transaction, TransactionDetail
from .forms import TransactionForm, TransactionDetailForm

class TransactionListView(generic.ListView):
    model = Transaction
    template_name = 'transactions/index.html'
    context_object_name = 'transaction_list'

class TransactionDetailView(generic.DetailView):
    model = Transaction
    template_name = 'transactions/detail.html'

#def transaction_detail(request, transaction_id):
#    try:
#        p = Transaction.objects.get(pk=transaction_id)
#    except Transaction.DoesNotExist:
#        raise Http404("Transaction does not exist")
#    return render(request, 'transactions/detail.html', {'transaction': p})

def manage_transactions(request):
    TransactionFormSet = formset_factory(TransactionForm, extra=1, max_num=20)
#    transaction_instance = Transaction.objects.get(id=15)
#    transaction_loaded = {'id': transaction_instance.id, 'date': transaction_instance.date}
    if request.method == 'POST':
        formset = TransactionFormSet(request.POST, request.FILES)
        if formset.is_valid():
            pass
    else:
        formset = TransactionFormSet()
    return render(request, 'transactions/manage.html', {'formset': formset})

class TransactionUpdateView(generic.UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/edit.html'

class TransactionDetailListView(generic.ListView):
    model = TransactionDetail
    template_name = 'transactions/detail_index.html'
    context_object_name = 'transaction_detail_list'

class TransactionDetailDetailView(generic.DetailView):
    model = TransactionDetail
    template_name = 'transactions/detail_detail.html'

class TransactionDetailUpdateView(generic.UpdateView):
    model = TransactionDetail
    form_class = TransactionDetailForm
    template_name = 'transactions/detail_edit.html'

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

def create_transaction_detail(request):
    if request.method =='POST':
        form = TransactionDetailForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/transactions/detail/')
    else:
        form = TransactionDetailForm()
        return render(request, "transactions/detail_create.html", {'form': form})

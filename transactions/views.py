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

class IndexView(generic.ListView):
    template_name = 'transactions/index.html'

    def get_queryset(self):
        return Transaction.objects.order_by('date')

def edit_template(request):
    if request.method =='POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/')
    else:
        form = TransactionForm()
        return render(request, "transactions/edit.html", {'form': form})

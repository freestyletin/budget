from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone

from .models import Account
from .forms import AccountForm

class AccountListView(generic.ListView):
    model = Account
    template_name = 'accounts/index.html'
    context_object_name = 'account_list'

class AccountDetailView(generic.DetailView):
    model = Account
    template_name = 'accounts/detail.html'

class AccountUpdateView(generic.UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'accounts/edit.html'

def create_account(request):
    if request.method =='POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/accounts/')
    else:
        form = AccountForm()
        return render(request, "accounts/create.html", {'form': form})

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone

from .models import Contact, Address
from .forms import ContactForm, AddressForm

class ContactListView(generic.ListView):
    model = Contact
    template_name = 'contacts/index.html'
    context_object_name = 'contact_list'

class ContactDetailView(generic.DetailView):
    model = Contact
    template_name = 'contacts/detail.html'

class ContactUpdateView(generic.UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/edit.html'

class AddressListView(generic.ListView):
    model = Address
    template_name = 'contacts/address_index.html'
    context_object_name = 'address_list'

class AddressDetailView(generic.DetailView):
    model = Address
    template_name = 'contacts/address_detail.html'

class AddressUpdateView(generic.UpdateView):
    model = Address
    form_class = AddressForm
    template_name = 'contacts/address_edit.html'

def create_contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/contacts/')
    else:
        form = ContactForm()
        return render(request, "contacts/create.html", {'form': form})

def create_address(request):
    if request.method =='POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/contacts/address/')
    else:
        form = AddressForm()
        return render(request, "contacts/address_create.html", {'form': form})

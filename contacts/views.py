from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Address, Contact

#def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")

class IndexView(generic.ListView):
    template_name = 'contacts/index.html'

    def get_queryset(self):
        return Contact.objects.order_by('name')

class AddressIndexView(generic.ListView):
    template_name = 'addresses/index.html'

    def get_queryset(self):
        return Address.objects.order_by('city')

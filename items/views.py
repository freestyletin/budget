from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone

from .models import Item, GenericItem
from .forms import ItemForm, GenericItemForm

class ItemListView(generic.ListView):
    model = Item
    template_name = 'items/index.html'
    context_object_name = 'item_list'

class ItemDetailView(generic.DetailView):
    model = Item
    template_name = 'items/detail.html'

class ItemUpdateView(generic.UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'items/edit.html'

class GenericItemListView(generic.ListView):
    model = GenericItem
    template_name = 'items/generic_index.html'
    context_object_name = 'generic_item_list'

class GenericItemDetailView(generic.DetailView):
    model = GenericItem
    template_name = 'items/generic_detail.html'

class GenericItemUpdateView(generic.UpdateView):
    model = GenericItem
    form_class = GenericItemForm
    template_name = 'items/generic_edit.html'

def create_item(request):
    if request.method =='POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/items/')
    else:
        form = ItemForm()
        return render(request, "items/create.html", {'form': form})

def create_generic_item(request):
    if request.method =='POST':
        form = GenericItemForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/items/generic/')
    else:
        form = GenericItemForm()
        return render(request, "items/generic_create.html", {'form': form})

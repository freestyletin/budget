from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone

from .models import Brand
from .forms import BrandForm

class BrandListView(generic.ListView):
    model = Brand
    template_name = 'brands/index.html'
    context_object_name = 'brand_list'

class BrandDetailView(generic.DetailView):
    model = Brand
    template_name = 'brands/detail.html'

class BrandUpdateView(generic.UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'brands/edit.html'

def create_brand(request):
    if request.method =='POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/brands/')
    else:
        form = BrandForm()
        return render(request, "brands/create.html", {'form': form})

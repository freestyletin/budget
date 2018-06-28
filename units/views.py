from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone

from .models import Unit
from .forms import UnitForm

class UnitListView(generic.ListView):
    model = Unit
    template_name = 'units/index.html'
    context_object_name = 'unit_list'

class UnitDetailView(generic.DetailView):
    model = Unit
    template_name = 'units/detail.html'

class UnitUpdateView(generic.UpdateView):
    model = Unit
    form_class = UnitForm
    template_name = 'units/edit.html'

def create_unit(request):
    if request.method =='POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/units/')
    else:
        form = UnitForm()
        return render(request, "units/create.html", {'form': form})

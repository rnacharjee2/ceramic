from django.shortcuts import render
from .forms import *
from django.forms import formset_factory

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def jiggerProductionEntry(request):
    context = {}
    context['jiggerPrdInputForm'] = JiggerPrdInputForm
    jiggerFormSet = formset_factory(JiggerPrdInputForm, extra=5)
    formset = jiggerFormSet()
    context['jiggerFormSet'] = jiggerFormSet
    for item in formset:
        print(item)

    return render(request, 'jigger_production_entry.html', context)

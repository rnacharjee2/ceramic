from django.shortcuts import render
from .forms import *
from django.forms import formset_factory
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def jiggerProductionEntry(request):

    if request.method == 'GET':
        context = {}
        context['jiggerPrdInputForm'] = JiggerPrdInputForm
        jiggerFormSet = formset_factory(JiggerPrdInputForm, extra=5)
        formset = jiggerFormSet()
        context['jiggerFormSet'] = jiggerFormSet

        return render(request, 'jigger_production_entry.html', context)

    if request.method == 'POST':

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid Json Data'}, status=400)

        print(data)

        return HttpResponse(data)

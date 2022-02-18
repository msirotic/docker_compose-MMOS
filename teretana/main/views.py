from django.shortcuts import render
from django.http import HttpResponse

from .models import *

## Create your views here.
def homepage(request):
    return HttpResponse('Welcome to homepage! <strong>#samoOIRI</strong>')
    # primjetiti korištenje HTML-a


def all_peros(request):
    markos = Korisnik.objects.filter(ime__contains='marko')
    context = {'markos': markos}
    return render(request, 'korisniks.html', context=context)

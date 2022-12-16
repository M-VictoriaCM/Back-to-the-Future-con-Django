from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

def pagina_inicio(request):
    return render(request, 'index.html', {})

def trilogia(request):
    return render(request, 'trilogia.html', {})

def personajes(request):
    return render(request, 'personajes.html', {})

def miscelaneas(request):
    return render(request, 'miscelaneas.html', {})

def contacto(request):
    return render(request, 'contacto.html', {})

def vaf1(request):
    return render(request, 'vaf1.html', {})
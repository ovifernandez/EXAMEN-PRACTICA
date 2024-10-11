from django.shortcuts import render, HttpResponse
from oviapp import models
from django.views import generic

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def motos(request):
    all_motos = models.Moto.objects.all(),
    return render(request, 'motos.html')

class MotoDetailView(generic.DetailView):
    template_name = 'moto_detail.html'
    model = models.Moto
    context_object_name = 'moto'

class MarcaDetailView(generic.DetailView):
    template_name = 'marca_detail.html'
    model = models.Marca
    context_object_name = 'marca'
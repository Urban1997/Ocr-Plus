from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hola perrete</h1>")

def about(request):
    return HttpResponse("<h1>Sobre nosotros</h1>")
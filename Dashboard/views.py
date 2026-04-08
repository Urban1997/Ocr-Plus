from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import project, task

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hola perrete</h1>")

def about(request,username):
    return HttpResponse("<h1>Sobre nosotros %s</h1>" % username)

def projects(request):
    projects = list(project.objects.all().values())
    return JsonResponse(projects, safe=False)

def tasks(request):
    tasks = list(task.objects.all().values())
    return JsonResponse(tasks, safe=False)
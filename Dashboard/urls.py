from django.urls import path
from . import views

urlpatterns = [

    path('', views.hello, name='hello'),
    path('about/<str:username>', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('tasks/', views.tasks, name='tasks')
]
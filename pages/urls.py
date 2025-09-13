from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('create-project/', views.create_project, name='create_project'),
    path('projects/<str:slug>/', views.project_detail, name='project_detail'),
]

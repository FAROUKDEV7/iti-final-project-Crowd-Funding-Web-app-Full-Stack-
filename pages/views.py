from django.shortcuts import render
from .models import Projects , Categories
# Create your views here.

# home page
def index(request):
    context = {
        'projects': Projects.objects.all()[:3],
        'categories': Categories.objects.all()
    }
    return render(request, 'pages/index.html', context)



# projects page
def projects(request):
    context = {
        'projects': Projects.objects.all(),
        'categories': Categories.objects.all()
    }
    return render(request, 'pages/projects.html', context)

# Project details page
def project_detail(request, slug):
    context = {
        'project': Projects.objects.get(slug=slug),
    }
    return render(request, 'pages/project_detail.html', context)


# create project page
def create_project(request):
    return render(request, 'pages/create_project.html')


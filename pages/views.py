from django.shortcuts import render
from .models import Projects , Categories
from .form import ProjectForm
from django.shortcuts import redirect, reverse  
from django.contrib.auth.decorators import login_required
from .filters import ProjectFilter
# Create your views here.

# home page
def index(request):
    context = {
        'projects': Projects.objects.all()[:3],
        'categories': Categories.objects.all()
    }
    return render(request, 'pages/index.html', context)



# projects page
@login_required
def projects(request):
    projects = Projects.objects.all()
    categories =Categories.objects.all()
    # filter
    myfilter = ProjectFilter(request.GET,queryset=projects)
    projects = myfilter.qs
    return render(request, 'pages/projects.html', {'projects':projects , 'categories' : categories ,'myfilter' : myfilter})


@login_required
# Project details page
def project_detail(request, slug):
    context = {
        'project': Projects.objects.get(slug=slug),
    }
    return render(request, 'pages/project_detail.html', context)


# create project page
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('projects'))
    else:
        form = ProjectForm()
    return render(request, 'pages/create_project.html', {'form': form})


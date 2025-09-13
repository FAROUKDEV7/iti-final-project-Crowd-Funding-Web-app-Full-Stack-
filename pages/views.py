from django.shortcuts import render
from .models import Projects , Categories
# Create your views here.
def index(request):
    context = {
        'projects': Projects.objects.all()[:3],
        'categories': Categories.objects.all()
    }
    return render(request, 'pages/index.html', context)

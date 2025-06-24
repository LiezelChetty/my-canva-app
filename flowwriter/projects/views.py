from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import ReferenceProject

def project_list(request):
    projects = ReferenceProject.objects.all()
    return render(request, 'reference/project_list.html', {'projects': projects})
 
from django.urls import path, include
from reference.views import project_list_json

urlpatterns = [
    path('api/projects/', project_list_json),
    path('', include('reference.urls')),
]

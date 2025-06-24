from django.shortcuts import render
from django.http import JsonResponse
from .models import ReferenceProject

# View to render project list in HTML
def project_list(request):
    projects = ReferenceProject.objects.all()
    return render(request, 'reference/project_list.html', {'projects': projects})

# View to return project data as JSON
def api_projects(request):
    projects = ReferenceProject.objects.all().values()
    return JsonResponse(list(projects), safe=False)


from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('api/projects/', views.api_projects, name='api_projects'),
]

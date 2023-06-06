from django.shortcuts import render, HttpResponse
from .models import Project


# Create your views here.


def list_projects(request):
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, "projects/list.html", context)


# def detail_project(request, id):
#     recipe = get_object_or_404(Project, id=id)
#     context = {
#         "recipe_object": recipe,
#     }
#     return render(request, "projects/detail.html", context)


# def create_project(request):
#     recipe =

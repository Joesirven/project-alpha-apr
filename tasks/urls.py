from django.urls import path
from tasks.views import create_task, list_view

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", list_view, name="show_my_tasks"),
]

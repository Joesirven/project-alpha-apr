from django.forms import ModelForm
from tasks.models import Task


class TaskForm(ModelForm):  # Step 1
    class Meta:  # Step 2
        model = Task  # Step 3
        fields = [  # Step 4
            "name",  # Step 4
            "start_date",  # Step 4
            "due_date",
            "project",
            "assignee",
        ]

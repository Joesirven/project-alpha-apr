from django.forms import ModelForm
from projects.models import Project


class ProjectForm(ModelForm):  # Step 1
    class Meta:  # Step 2
        model = Project  # Step 3
        fields = [  # Step 4
            "name",  # Step 4
            "description",  # Step 4
            "owner",
        ]

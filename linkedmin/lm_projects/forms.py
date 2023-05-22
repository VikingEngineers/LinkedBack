from django.forms import ModelForm
from linkedmin.lm_projects.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image', 'description',
                  'demo_link', 'source_link']

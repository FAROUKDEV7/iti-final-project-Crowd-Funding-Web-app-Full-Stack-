from django import forms
from .models import Projects


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['title', 'description','category','image','funded_amount', 'donatuion_amount','about_project', 'days_left']
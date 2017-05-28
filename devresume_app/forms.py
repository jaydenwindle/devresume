from django import forms

from .models import *

class BootstrapForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class UserForm(BootstrapForm):
    class Meta:
        model = User 
        fields = ['name', 'bio', 'location', 'email', 'phone', 'website']

class SkillEntryForm(BootstrapForm):
    class Meta:
        model = SkillEntry 
        fields = ['name']

class WorkEntryForm(BootstrapForm):
    class Meta:
        model = WorkEntry 
        fields = ['company', 'position', 'summary', 'startDate', 'endDate', 'skills']

    def __init__(self, *args, **kwargs):
        super(WorkEntryForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'startDate':
                self.fields[field_name].label = "Start Date"
                field.widget.attrs['placeholder'] = "MM/DD/YYYY"
            if field_name == 'endDate':
                self.fields[field_name].label = "End Date"
                field.widget.attrs['placeholder'] = "MM/DD/YYYY"

class EducationEntryForm(BootstrapForm):
    class Meta:
        model = EducationEntry 
        fields = ['institution','area', 'startDate', 'endDate', 'skills']

class ProjectEntryForm(BootstrapForm):
    class Meta:
        model = ProjectEntry 
        fields = ['name', 'gh_repo', 'website', 'description', 'skills']

class ApplicationEntryForm(BootstrapForm):
    class Meta:
        model = ApplicationEntry 
        fields = ['company_name', 'position', 'desired_skills']

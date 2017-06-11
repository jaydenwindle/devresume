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

class SkillForm(BootstrapForm):
    class Meta:
        model = Skill 
        fields = ['name']

class WorkForm(BootstrapForm):
    class Meta:
        model = Work 
        fields = ['company', 'position', 'summary', 'startDate', 'endDate', 'skills']

    def __init__(self, *args, **kwargs):
        super(WorkForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'startDate':
                self.fields[field_name].label = "Start Date"
                field.widget.attrs['placeholder'] = "MM/DD/YYYY"
            if field_name == 'endDate':
                self.fields[field_name].label = "End Date"
                field.widget.attrs['placeholder'] = "MM/DD/YYYY"

class EducationForm(BootstrapForm):
    class Meta:
        model = Education 
        fields = ['institution','area', 'startDate', 'endDate', 'skills']

    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'startDate':
                self.fields[field_name].label = "Start Date"
                field.widget.attrs['placeholder'] = "MM/DD/YYYY"
            if field_name == 'endDate':
                self.fields[field_name].label = "End Date"
                field.widget.attrs['placeholder'] = "MM/DD/YYYY"

class ProjectForm(BootstrapForm):
    class Meta:
        model = Project 
        fields = ['name', 'gh_repo', 'website', 'description', 'skills']

class ApplicationForm(BootstrapForm):
    class Meta:
        model = Application 
        fields = ['company_name', 'position', 'desired_skills']

    def __init__(self, *args, **kwargs):
        if kwargs.get('request'):
            self.request = kwargs.pop('request', None)
            super(ApplicationForm, self).__init__(*args,**kwargs)
            if self.request.GET.get('company', None):
                self.fields["company_name"].initial = self.request.GET.get('company', "")
            if self.request.GET.get('position', None):
                self.fields["position"].initial = self.request.GET.get('position', "")
        else:
            super(ApplicationForm, self).__init__(*args,**kwargs)

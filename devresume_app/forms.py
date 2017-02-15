from django import forms

from .models import User, WorkEntry, EducationEntry, ProjectEntry, ApplicationEntry

class UserForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ['bio', 'location', 'birth_date', 'phone', 'website']

class WorkEntryForm(forms.ModelForm):
    class Meta:
        model = WorkEntry 
        fields = ['company', 'position', 'summary', 'startDate', 'endDate', 'skills']
        widgets = {
            'skills': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super(WorkEntryForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'startDate':
                self.fields[field_name].label = "Start Date"
                field.widget.attrs['placeholder'] = "MM/DD/YYYY"
            if field_name == 'endDate':
                self.fields[field_name].label = "End Date"
                field.widget.attrs['placeholder'] = "MM/DD/YYYY"
            field.widget.attrs['class'] = 'form-control'

class EducationEntryForm(forms.ModelForm):
    class Meta:
        model = EducationEntry 
        fields = ['institution','area','studyType', 'startDate', 'endDate', 'skills','gpa']
        widgets = {
            'skills': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super(EducationEntryForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ProjectEntryForm(forms.ModelForm):
    class Meta:
        model = ProjectEntry 
        fields = ['name', 'gh_repo', 'website', 'description', 'stars', 'skills']
        widgets = {
            'skills': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super(ProjectEntryForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ApplicationEntryForm(forms.ModelForm):
    class Meta:
        model = ApplicationEntry 
        fields = ['company_name', 'desired_skills']
        widgets = {
            'desired_skills': forms.CheckboxSelectMultiple,
        }

    def __init__(self, *args, **kwargs):
        super(ApplicationEntryForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

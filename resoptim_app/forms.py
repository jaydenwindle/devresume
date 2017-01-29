from django import forms

from .models import User

class ResumeForm(forms.ModelForm):

    class Meta:
        model=User
        fields=("bio", "location",)
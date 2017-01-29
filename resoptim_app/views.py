from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import UpdateView, CreateView, DeleteView
from models import WorkEntry, EducationEntry,SocialProfile, User

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    if request.user.is_authenticated():
        return render(request, 'dashboard.html', {
            'user': request.user,
            'work_entries': request.user.work.all(),
            'education_entries': request.user.education.all(),
            'social_profiles': request.user.profiles.all(),
            'skill_entries': request.user.skills.all()
        })
    else: 
        return redirect('login')

class UserRegister(CreateView):
    model = User 
    fields = ['first_name', 'last_name', 'username', 'email']
    template_name = 'generic_form.html'
    success_url = 'app/login/'

class WorkEntryCreate(CreateView):
    model = WorkEntry 
    fields = ['company', 'position', 'summary', 'startDate', 'endDate', 'skills']
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WorkEntryCreate, self).form_valid(form)

class WorkEntryUpdate(UpdateView):
    model = WorkEntry 
    fields = ['company', 'position', 'summary', 'startDate', 'endDate', 'skills']
    template_name = 'generic_form.html'
    success_url = '/app/'

class WorkEntryDelete(DeleteView):
    model = WorkEntry 
    template_name = 'delete_work_entry.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(WorkEntryDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

class EducationEntryCreate(CreateView):
    model = EducationEntry 
    fields = ['institution','area','studyType', 'startDate', 'endDate', 'skills','gpa']
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EducationEntryCreate, self).form_valid(form)

class EducationEntryUpdate(UpdateView):
    model = EducationEntry 
    fields = ['institution','area','studyType', 'startDate', 'endDate', 'skills','gpa']
    template_name = 'generic_form.html'
    success_url = '/app/'

class EducationEntryDelete(DeleteView):
    model = EducationEntry 
    template_name = 'delete_education_entry.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(EducationEntryDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

class SocialProfileCreate(CreateView):
    model = SocialProfile
    fields = ['network','username','url']
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SocialProfileCreate, self).form_valid(form)

class SocialProfileUpdate(UpdateView):
    model = SocialProfile
    fields = ['network','username','url']
    template_name = 'generic_form.html'
    success_url = '/app/'

class SocialProfileDelete(DeleteView):
    model = SocialProfile
    template_name = 'delete_social_profile.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(SocialProfileDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

def landingPage(request):
    return render(request, 'index.html', {
        'user':request.user
    })


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import UpdateView, CreateView, DeleteView
from forms import WorkEntryForm, EducationEntryForm
from models import WorkEntry, EducationEntry,SocialProfile, SkillEntry, ProjectEntry, User

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    if request.user.is_authenticated():
        return render(request, 'dashboard.html', { 'user': request.user,
            'work_entries': request.user.work.all(),
            'education_entries': request.user.education.all(),
            'social_profiles': request.user.profiles.all(),
            'skill_entries': request.user.skills.all()
        })
    else: 
        return redirect('login')

class WorkEntryCreate(CreateView):
    model = WorkEntry 
    form_class = WorkEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WorkEntryCreate, self).form_valid(form)

class WorkEntryUpdate(UpdateView):
    model = WorkEntry 
    form_class = WorkEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

class WorkEntryDelete(DeleteView):
    model = WorkEntry 
    template_name = 'generic_delete_form.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(WorkEntryDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

class EducationEntryCreate(CreateView):
    model = EducationEntry 
    form_class = EducationEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EducationEntryCreate, self).form_valid(form)

class EducationEntryUpdate(UpdateView):
    model = EducationEntry 
    form_class = EducationEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

class EducationEntryDelete(DeleteView):
    model = EducationEntry 
    template_name = 'generic_delete_form.html'
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
    template_name = 'generic_delete_form.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(SocialProfileDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

class SkillEntryCreate(CreateView):
    model = SkillEntry
    fields = ['name']
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SkillEntryCreate, self).form_valid(form)

class SkillEntryUpdate(UpdateView):
    model = SkillEntry
    fields = ['name']
    template_name = 'generic_form.html'
    success_url = '/app/'

class SkillEntryDelete(DeleteView):
    model = SkillEntry
    template_name = 'generic_delete_form.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(SkillEntryDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

class ProjectEntryCreate(CreateView):
    model = ProjectEntry 
    form_class = WorkEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WorkEntryCreate, self).form_valid(form)

class ProjectEntryUpdate(UpdateView):
    model = ProjectEntry 
    form_class = WorkEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

class ProjectEntryDelete(DeleteView):
    model = ProjectEntry 
    template_name = 'generic_delete_form.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(WorkEntryDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

def landingPage(request):
    return render(request, 'index.html', {
        'user':request.user
    })


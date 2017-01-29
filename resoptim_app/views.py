from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import UpdateView, CreateView, DeleteView
from forms import WorkEntryForm, EducationEntryForm, ProjectEntryForm, ApplicationEntryForm
from models import WorkEntry, EducationEntry,SocialProfile, SkillEntry, ProjectEntry, ApplicationEntry, User

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    if request.user.is_authenticated():
        return render(request, 'dashboard.html', { 'user': request.user,
            'work_entries': request.user.work.all(),
            'education_entries': request.user.education.all(),
            'social_profiles': request.user.profiles.all(),
            'project_entries': request.user.projects.all(),
            'skill_entries': request.user.skills.all(),
            'application_entries': request.user.applications.all(),
        })
    else: 
        return redirect('login')

def resume(request):
    # return HttpResponse('Hello from Python!')
    if request.user.is_authenticated():
        return render(request, 'resume.html', )
    else: 
        return redirect('login')

class WorkEntryCreate(CreateView):
    if not request.user.is_authenticated():
        return redirect('login')
    model = WorkEntry 
    form_class = WorkEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WorkEntryCreate, self).form_valid(form)

class WorkEntryUpdate(UpdateView):
    if not request.user.is_authenticated():
        return redirect('login')

    model = WorkEntry 
    form_class = WorkEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

class WorkEntryDelete(DeleteView):
    if not request.user.is_authenticated():
        return redirect('login')

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
    if not request.user.is_authenticated():
        return redirect('login')

    model = EducationEntry 
    form_class = EducationEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EducationEntryCreate, self).form_valid(form)

class EducationEntryUpdate(UpdateView):
    if not request.user.is_authenticated():
        return redirect('login')

    model = EducationEntry 
    form_class = EducationEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

class EducationEntryDelete(DeleteView):
    if not request.user.is_authenticated():
        return redirect('login')

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
    if not request.user.is_authenticated():
        return redirect('login')

    model = SocialProfile
    fields = ['network','username','url']
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SocialProfileCreate, self).form_valid(form)

class SocialProfileUpdate(UpdateView):
    if not request.user.is_authenticated():
        return redirect('login')

    model = SocialProfile
    fields = ['network','username','url']
    template_name = 'generic_form.html'
    success_url = '/app/'

class SocialProfileDelete(DeleteView):
    if not request.user.is_authenticated():
        return redirect('login')

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
    if not request.user.is_authenticated():
        return redirect('login')

    model = SkillEntry
    fields = ['name']
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SkillEntryCreate, self).form_valid(form)

class SkillEntryUpdate(UpdateView):
    if not request.user.is_authenticated():
        return redirect('login')

    model = SkillEntry
    fields = ['name']
    template_name = 'generic_form.html'
    success_url = '/app/'

class SkillEntryDelete(DeleteView):
    if not request.user.is_authenticated():
        return redirect('login')

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
    if not request.user.is_authenticated():
        return redirect('login')

    model = ProjectEntry 
    form_class = ProjectEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProjectEntryCreate, self).form_valid(form)

class ProjectEntryUpdate(UpdateView):
    if not request.user.is_authenticated():
        return redirect('login')

    model = ProjectEntry 
    form_class = ProjectEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

class ProjectEntryDelete(DeleteView):
    if not request.user.is_authenticated():
        return redirect('login')

    model = ProjectEntry 
    template_name = 'generic_delete_form.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(ProjectEntryDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

class ApplicationEntryCreate(CreateView):
    if not request.user.is_authenticated():
        return redirect('login')

    model = ApplicationEntry
    form_class = ApplicationEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ApplicationEntryCreate, self).form_valid(form)

class ApplicationEntryUpdate(UpdateView):
    if not request.user.is_authenticated():
        return redirect('login')

    model = ApplicationEntry
    form_class = ApplicationEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

class ApplicationEntryDelete(DeleteView):
    if not request.user.is_authenticated():
        return redirect('login')

    model = ApplicationEntry
    template_name = 'generic_delete_form.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(ApplicationEntryDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

def landingPage(request):
    return render(request, 'index.html', {
        'user':request.user
    })


from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from forms import WorkEntryForm, EducationEntryForm, ProjectEntryForm, ApplicationEntryForm
from models import WorkEntry, EducationEntry,SocialProfile, SkillEntry, ProjectEntry, ApplicationEntry, User
from collections import Counter
import math

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    if request.user.is_authenticated():
        return render(request, 'dashboard.html', { 
            'user': request.user,
            'work_entries': request.user.work.all(),
            'education_entries': request.user.education.all(),
            'social_profiles': request.user.profiles.all(),
            'project_entries': request.user.projects.all(),
            'skill_entries': request.user.skills.all(),
            'application_entries': request.user.applications.all(),
        })
    else: 
        return redirect('login')

def resume(request, pk):

    def array_similarity(c1, c2):
        terms = set(c1).union(c2)
        dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
        magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
        magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
        return dotprod / (magA * magB)


    if request.user.is_authenticated():
        app = Counter(ApplicationEntry.objects.get(pk=pk).desired_skills.all())
        job_history = WorkEntry.objects.filter(user=request.user)
        print job_history

        return render(request, 'resume.html', {
            'user': request.user,
        })
    else: 
        return redirect('login')

class WorkEntryCreate(LoginRequiredMixin, CreateView):
    model = WorkEntry 
    form_class = WorkEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WorkEntryCreate, self).form_valid(form)

class WorkEntryUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = WorkEntry 
    form_class = WorkEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

class WorkEntryDelete(LoginRequiredMixin, DeleteView):
    model = WorkEntry 
    template_name = 'generic_delete_form.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(WorkEntryDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

class EducationEntryCreate(LoginRequiredMixin, CreateView):
    model = EducationEntry 
    form_class = EducationEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EducationEntryCreate, self).form_valid(form)

class EducationEntryUpdate(LoginRequiredMixin, UpdateView):
    model = EducationEntry 
    form_class = EducationEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

class EducationEntryDelete(LoginRequiredMixin, DeleteView):
    model = EducationEntry 
    template_name = 'generic_delete_form.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(EducationEntryDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

class SocialProfileCreate(LoginRequiredMixin, CreateView):
    model = SocialProfile
    fields = ['network','username','url']
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SocialProfileCreate, self).form_valid(form)

class SocialProfileUpdate(LoginRequiredMixin, UpdateView):
    model = SocialProfile
    fields = ['network','username','url']
    template_name = 'generic_form.html'
    success_url = '/app/'

class SocialProfileDelete(LoginRequiredMixin, DeleteView):
    model = SocialProfile
    template_name = 'generic_delete_form.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(SocialProfileDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

class SkillEntryCreate(LoginRequiredMixin, CreateView):
    model = SkillEntry
    fields = ['name']
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SkillEntryCreate, self).form_valid(form)

class SkillEntryUpdate(LoginRequiredMixin, UpdateView):
    model = SkillEntry
    fields = ['name']
    template_name = 'generic_form.html'
    success_url = '/app/'

class SkillEntryDelete(LoginRequiredMixin, DeleteView):
    model = SkillEntry
    template_name = 'generic_delete_form.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(SkillEntryDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

class ProjectEntryCreate(LoginRequiredMixin, CreateView):
    model = ProjectEntry 
    form_class = ProjectEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProjectEntryCreate, self).form_valid(form)

class ProjectEntryUpdate(LoginRequiredMixin, UpdateView):
    model = ProjectEntry 
    form_class = ProjectEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

class ProjectEntryDelete(LoginRequiredMixin, DeleteView):
    model = ProjectEntry 
    template_name = 'generic_delete_form.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(ProjectEntryDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

class ApplicationEntryCreate(LoginRequiredMixin, CreateView):
    model = ApplicationEntry
    form_class = ApplicationEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ApplicationEntryCreate, self).form_valid(form)

class ApplicationEntryUpdate(LoginRequiredMixin, UpdateView):
    model = ApplicationEntry
    form_class = ApplicationEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

class ApplicationEntryDelete(LoginRequiredMixin, DeleteView):
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

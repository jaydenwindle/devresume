from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from devresume_app.models import ProjectEntry, SkillEntry
from devresume_app.forms import ProjectEntryForm
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from requests import get

class ListProjects(LoginRequiredMixin, ListView):
    model = ProjectEntry
    template_name = 'list_projects.html'
    context_object_name="projects"

    def get_queryset(self):
        return self.request.user.projects.all

    def get_context_data(self, **kwargs):
        context = super(ListProjects, self).get_context_data(**kwargs)
        context['title'] = 'Projects'
        return context


class ProjectEntryCreate(LoginRequiredMixin, CreateView):
    model = ProjectEntry
    form_class = ProjectEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/resume_info#projects'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProjectEntryCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProjectEntryCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add a Project'
        return context

class ProjectEntryUpdate(LoginRequiredMixin, UpdateView):
    model = ProjectEntry
    form_class = ProjectEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/resume_info#projects'

    def get_context_data(self, **kwargs):
        context = super(ProjectEntryUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Update Project'
        return context

class ProjectEntryDelete(LoginRequiredMixin, DeleteView):
    model = ProjectEntry
    template_name = 'generic_delete_form.html'
    success_url = '/app/resume_info#projects'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(ProjectEntryDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

def ImportGithubProjects(request):
    username = request.user.username
    token = social = request.user.social_auth.get(provider='github').extra_data["access_token"]
    repos = get("http://api.github.com/users/" + username + "/repos", params={"access_token": token}).json()
    for repo in repos:
        name = repo["name"]
        skills = get("http://api.github.com/repos/" + username + "/" + name + "/languages", 
                     params={"access_token": token}).json()
        print(repo["description"])

        project, new = request.user.projects.get_or_create(name=name) 
        project.description = repo["description"] or ""
        project.gh_repo = repo["html_url"] or ""
        project.website = repo["homepage"] or repo["html_url"]
        project.stars = repo["stargazers_count"]
        project.save()
        for skill in skills:
            if skill != "documentation_url":
                s, new = SkillEntry.objects.get_or_create(name=skill)
                project.skills.add(s)

    return redirect(reverse("resume_info") + "#projects")

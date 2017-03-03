from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from devresume_app.models import ProjectEntry
from devresume_app.forms import ProjectEntryForm

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
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProjectEntryCreate, self).form_valid(form)

class ProjectEntryUpdate(LoginRequiredMixin, UpdateView):
    model = ProjectEntry
    form_class = ProjectEntryForm
    template_name = 'generic_form.html'

class ProjectEntryDelete(LoginRequiredMixin, DeleteView):
    model = ProjectEntry
    template_name = 'generic_delete_form.html'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(ProjectEntryDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from devresume_app.models import ApplicationEntry
from devresume_app.forms import ApplicationEntryForm
from django.shortcuts import render

class ListApplications(LoginRequiredMixin, ListView):
    model = ApplicationEntry
    template_name = 'list_applications.html'
    context_object_name="applications"

    def get_queryset(self):
        return self.request.user.applications.all

    def get_context_data(self, **kwargs):
        context = super(ListApplications, self).get_context_data(**kwargs)
        context['title'] = 'Applications'
        return context 

class ApplicationEntryCreate(LoginRequiredMixin, CreateView):
    model = ApplicationEntry
    form_class = ApplicationEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/applications'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ApplicationEntryCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ApplicationEntryCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add an Application'
        return context

class ApplicationEntryUpdate(LoginRequiredMixin, UpdateView):
    model = ApplicationEntry
    form_class = ApplicationEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/applications'

    def get_context_data(self, **kwargs):
        context = super(ApplicationEntryUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Update Application'
        return context

class ApplicationEntryDelete(LoginRequiredMixin, DeleteView):
    model = ApplicationEntry
    template_name = 'generic_delete_form.html'
    success_url = '/app/applications'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(ApplicationEntryDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

def ViewApplicationResume(request, pk):
    app = ApplicationEntry.objects.get(pk=pk)
    print(app.jobs.all().order_by('-similarity')[:3])
    return render(request, "resume.html",{
        "user": app.user,
        "projects": app.projects.all().order_by('-similarity')[:3],
        "work_history": app.jobs.all().order_by('-similarity')[:3],
        "education": app.education.all().order_by('-similarity')[:3]
    })

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from dr_app.models import Application
from dr_app.forms import ApplicationForm
from django.shortcuts import render

class ListApplications(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'list_applications.html'
    context_object_name="applications"

    def get_queryset(self):
        return self.request.user.applications.all

    def get_context_data(self, **kwargs):
        context = super(ListApplications, self).get_context_data(**kwargs)
        context['title'] = 'Applications'
        return context 

class ApplicationCreate(LoginRequiredMixin, CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'generic_form.html'
    success_url = '/app/applications'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ApplicationCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ApplicationCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add an Application'
        return context

    def get_form_kwargs(self):
        kwargs = super(ApplicationCreate, self).get_form_kwargs()
        kwargs['request'] = self.request 

        return kwargs

class ApplicationUpdate(LoginRequiredMixin, UpdateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'generic_form.html'
    success_url = '/app/applications'

    def get_context_data(self, **kwargs):
        context = super(ApplicationUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Update Application'
        return context

class ApplicationDelete(LoginRequiredMixin, DeleteView):
    model = Application
    template_name = 'generic_delete_form.html'
    success_url = '/app/applications'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(ApplicationDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

def ViewApplicationResume(request, pk):
    app = Application.objects.get(pk=pk)
    print(app.jobs.all().order_by('-similarity')[:3])
    return render(request, "resume.html",{
        "user": app.user,
        "projects": app.projects.all().order_by('-similarity')[:3],
        "work_history": app.jobs.all().order_by('-similarity')[:3],
        "education": app.education.all().order_by('-similarity')[:3]
    })

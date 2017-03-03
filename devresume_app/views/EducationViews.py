from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from devresume_app.models import EducationEntry
from devresume_app.forms import EducationEntryForm

class ListEducation(LoginRequiredMixin, ListView):
    model = EducationEntry
    template_name = 'list_education.html'
    context_object_name="education"

    def get_queryset(self):
        return self.request.user.education.all

    def get_context_data(self, **kwargs):
        context = super(ListEducation, self).get_context_data(**kwargs)
        context['title'] = 'Education'
        return context

class EducationEntryCreate(LoginRequiredMixin, CreateView):
    model = EducationEntry
    form_class = EducationEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/education'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EducationEntryCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EducationEntryCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add an Education Entry'
        return context

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

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from dr_app.models import Education
from dr_app.forms import EducationForm

class ListEducation(LoginRequiredMixin, ListView):
    model = Education
    template_name = 'list_education.html'
    context_object_name="education"

    def get_queryset(self):
        return self.request.user.education.all

    def get_context_data(self, **kwargs):
        context = super(ListEducation, self).get_context_data(**kwargs)
        context['title'] = 'Education'
        return context

class EducationCreate(LoginRequiredMixin, CreateView):
    model = Education
    form_class = EducationForm
    template_name = 'generic_form.html'
    success_url = '/app/resume_info'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EducationCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EducationCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add an Education '
        return context

class EducationUpdate(LoginRequiredMixin, UpdateView):
    model = Education
    form_class = EducationForm
    template_name = 'generic_form.html'
    success_url = '/app/resume_info'

    def get_context_data(self, **kwargs):
        context = super(EducationUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Update Education '
        return context

class EducationDelete(LoginRequiredMixin, DeleteView):
    model = Education
    template_name = 'generic_delete_form.html'
    success_url = '/app/resume_info'

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(EducationDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

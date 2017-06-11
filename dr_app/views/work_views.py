from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from dr_app.models import Work
from dr_app.forms import WorkForm

class ListWorkHistory(LoginRequiredMixin, ListView):
    model = Work
    template_name = 'list_work_history.html'
    context_object_name="work_history"

    def get_queryset(self):
        return self.request.user.work_history.all

    def get_context_data(self, **kwargs):
        context = super(ListWorkHistory, self).get_context_data(**kwargs)
        context['title'] = 'Work History'
        return context

class AddWorkHistory(LoginRequiredMixin, CreateView):
    model = Work
    form_class = WorkForm
    template_name = 'generic_form.html'
    success_url = '/app/resume_info/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddWorkHistory, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AddWorkHistory, self).get_context_data(**kwargs)
        context['title'] = 'Add Work History'
        return context

class EditWorkHistory(LoginRequiredMixin, UpdateView):
    model = Work
    form_class = WorkForm
    template_name = 'generic_form.html'
    success_url = '/app/resume_info/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EditWorkHistory, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(EditWorkHistory, self).get_context_data(**kwargs)
        context['title'] = 'Update Work History'
        return context

class DeleteWorkHistory(LoginRequiredMixin, DeleteView):
    model = Work
    template_name = 'generic_delete_form.html'
    success_url = '/app/work_history'

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(WorkDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

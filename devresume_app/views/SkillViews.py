from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from devresume_app.models import SkillEntry
from devresume_app.forms import SkillEntryForm

class SkillEntryCreate(LoginRequiredMixin, CreateView):
    model = SkillEntry
    form_class = SkillEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SkillEntryCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SkillEntryCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add a new Skill'
        return context

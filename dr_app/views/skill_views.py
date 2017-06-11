from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from dr_app.models import Skill
from dr_app.forms import SkillForm

class SkillCreate(LoginRequiredMixin, CreateView):
    model = Skill
    form_class = SkillForm
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SkillCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(SkillCreate, self).get_context_data(**kwargs)
        context['title'] = 'Add a new Skill'
        return context

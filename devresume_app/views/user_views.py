from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from devresume_app.models import User
from devresume_app.forms import UserForm

class UserInfoUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'generic_form.html'
    success_url = '/app/'

    def get_context_data(self, **kwargs):
        context = super(UserInfoUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Edit Profile'
        return context

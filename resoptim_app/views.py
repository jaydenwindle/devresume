from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import UpdateView, CreateView, DeleteView
from models import WorkEntry 

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    if request.user.is_authenticated():
        return render(request, 'dashboard.html', {
            'user': request.user,
            'work_entries': request.user.work.all(),
            'education_entries': request.user.education.all(),
            'social_profiles': request.user.profiles.all(),
            'skill_entries': request.user.skills.all()
        })
    else: 
        return redirect('login')

class WorkEntryCreate(CreateView):
    model = WorkEntry 
    fields = ['company', 'position', 'summary']
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WorkEntryCreate, self).form_valid(form)
        

class WorkEntryUpdate(UpdateView):
    model = WorkEntry 
    fields = ['company', 'position', 'summary']
    template_name = 'generic_form.html'
    success_url = '/app/'

class WorkEntryDelete(DeleteView):
    model = WorkEntry 
    template_name = 'delete_work_entry.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(WorkEntryDelete, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        return obj

def landingPage(request):
    return render(request, 'index.html', {
        'user':request.user
    })


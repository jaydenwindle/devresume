from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import UpdateView, CreateView
from models import WorkEntry 

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    if request.user.is_authenticated():
        return render(request, 'dashboard.html', {
            'user': request.user,
            'work_entries': request.user.work.all()
        })
    else: 
        return redirect('login')

class WorkEntryCreate(CreateView):
    model = WorkEntry 
    fields = ['company', 'position', 'summary']
    template_name = 'generic_form.html'
    success_url = '/app/'

class WorkEntryUpdate(UpdateView):
    model = WorkEntry 
    fields = ['company', 'position', 'summary']
    template_name = 'generic_form.html'
    success_url = '/app/'

def landingPage(request):
    return render(request, 'index.html', {
        'user':request.user
    })


from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    if request.user.is_authenticated():
        return render(request, 'index.html')
    else: 
        return redirect('login')

def landingPage(request):
    return render(request, 'index.html')

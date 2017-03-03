from django.shortcuts import render, redirect

def index(request):
    if request.user.is_authenticated():
        return render(request, 'dashboard.html', { "title": "Dashboard", "id": request.user.id });
    else:
        return redirect('landingpage')

def resume_info(request):
    return render(request, 'resume_info.html', {"title": "Resume Info"});

def landingPage(request):
    return render(request, 'index.html', {
        'user': request.user
    })

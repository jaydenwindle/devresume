from django.shortcuts import render, redirect
from requests import get

def index(request):
    if request.user.is_authenticated():
        return render(request, 'dashboard.html', { "title": "Dashboard", "id": request.user.id });
    else:
        return redirect('landingpage')

def resume_info(request):
    return render(request, 'resume_info.html', {
        "title": "Resume Info", 
        "projects": request.user.projects.all(),
        "work_history": request.user.work_history.all(),
        "education": request.user.education.all()
    })

def landingPage(request):
    return render(request, 'index.html', {
        'user': request.user
    })

def job_list(request):
    query = request.GET.get('q', 'developer')
    job_list = get("http://api.indeed.com/ads/apisearch", params={
        "publisher": 9978236252243350,
        "format": "json",
        "v": 2,
        "q": request.GET.get('q', 'developer'),
        "l": request.user.location,
        "co": "ca",
        "userip": request.META['REMOTE_ADDR'],
        "useragent": request.META['HTTP_USER_AGENT']
    }).json()

    return render(request, "job_list.html", {
        "title": "Find a Job", 
        "query": query,
        "job_list": job_list["results"]
    });

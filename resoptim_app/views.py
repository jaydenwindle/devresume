from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from forms import WorkEntryForm, EducationEntryForm, ProjectEntryForm, ApplicationEntryForm
from models import WorkEntry, EducationEntry,SocialProfile, SkillEntry, ProjectEntry, ApplicationEntry, User
from collections import Counter
import math
import collections
import urllib2, base64
import json


# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    if request.user.is_authenticated():
        return render(request, 'dashboard.html', {
            'user': request.user,
            'work_entries': request.user.work.all(),
            'education_entries': request.user.education.all(),
            'social_profiles': request.user.profiles.all(),
            'project_entries': request.user.projects.all(),
            'skill_entries': request.user.skills.all(),
            'application_entries': request.user.applications.all(),
        })
    else:
        return redirect('login')

def resume(request, pk):

    def array_similarity(c1, c2):
        terms = set(c1).union(c2)
        dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
        magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
        magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
        return dotprod / (magA * magB)


    if request.user.is_authenticated():
        renderDict = {
            'user': request.user,
        }
        app = Counter(ApplicationEntry.objects.get(pk=pk).desired_skills.all())

        # match jobs
        job_history = WorkEntry.objects.filter(user=request.user).all()
        sorted_jobs = {}
        for item in job_history:
            counter = Counter(item.skills.all())
            sorted_jobs[array_similarity(app,counter)] = item

        for i in range(3):
            renderDict['job' + str(i)] = sorted_jobs[max(sorted_jobs)]
            del sorted_jobs[max(sorted_jobs.keys())]
            renderDict['job' + str(i) + "skills"] = renderDict['job' + str(i)].skills.all()
            if len(sorted_jobs) == 0:
                break;

        # match projects
        job_history = WorkEntry.objects.filter(user=request.user).all()
        sorted_projects = {}
        for item in job_history:
            counter = Counter(item.skills.all())
            sorted_projects[array_similarity(app,counter)] = item
            print sorted_projects[array_similarity(app,counter)]


        for i in range(3):
            renderDict['project' + str(i)] = sorted_projects[max(sorted_projects)]
            del sorted_projects[max(sorted_projects.keys())]
            renderDict['project' + str(i) + "skills"] = renderDict['job' + str(i)].skills.all()
            if len(sorted_projects) == 0:
                break;

        return render(request, 'resume.html', renderDict)
    else:
        return redirect('login')

class WorkEntryCreate(LoginRequiredMixin, CreateView):
    model = WorkEntry
    form_class = WorkEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(WorkEntryCreate, self).form_valid(form)

class WorkEntryUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    model = WorkEntry
    form_class = WorkEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

class WorkEntryDelete(LoginRequiredMixin, DeleteView):
    model = WorkEntry
    template_name = 'generic_delete_form.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(WorkEntryDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

class EducationEntryCreate(LoginRequiredMixin, CreateView):
    model = EducationEntry
    form_class = EducationEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EducationEntryCreate, self).form_valid(form)

class EducationEntryUpdate(LoginRequiredMixin, UpdateView):
    model = EducationEntry
    form_class = EducationEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

class EducationEntryDelete(LoginRequiredMixin, DeleteView):
    model = EducationEntry
    template_name = 'generic_delete_form.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(EducationEntryDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

class SocialProfileCreate(LoginRequiredMixin, CreateView):
    model = SocialProfile
    fields = ['network','username','url']
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SocialProfileCreate, self).form_valid(form)

class SocialProfileUpdate(LoginRequiredMixin, UpdateView):
    model = SocialProfile
    fields = ['network','username','url']
    template_name = 'generic_form.html'
    success_url = '/app/'

class SocialProfileDelete(LoginRequiredMixin, DeleteView):
    model = SocialProfile
    template_name = 'generic_delete_form.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(SocialProfileDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

class SkillEntryCreate(LoginRequiredMixin, CreateView):
    model = SkillEntry
    fields = ['name']
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(SkillEntryCreate, self).form_valid(form)

class SkillEntryUpdate(LoginRequiredMixin, UpdateView):
    model = SkillEntry
    fields = ['name']
    template_name = 'generic_form.html'
    success_url = '/app/'

class SkillEntryDelete(LoginRequiredMixin, DeleteView):
    model = SkillEntry
    template_name = 'generic_delete_form.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(SkillEntryDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

class ProjectEntryCreate(LoginRequiredMixin, CreateView):
    model = ProjectEntry
    form_class = ProjectEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProjectEntryCreate, self).form_valid(form)

class ProjectEntryUpdate(LoginRequiredMixin, UpdateView):
    model = ProjectEntry
    form_class = ProjectEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

class ProjectEntryDelete(LoginRequiredMixin, DeleteView):
    model = ProjectEntry
    template_name = 'generic_delete_form.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(ProjectEntryDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

class ApplicationEntryCreate(LoginRequiredMixin, CreateView):
    model = ApplicationEntry
    form_class = ApplicationEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ApplicationEntryCreate, self).form_valid(form)

class ApplicationEntryUpdate(LoginRequiredMixin, UpdateView):
    model = ApplicationEntry
    form_class = ApplicationEntryForm
    template_name = 'generic_form.html'
    success_url = '/app/'

class ApplicationEntryDelete(LoginRequiredMixin, DeleteView):
    model = ApplicationEntry
    template_name = 'generic_delete_form.html'
    success_url = '/app/'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(ApplicationEntryDelete, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj

def landingPage(request):
    return render(request, 'index.html', {
        'user':request.user
    })

# //====================GITHUB INFORMATION=====================//
def githubProfile():
    userName = raw_input("Enter user github name: ")
    userDict = {}
    username = "atlasmaxima"
    password = "389c60b741df216a31263bcee43d0769b6d916a0"
    request = urllib2.Request("https://api.github.com/users/"+userName)
    base64string = base64.b64encode('%s:%s' % (username, password))
    request.add_header("Authorization", "Basic %s" % base64string)
    result = urllib2.urlopen(request)
    readFile = result.read()
    jsonLoads = json.loads(readFile)
    profileBasic = json.dumps(jsonLoads, indent=2)

    # update dictionary
    userDict.update({'blog': jsonLoads['blog'], 'location': jsonLoads['location'],
                     'name': jsonLoads['name'], 'company': jsonLoads['company'],
                     'bio':jsonLoads['bio'], 'profile_picture':jsonLoads['avatar_url']})
    # print(json.dumps(userDict, indent=4))

    repoDict = {}
    totalList = []
    # User Repository
    reposURL = jsonLoads['repos_url']
    requestRepo = urllib2.Request(reposURL)
    requestRepo.add_header("Authorization", "Basic %s" % base64string)
    resultRepo = urllib2.urlopen(requestRepo)
    readFile = resultRepo.read()
    countRepo = 0
    for i, repo in enumerate(json.loads(readFile), 1):
        countRepo +=1
        dumpRepo = json.dumps(repo, indent=4)
        # print(dumpRepo)
        name = repo['name']
        language = repo['language']
        description = repo['description']
        stargazers_count = repo['stargazers_count']
        repo = 'Repo%d' % i
        repoDict[repo] = {'name': name}
        if stargazers_count != 0:
            repoDict.update({'stargazers_count': stargazers_count})
        if language != "None":
            repoDict.update({'language': language})
        if description != "None":
            repoDict.update({'description': description})
        totalList.append(repoDict)
    #
    # print("The total repo from " + userDict['name'] + " is ")
    # print(totalList[0])

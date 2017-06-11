from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from views import *
from .models import *

admin.autodiscover()

urlpatterns = [

    # Static views
    url(r'^$', index, name='dashboard'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^resume_info/$', resume_info, name='resume_info'),
    url(r'^find_jobs/$', job_list, name='job_list'),

    # User views
    url(r'^profile/edit/$', UserInfoUpdate.as_view(), name='edit_user_profile'),

    # Work views
    url(r'^work_history/add/$', AddWorkHistory.as_view(), name='add_work_history'),
    url(r'^work_history/(?P<pk>[\w-]+)/edit/$', EditWorkHistory.as_view(), name='edit_work_history'),
    url(r'^work_history/(?P<pk>[\w-]+)/delete/$', DeleteWorkHistory.as_view(), name='delete_work_history'),

    # Education views
    url(r'^education/add/$', EducationCreate.as_view(), name='create_education_entry'),
    url(r'^education/(?P<pk>[\w-]+)/edit/$', EducationUpdate.as_view(), name='update_education_entry'),
    url(r'^education/(?P<pk>[\w-]+)/delete/$', EducationDelete.as_view(), name='delete_education_entry'),

    # Skill views
    url(r'^skill/add/$', SkillCreate.as_view(), name='create_skill_entry'),

    # Project views
    url(r'^projects/add/$', ProjectCreate.as_view(), name='create_project_entry'),
    url(r'^projects/(?P<pk>[\w-]+)/edit/$', ProjectUpdate.as_view(), name='edit_project_entry'),
    url(r'^projects/(?P<pk>[\w-]+)/delete/$', ProjectDelete.as_view(), name='delete_project_entry'),
    url(r'^projects/import/$', ImportGithubProjects, name='import_github_projects'),

    # Application views
    url(r'^applications/$', ListApplications.as_view(), name='list_applications'),
    url(r'^applications/create/$', ApplicationCreate.as_view(), name='create_application_entry'),
    url(r'^applications/(?P<pk>[\w-]+)/edit/$', ApplicationUpdate.as_view(), name='edit_application_entry'),
    url(r'^applications/(?P<pk>[\w-]+)/delete/$', ApplicationDelete.as_view(), name='delete_application_entry'),
    url(r'^applications/(?P<pk>[\w-]+)/view_resume/$', ViewApplicationResume, name='view_application_resume'),
]

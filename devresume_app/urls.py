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

    # User views
    url(r'^profile/(?P<pk>[\w-]+)/edit/$', UserInfoUpdate.as_view(), name='edit_user_profile'),

    # Work views
    url(r'^work_history/$', ListWorkHistory.as_view(), name='list_work_history'),
    url(r'^work_history/add/$', AddWorkHistory.as_view(), name='add_work_history'),
    url(r'^work_history/(?P<pk>[\w-]+)/edit/$', EditWorkHistory.as_view(), name='edit_work_history'),
    url(r'^work_history/(?P<pk>[\w-]+)/delete/$', DeleteWorkHistory.as_view(), name='delete_work_history'),

    # Education views
    url(r'^education/$', ListEducation.as_view(), name='list_education'),
    url(r'^education/add/$', EducationEntryCreate.as_view(), name='create_education_entry'),
    url(r'^education/(?P<pk>[\w-]+)/edit/$', EducationEntryUpdate.as_view(), name='update_education_entry'),
    url(r'^education/(?P<pk>[\w-]+)/delete/$', EducationEntryDelete.as_view(), name='delete_education_entry'),

    # Skill views
    url(r'^skill/add/$', SkillEntryCreate.as_view(), name='create_skill_entry'),

    # Project views
    url(r'^projects/$', ListProjects.as_view(), name='list_projects'),
    url(r'^projects/add/$', ProjectEntryCreate.as_view(), name='create_project_entry'),
    url(r'^projects/(?P<pk>[\w-]+)/edit/$', ProjectEntryUpdate.as_view(), name='edit_project_entry'),
    url(r'^projects/(?P<pk>[\w-]+)/delete/$', ProjectEntryDelete.as_view(), name='delete_project_entry'),
    url(r'^projects/import/$', ImportGithubProjects, name='import_github_projects'),

    # Application views
    url(r'^application/$', ListApplications.as_view(), name='list_applications'),
    url(r'^application/create/$', ApplicationEntryCreate.as_view(), name='create_application_entry'),
    url(r'^application/(?P<pk>[\w-]+)/edit/$', ApplicationEntryUpdate.as_view(), name='edit_application_entry'),
    url(r'^application/(?P<pk>[\w-]+)/delete/$', ApplicationEntryDelete.as_view(), name='delete_application_entry'),
    url(r'^application/(?P<pk>[\w-]+)/view_resume/$', index, name='view_application_resume'),
]

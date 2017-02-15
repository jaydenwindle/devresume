from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from views import UserInfoUpdate, WorkEntryUpdate, WorkEntryCreate, WorkEntryDelete, EducationEntryUpdate, EducationEntryCreate, EducationEntryDelete, SkillEntryUpdate, SkillEntryCreate, SkillEntryDelete, ProjectEntryCreate, ProjectEntryUpdate, ProjectEntryDelete, ApplicationEntryCreate, ApplicationEntryUpdate, ApplicationEntryDelete


admin.autodiscover()

import views

urlpatterns = [
    url(r'^$', views.index, name='dashboard'),
    # url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^profile/(?P<pk>[\w-]+)/edit/$', UserInfoUpdate.as_view(), name='edit_user_profile'),
    url(r'^work_entry/create/$', WorkEntryCreate.as_view(), name='create_work_entry'),
    url(r'^work_entry/(?P<pk>[\w-]+)/update/$', WorkEntryUpdate.as_view(), name='update_work_entry'),
    url(r'^work_entry/(?P<pk>[\w-]+)/delete/$', WorkEntryDelete.as_view(), name='delete_work_entry'),
    url(r'^education_entry/create/$', EducationEntryCreate.as_view(), name='create_education_entry'),
    url(r'^education_entry/(?P<pk>[\w-]+)/update/$', EducationEntryUpdate.as_view(), name='update_education_entry'),
    url(r'^education_entry/(?P<pk>[\w-]+)/delete/$', EducationEntryDelete.as_view(), name='delete_education_entry'),
    url(r'^create_skill_entry/$', SkillEntryCreate.as_view(), name='create_skill_entry'),
    url(r'^update_skill_entry/(?P<pk>[\w-]+)$', SkillEntryUpdate.as_view(), name='update_skill_entry'),
    url(r'^delete_skill_entry/(?P<pk>[\w-]+)$', SkillEntryDelete.as_view(), name='delete_skill_entry'),
    url(r'^create_project_entry/$', ProjectEntryCreate.as_view(), name='create_project_entry'),
    url(r'^update_project_entry/(?P<pk>[\w-]+)$', ProjectEntryUpdate.as_view(), name='update_project_entry'),
    url(r'^delete_project_entry/(?P<pk>[\w-]+)$', ProjectEntryDelete.as_view(), name='delete_project_entry'),
    url(r'^create_application_entry/$', ApplicationEntryCreate.as_view(), name='create_application_entry'),
    url(r'^update_application_entry/(?P<pk>[\w-]+)$', ApplicationEntryUpdate.as_view(), name='update_application_entry'),
    url(r'^delete_application_entry/(?P<pk>[\w-]+)$', ApplicationEntryDelete.as_view(), name='delete_application_entry'),
    url(r'^view_application_resume/(?P<pk>[\w-]+)$', views.resume, name='view_application_resume'),
    url(r'^import_gh_projects/$', views.ghImport, name='import_gh_projects'),
    
]

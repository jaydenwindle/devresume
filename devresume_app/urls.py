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
    url(r'^resume_info/$', views.resume_info, name='resume_info'),
    url(r'^profile/(?P<pk>[\w-]+)/edit/$', UserInfoUpdate.as_view(), name='edit_user_profile'),
    url(r'^work_entry/create/$', WorkEntryCreate.as_view(), name='create_work_entry'),
    url(r'^work_entry/(?P<pk>[\w-]+)/update/$', WorkEntryUpdate.as_view(), name='update_work_entry'),
    url(r'^work_entry/(?P<pk>[\w-]+)/delete/$', WorkEntryDelete.as_view(), name='delete_work_entry'),
    url(r'^education_entry/create/$', EducationEntryCreate.as_view(), name='create_education_entry'),
    url(r'^education_entry/(?P<pk>[\w-]+)/update/$', EducationEntryUpdate.as_view(), name='update_education_entry'),
    url(r'^education_entry/(?P<pk>[\w-]+)/delete/$', EducationEntryDelete.as_view(), name='delete_education_entry'),
    url(r'^skill/create/$', SkillEntryCreate.as_view(), name='create_skill_entry'),
    url(r'^skill/(?P<pk>[\w-]+)/update$', SkillEntryUpdate.as_view(), name='update_skill_entry'),
    url(r'^skill/(?P<pk>[\w-]+)/delete$', SkillEntryDelete.as_view(), name='delete_skill_entry'),
    url(r'^project/create/$', ProjectEntryCreate.as_view(), name='create_project_entry'),
    url(r'^project/(?P<pk>[\w-]+)/update/$', ProjectEntryUpdate.as_view(), name='update_project_entry'),
    url(r'^project/(?P<pk>[\w-]+)/delete/$', ProjectEntryDelete.as_view(), name='delete_project_entry'),
    url(r'^application/create/$', ApplicationEntryCreate.as_view(), name='create_application_entry'),
    url(r'^application/(?P<pk>[\w-]+)/update/$', ApplicationEntryUpdate.as_view(), name='update_application_entry'),
    url(r'^application/(?P<pk>[\w-]+)/delete/$', ApplicationEntryDelete.as_view(), name='delete_application_entry'),
    url(r'^application/(?P<pk>[\w-]+)/view_resume/$', views.resume, name='view_application_resume'),
]

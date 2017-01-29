from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from views import WorkEntryUpdate, WorkEntryCreate, WorkEntryDelete, EducationEntryUpdate, EducationEntryCreate, EducationEntryDelete,SocialProfileUpdate, SocialProfileCreate, SocialProfileDelete,SkillEntryUpdate, SkillEntryCreate, SkillEntryDelete


admin.autodiscover()

import views

urlpatterns = [
    url(r'^$', views.index, name='dashboard'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^create_work_entry/$', WorkEntryCreate.as_view(), name='create_work_entry'),
    url(r'^update_work_entry/(?P<pk>[\w-]+)$', WorkEntryUpdate.as_view(), name='update_work_entry'),
    url(r'^delete_work_entry/(?P<pk>[\w-]+)$', WorkEntryDelete.as_view(), name='delete_work_entry'),
    url(r'^create_education_entry/$', EducationEntryCreate.as_view(), name='create_education_entry'),
    url(r'^update_education_entry/(?P<pk>[\w-]+)$', EducationEntryUpdate.as_view(), name='update_education_entry'),
    url(r'^delete_education_entry/(?P<pk>[\w-]+)$', EducationEntryDelete.as_view(), name='delete_education_entry'),
    url(r'^create_social_profile/$', SocialProfileCreate.as_view(), name='create_social_profile'),
    url(r'^update_social_profile/(?P<pk>[\w-]+)$', SocialProfileUpdate.as_view(), name='update_social_profile'),
    url(r'^delete_social_profile/(?P<pk>[\w-]+)$', SocialProfileDelete.as_view(), name='delete_social_profile'),
    url(r'^create_skill_entry/$', SkillEntryCreate.as_view(), name='create_skill_entry'),
    url(r'^update_skill_entry/(?P<pk>[\w-]+)$', SkillEntryUpdate.as_view(), name='update_skill_entry'),
    url(r'^delete_skill_entry/(?P<pk>[\w-]+)$', SkillEntryDelete.as_view(), name='delete_skill_entry'),
    
]

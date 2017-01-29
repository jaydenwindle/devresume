from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from views import WorkEntryUpdate, WorkEntryCreate

admin.autodiscover()

import views

urlpatterns = [
    url(r'^$', views.index, name='dashboard'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^update_work_entry/(?P<pk>[\w-]+)$', WorkEntryUpdate.as_view(), name='update_work_entry'),
    url(r'^create_work_entry/$', WorkEntryCreate.as_view(), name='create_work_entry'),
]

from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin

admin.autodiscover()

import views

urlpatterns = [
    url(r'^$', views.index, name='app_index'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]

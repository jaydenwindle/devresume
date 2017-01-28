from django.conf.urls import url, include

from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = [
    url(r'^$', views.index, name='app_index'),
    url(r'^admin/', include(admin.site.urls)),
]

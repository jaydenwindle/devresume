from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import resoptim_app.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', resoptim_app.views.index, name='index'),
    url(r'^db', resoptim_app.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
]

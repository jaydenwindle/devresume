from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import resoptim_app.views, resoptim_app.urls

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', resoptim_app.views.index, name='index'),
    url(r'^app/', include(resoptim_app.urls)),
    url(r'^admin/', include(admin.site.urls)),
]

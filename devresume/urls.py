from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import devresume_app.views, devresume_app.urls

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', devresume_app.views.landingPage, name='landingpage'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include(devresume_app.urls)),
]

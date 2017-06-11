from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import dr_app.views, dr_app.urls
import dr_static.urls

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^', include(dr_static.urls)),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include(dr_app.urls)),
]

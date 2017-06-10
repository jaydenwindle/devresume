from django.conf.urls import url, include
from views import *

urlpatterns = [
    # Static views
    url(r'^$', landingPage, name='landingpage'),
]

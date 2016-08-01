from django.conf.urls import url

from django.contrib import admin
admin.autodiscover()

import gitlist.views

urlpatterns = [
    url(r'^$', gitlist.views.index, name='index'),
    url(r'^issues/', gitlist.views.issues, name='issues'),
]

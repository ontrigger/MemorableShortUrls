from django.urls import re_path

from urlshort import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^(?P<shortlink>[a-zA-Z0-9-_]+)$', views.redirect, name='shortlink'),
]

# coding: utf-8

from django.conf.urls import url
from .views import *

urlpatterns = [
    url('^$', index, name='index',),
    url('^accounts/profile/$', profile, name='profile',),
    url('^extra/data/', extra_data),
    url('^ssh/$', ssh, name='ssh',),
    url('^ssh/criar/$', ssh_criar, name='ssh_criar',),
    url('^ssh/iniciar/$', ssh_iniciar, name='ssh_iniciar'),
]

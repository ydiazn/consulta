# -*- encoding:utf-8 -*-
# -*- coding:utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^$', index, name='index'),
]

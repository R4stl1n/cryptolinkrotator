from django.urls import include, path
from django.contrib import admin

from . import views

handler404 = 'views.display404'

urlpatterns = [
	path(r'', views.index, name='index'),
    path(r'rotate/<rotate>', views.rotate, name='link_rotator'),

]
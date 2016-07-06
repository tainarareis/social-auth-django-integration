from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views
admin.autodiscover()

urlpatterns = [
   url(r'^$', views.home, name='home')
 ]

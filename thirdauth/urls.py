from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views
admin.autodiscover()

urlpatterns = [
   url(r'^', include('app.urls')),
   url(r'^admin/', include(admin.site.urls)),
   url(r'', include('social.apps.django_app.urls', namespace='social')),
   url('', include('django.contrib.auth.urls', namespace='auth')),
]

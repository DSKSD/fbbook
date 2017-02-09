from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', views.index, name = 'index'), 
    url(r'^webhook$', views.webhook, name='webhook')
    ]
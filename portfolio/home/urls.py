from django.contrib import admin
from django.urls import path, include
from home import views

# Dango admin customisation

admin.site.site_header = "Developer Funmi"
admin.site.site_title = "Welcome to Funmi's Dashboard"
admin.site.index_title = "Welcome to this Portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
]
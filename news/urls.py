from django.contrib import admin
from django.urls import path
from news import views

urlpatterns = [
    path('', views.index, name='index'),
    path('(?P<article_id>[0-9]+)', views.detail, name='detail'),
]


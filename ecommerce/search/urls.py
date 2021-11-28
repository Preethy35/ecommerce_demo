from django.contrib import admin
from django.urls import path,include
from . import views

app_name='search'

urlpatterns = [
    path('', views.SearchResult, name='SearchResult'),

]
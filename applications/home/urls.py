from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.IndexView.as_view()),
    path('vista/', views.PruebaListView.as_view()),
]
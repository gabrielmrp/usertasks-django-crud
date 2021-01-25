# subscriptions/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from usertasksapi import viewsets

urlpatterns = [
    path('user/', views.UserViewset.as_view()),
    path('user/<int:pk>/', views.UserViewset.as_view()),
]
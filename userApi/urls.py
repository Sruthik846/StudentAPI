
from django.urls import path
from . views import *

urlpatterns = [
    path('create/',RegisterAPIView.as_view()),
    path('all/',StudentAPIView.as_view()),
    path('edit/<int:pk>/',EditAPIView.as_view()),
    path('delete/<int:pk>/',DeleteAPIView.as_view()),
]

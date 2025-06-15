from django.urls import path
from . import views

path('', ProductView.as_view()),         # list & create
path('<int:pk>/', ProductView.as_view()) # retrieve, update, delete

  

 
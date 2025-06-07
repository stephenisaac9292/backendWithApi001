from django.urls import path, include 
from . import views

urlpatterns = [
    path('signup/', views.UserSignupAPIView.as_view(), name='UserSignupAPIView'),
    path('staff-signup/', views.StaffSignupAPIView.as_view(), name='StaffSignupAPIView'), 
   
]


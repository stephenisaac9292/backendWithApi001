from django.urls import path, include 

urlpatterns = [
    path('signup/', user_signup_view, name='user-signup'),
    path('staff-signup/', staff_signup_view, name='staff-signup'),
   
]``
from django.urls import path
from . import views

urlpatterns = [

    path('', views.ProductsListCreateAPIView.as_view()),
    path('<int:pk>/', views.ProductsDetailAPIView.as_view()),
    path('<int:pk>/update/', views.ProductsUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.ProductsDestroyAPIView.as_view()),

] 

  


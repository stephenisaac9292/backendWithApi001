from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from .serializers import UserSignupSerializer, StaffSignupSerializer

class UserSignupAPIView(generics.CreateAPIView):
    serializer_class = UserSignupSerializer
    permission_classes = [AllowAny]

class StaffSignupAPIView(generics.CreateAPIView):
    serializer_class = StaffSignupSerializer
    permission_classes = [AllowAny]
 
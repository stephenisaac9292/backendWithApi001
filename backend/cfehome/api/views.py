from django.shortcuts import render
from django.http import JsonResponse
from products.models import Products
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductsSerializer
# Create your views here.

@api_view(["POST", "PUT", "GET"])
def api_home(request, *args, **kwargs):
   serializer = ProductsSerializer(data = request.data)
   if serializer.is_valid(raise_exception = True):
      print(serializer.data)
   return Response(serializer.data)

     
 


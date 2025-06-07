from rest_framework import generics, serializers, permissions
from .models import Products
from .serializers import ProductsSerializer
from products.permissions import IsAuthenticated, IsCustomer, IsSeller, IsStaff



class ProductsDetailAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    authentication_classes = []
    permission_classes = [IsAuthenticated , IsCustomer| IsSeller | IsStaff]


class ProductsListCreateAPIView(generics.ListCreateAPIView): 
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    authentication_classes = []
    permission_classes = [IsAuthenticated , IsSeller | IsStaff]

    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)form 
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content= "No description available" 
        serializer.save(content=content)


class ProductsUpdateAPIView(generics.UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'pk'
    authentication_classes = []
    permission_classes = [IsAuthenticated , IsSeller | IsStaff]

    def perform_update (self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        
        if not content:
            content = title
        serializer.save(content=content) 


class ProductsDestroyAPIView(generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'pk'
    authentication_classes = []
    permission_classes = [IsAuthenticated, IsSeller | IsStaff]

    def perform_destroy (self, instance):
        super().perform_destroy(instance) 



 









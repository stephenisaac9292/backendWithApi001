from rest_framework import generics, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsSellerOnly
from .models import Product
from .serializers import ProductSerializer

class ProductView(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'  # optional; default is 'pk'

    def get_permissions(self):
        method = self.request.method
        if method == 'GET':
            if self.kwargs.get('pk'):
                return [IsAuthenticated()]  # optional: restrict single-view
            return [AllowAny()]  # public list
        elif method == 'POST':
            return [IsAuthenticated(), IsSellerOnly()]
        elif method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), IsSellerOnly()]
        return []

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

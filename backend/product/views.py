from rest_framework import generics


from .models import Product
from .serializers import ProductSerializers

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    def perform_create(self , serializer):
        # serializer.save(user = self.request.user)
        print (serializer.validated_data)
        serializer.save()
Product_List_create = ProductListCreateAPIView.as_view() # This is the same as the above class-based view, but it's a function-based view.
    
    
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    # lookup_field = 'id'
Product_detail = ProductDetailAPIView.as_view() # This is the same as the above class-based view, but it's a function-based view.

class ProductListAPIView(generics.ListAPIView):
    '''not used'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    # lookup_field = 'id'
Product_list = ProductListAPIView.as_view() # This is the same as the above class-based view, but it's a function-based view.
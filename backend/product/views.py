from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializers

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    def perform_create(self , serializer):
        # serializer.save(user = self.request.user)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content =content)
        print (serializer.validated_data)
Product_List_create = ProductListCreateAPIView.as_view() # This is the same as the above class-based view, but it's a function-based view.
    
    
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    # lookup_field = 'id'
Product_detail = ProductDetailAPIView.as_view()



class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
Product_delete = ProductDeleteAPIView.as_view()



class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            instance.save()
            
Product_update = ProductUpdateAPIView.as_view() # This is the same as the above class-based view, but it's a function-based view.





# make all the class-based views in one function-based view
@api_view(['GET', 'POST'])
def product_alt_view(request ,pk = None ,  *args , **kwargs):
    method = request.method
    if method =="GET":
        if pk is not None:
            #detail view
            # return Product_detail(request , pk)
            obj = get_object_or_404(Product , pk = pk) #if not found it will return 404
            data = ProductSerializers(obj , many = False).data
            '''
            this is the same as the above line
        
            queryset = Product.objects.filter(pk = pk)
            if not queryset.exists():
                return Response({"message" : "Not Found"}, status=404)
            
            '''
            return Response(data)
            
        else :
            # list view
            queryset = Product.objects.all()
            data = ProductSerializers(queryset , many = True).data
            return Response(data)
    elif method == "POST":
        serializer = ProductSerializers(data = request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get("title")
            content = serializer.validated_data.get("content")
            if content is None:
                content = title
            serializer.save(content =content)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
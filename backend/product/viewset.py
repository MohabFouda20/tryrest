from rest_framework import viewsets , mixins

from .models import Product 
from .serializers import ProductSerializers

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'
    
    
class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet):
    '''
    This viewset automatically provides `list` and `detail` actions.
    '''
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'
    
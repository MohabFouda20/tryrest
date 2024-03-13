# from django.shortcuts import render
# from django.http import JsonResponse  
# import json
from product.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.serializers import ProductSerializers

# Create your views here.
@api_view(['POST'])
def api_home(request , *args , **kwargs):
  
    serializer = ProductSerializers(data = request.data)
    if serializer.is_valid(raise_exception=True ):
        instance  = serializer.save()
        print(instance)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)
        
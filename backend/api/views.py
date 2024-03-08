# from django.shortcuts import render
from django.http import JsonResponse
import json
from product.models import Product

# Create your views here.
def api_home(request , *args , **kwargs):
    # this is before the product app 
    
    
    # print (request.GET) # get the query parameters (params)
    # print (request.POST)
    # body= request.body
    # data={}
    # try:
    #     data = json.loads(body) # convert json to python dictionary
    # except:
    #     pass
    # print (data)
    # print (request.headers)
    # # json.dumps(dict(request.headers))
    # data['params'] = dict(request.GET)
    # data['header'] = dict(request.headers) # get the header of the request
    # data['content_type'] = request.content_type # get the content type of the request
    
    
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price

    return JsonResponse(data)
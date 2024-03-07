# from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def api_home(request):
    
    
    return JsonResponse({"message": "Hi there , this is my first try to api response"})
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Product_List_create),
    path('<int:pk>/', views.Product_detail),
    path('update/<int:pk>/', views.Product_update),
    path('delete/<int:pk>/', views.Product_delete),
]

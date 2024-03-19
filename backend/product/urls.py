from django.urls import path
from . import views

urlpatterns = [
    path('', views.Product_List_create , name = 'product-list'),
    path('<int:pk>/', views.Product_detail , name = 'product-detail'),
    path('update/<int:pk>/', views.Product_update , name = 'product-update'),
    path('delete/<int:pk>/', views.Product_delete ),
]

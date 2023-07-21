
from django.urls import path
from peopleapi.apis.views import SuppliersAPI,ProductsAPI

urlpatterns = [
   
    path('suppliers/<int:pk>',SuppliersAPI.as_view(), name="supplier-by-id"),
    path('suppliers/',SuppliersAPI.as_view(),name="supplier-get"),
    path('products/<int:pk>',ProductsAPI.as_view(), name="product-by-id"),
    path('products/',ProductsAPI.as_view(),name="product-get")
  
]
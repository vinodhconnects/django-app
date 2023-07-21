
from django.urls import path
from peopleapi.apis.views import SuppliersAPI

urlpatterns = [
   
    path('suppliers/<int:pk>',SuppliersAPI.as_view(), name="supplier-by-id"),
    path('suppliers/',SuppliersAPI.as_view(),name="supplier-get"),
  
]
from django.shortcuts import render
from peopleapi.models import Product,Supplier
from rest_framework.decorators import api_view,APIView
from rest_framework.response import Response
from peopleapi.apis.serializers import ProductSerializer,SupplierSerializer
from rest_framework import status
class  ProductsAPI(APIView):

    def get(self,request,pk=None):
        if(pk==None):
            productlist=Product.objects.all()
            result=ProductSerializer(productlist,many=True,context={'request':request})
            return Response(result.data)
        else:
            try:
                item=Product.objects.get(pk=pk)
                return Response(ProductSerializer(item).data)
            except Product.DoesNotExist:
                return Response({'error':'No Content'}, status=status.HTTP_204_NO_CONTENT)

class  SuppliersAPI(APIView):

    def get(self,request,pk=None):
        if(pk==None):
            supplierlist=Supplier.objects.all()
            result=SupplierSerializer(supplierlist,many=True,context={'request':request})
            return Response(result.data)
        else:
            try:
                item=Supplier.objects.get(pk=pk)
                return Response(SupplierSerializer(item).data)
            except Supplier.DoesNotExist:
                return Response({'error':'No Content'}, status=status.HTTP_204_NO_CONTENT)
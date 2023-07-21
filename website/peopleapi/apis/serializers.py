from django.db.models import fields
from rest_framework import serializers
from peopleapi.models import Product,Supplier

class ProductSerializer(serializers.ModelSerializer):
    supplier = serializers.CharField(source='supplier.name')
    class Meta:
        model= Product
        fields = "__all__" 
        #exclude=['productid']   
    def validate(self,data):
        if data['price']<0:
            print('validated ', data['price'])
            raise serializers.ValidationError('Price is less than zero')
        else:
            return data

class SupplierSerializer(serializers.ModelSerializer):
    #products = serializers.StringRelatedField(many=True)
    # products = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='product-by-id'
    # )
    class Meta:
        model= Supplier
        fields= "__all__"
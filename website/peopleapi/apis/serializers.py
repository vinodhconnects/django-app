from django.db.models import fields
from rest_framework import serializers
from peopleapi.models import Product,Supplier

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
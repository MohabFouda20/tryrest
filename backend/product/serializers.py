from rest_framework import serializers

from rest_framework.reverse import reverse
from .models import Product
from . import validators 

class ProductSerializers(serializers.ModelSerializer):
    before = serializers.SerializerMethodField(read_only=True) # this is a custom field make sure to add the get_fieldname method
    url_update = serializers.SerializerMethodField(read_only=True) # this is a custom field make sure to add the get_fieldname method
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk')
    # email = serializers.EmailField(write_only = True) #custom field
    title  = serializers.CharField(validators=[validators.validate_title ,validators.unique_product_title])
    class Meta:
        model = Product
        fields = [
            # 'email', # this is a custom field
            # 'user',
            'url_update',# this is the url of the product update view
            'url', # this is the url of the product detail view
            'pk', # this is the primary key
            'title',
            'content',
            'price',
            'sale',
            'before'
        ]
        
        
    # def  create(self, validated_data): # this is a custom create method BECAUSE WE HAVE A CUSTOM FIELD "email"
    #     # email = validated_data.pop('email')
    #     obj = Product.objects.create(**validated_data)
    #     # print (email , obj)
    #     return obj
    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)
    
    # there is another validation method by the user
    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user= request.user
    #     qs = Product.objects.filter(user = user , title__iexact = value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already taken")
    #     return value
    
    
    
    def get_url_update(self, obj):
        # return f"/api/product/{obj.pk}/"
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-update", kwargs={'pk': obj.pk}, request=request )
    def get_before(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return "Custom value based on obj"
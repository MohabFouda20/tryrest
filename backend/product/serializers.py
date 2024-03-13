from rest_framework import serializers


from .models import Product


class ProductSerializers(serializers.ModelSerializer):
    before = serializers.SerializerMethodField(read_only=True) # this is a custom field make sure to add the get_fieldname method
    class Meta:
        model = Product
        fields = [
            'id', # this is the primary key
            'title',
            'content',
            'price',
            'sale',
            'before'
        ]
    def get_before(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return "Custom value based on obj"
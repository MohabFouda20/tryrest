from rest_framework import serializers


from .models import Product


class ProductSerializers(serializers.ModelSerializer):
    before = serializers.SerializerMethodField(read_only=True) # this is a custom field make sure to add the get_fieldname method
    class Meta:
        model = Product
        fields = [
            'title',
            'content',
            'price',
            'sale',
            'before'
        ]
    def get_before(self , obj): # obj is the instance of the model and the method name should be get_fieldname
        print (obj.id) # prin the id in the server console
        return "hello world"
from rest_framework import serializers

from rest_framework.reverse import reverse
from .models import Product


class ProductSerializers(serializers.ModelSerializer):
    before = serializers.SerializerMethodField(read_only=True) # this is a custom field make sure to add the get_fieldname method
    url_update = serializers.SerializerMethodField(read_only=True) # this is a custom field make sure to add the get_fieldname method
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk')
    class Meta:
        model = Product
        fields = [
            'url_update',# this is the url of the product update view
            'url', # this is the url of the product detail view
            'pk', # this is the primary key
            'title',
            'content',
            'price',
            'sale',
            'before'
        ]
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
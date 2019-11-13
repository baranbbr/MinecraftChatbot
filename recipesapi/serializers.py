from .models import Item
from rest_framework import serializers


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('id','itemTitle', 'craftingURL', 'itemDescription', 'itemIngredients')


class AllItemsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('id','itemTitle')





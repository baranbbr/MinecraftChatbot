from .models import Item #imported model
from rest_framework import serializers #serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML


class ItemSerializer(serializers.HyperlinkedModelSerializer):#declarazation of Serializer
    class Meta:
        model = Item #setting up the model, which data I want to serialize then
        fields = ('id','itemTitle', 'craftingURL', 'itemDescription', 'itemIngredients') #what exactly do I want to serialize


class AllItemsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('id','itemTitle')





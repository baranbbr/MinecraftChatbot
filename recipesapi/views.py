from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Item
from WebScrapingMinecraftRecipes.webscraping import GetWebInfo
from rest_framework import viewsets
from .serializers import ItemSerializer
from .serializers import AllItemsSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class AllItemsViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = AllItemsSerializer


def dataInput(request):
    itemsList = open('WebScrapingMinecraftRecipes/items.txt', 'r')
    lines = itemsList.readlines()
    for i in lines:
        item = i[:-1]
        print(item)
        recipesDATA = GetWebInfo()
        data = recipesDATA.get_craft_info(item)
        itemT = str(data[0])
        itemU = str(data[1])
        itemD = str(data[2])
        itemD = itemD[6:].strip('</span>')
        itemI = str(data[3][13:])
        insert = InsertData(itemT,itemU,itemD,itemI)

    return HttpResponse("Succesfully saved!")

def InsertData(itemTit, itemUrl, itemDesc, itemIng):
    itemSession = Item(itemTitle = itemTit, itemURL = itemUrl, itemDescription = itemDesc, itemIngredients= itemIng)
    itemSession.save()

def listOfItems():
    itemsList = open('WebScrapingMinecraftRecipes/items.txt', 'r')
    items = []
    lines = itemsList.readlines()
    for i in lines:
        items.append(i[:-1])
    return items
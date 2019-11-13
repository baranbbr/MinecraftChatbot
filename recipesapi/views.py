from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Item
from WebScrapingMinecraftRecipes.webscraping import GetWebInfo
from rest_framework import viewsets
from .serializers import ItemSerializer
from .serializers import AllItemsSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all() #querying the database for all items
    serializer_class = ItemSerializer #Passing queryset into the serializer, so that it gets converted into JSON and rendered

class AllItemsViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = AllItemsSerializer

#this function is the way how django works, in django framework it is called a View
#crated this function that will import all items into database
def dataInput(request):
    itemsList = open('WebScrapingMinecraftRecipes/items.txt', 'r')
    lines = itemsList.readlines() #get list of all items from textfile
    for i in lines:
        item = i[:-1] #get the name of an item
        print(item) #print it out just for the test
        recipesDATA = GetWebInfo() #declaration of Constructor, so i can interact with Baran's webscraping.py
        data = recipesDATA.get_craft_info(item) #finds the data for the item and insert it into list
        itemT = str(data[0])
        itemU = str(data[1])
        itemD = str(data[2])
        itemD = itemD[6:].strip('</span>')
        itemI = str(data[3][13:])
        insert = InsertData(itemT,itemU,itemD,itemI) #inserting data to the database

    return HttpResponse("Succesfully saved!")#returning http response on the website if everything worked, if not, there is an error

def InsertData(itemTit, itemUrl, itemDesc, itemIng):#function for inserting data to the database itself
    itemSession = Item(itemTitle = itemTit, itemURL = itemUrl, itemDescription = itemDesc, itemIngredients= itemIng)
    itemSession.save()


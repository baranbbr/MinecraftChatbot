from django.db import models


class Item(models.Model):#creates a model which is basically row in a database
    itemTitle = models.CharField(max_length=250)#creates columns for item title
    craftingURL = models.URLField(max_length=250)#creates columns for URL link
    itemDescription = models.TextField()#creates columns for item description
    itemIngredients = models.TextField()#creates columns for item ingredients

    def __str__(self): #method just tells Django what to print when it needs to print out an instance of the Item model.
        return self.title



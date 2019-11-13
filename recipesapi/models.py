from django.db import models


class Item(models.Model):
    itemTitle = models.CharField(max_length=250)
    craftingURL = models.URLField(max_length=250)
    itemDescription = models.TextField()
    itemIngredients = models.TextField()

    def __str__(self):
        return self.title



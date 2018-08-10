
from django.db import models


from location.models import Location
from people.models import Participant


class ItemCategory(models.Model):
    label = models.CharField(max_length=200)

    def __str__(self):
        return self.label


class Item(models.Model):
    label = models.CharField(max_length=200)
    owner = models.ForeignKey(Participant)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    categories = models.ManyToManyField(ItemCategory)

    def __str__(self):
        return self.label


class ItemPicture(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    label = models.CharField(max_length=200)
    picture = models.FileField('Picture', upload_to='pictures/items_pictures', blank=True)

    def __str__(self):
        return self.label

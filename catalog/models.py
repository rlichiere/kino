
from django.db import models


from location.models import Location
from people.models import Participant

from core.generic.model import GenericModelInterface


class ItemCategory(models.Model, GenericModelInterface):
    label = models.CharField(max_length=200)

    """ Abstract implementations """

    def __str__(self):
        return self.label


class Item(models.Model, GenericModelInterface):
    label = models.CharField(max_length=200)
    owner = models.ForeignKey(Participant)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    categories = models.ManyToManyField(ItemCategory)

    """ Abstract implementations """

    def __str__(self):
        return self.label


class ItemPicture(models.Model, GenericModelInterface):
    label = models.CharField(max_length=200)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    picture = models.FileField('Picture', upload_to='pictures/items_pictures', blank=True)

    """ Abstract implementations """

    def __str__(self):
        return self.label

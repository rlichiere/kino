
from django.db import models
from django.contrib.auth.models import User

from location.models import Location


class Contact(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)           # external contacts are not linked to a User account
    referer = models.ForeignKey(User, related_name='referer')              # the referer is the 'creator' of the Contact
    pseudo = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    phone_mobile = models.CharField(max_length=200, blank=True)
    phone_static = models.CharField(max_length=200, blank=True)
    facebook = models.CharField(max_length=200, blank=True)
    location = models.ForeignKey(Location, null=True, blank=True)
    picture = models.FileField('Photo', upload_to='pictures/contacts', blank=True)

    def __str__(self):
        return self.pseudo

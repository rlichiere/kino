
from django.db import models
from django.contrib.auth.models import User

from location.models import Location
from constants import PARTICIPANT_PREFERRED_METHODS_OF_CONTACT


class Capacity(models.Model):
    label = models.CharField(max_length=200)

    def __str__(self):
        return self.label


class Participant(models.Model):
    user = models.OneToOneField(User, null=True, blank=True)        # external contacts are not linked to a User account
    referer = models.ForeignKey(User, related_name='referer')          # the referer is the 'creator' of the participant
    pseudo = models.CharField(max_length=200, unique=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    phone_mobile = models.CharField(max_length=200, blank=True)
    phone_static = models.CharField(max_length=200, blank=True)
    facebook = models.CharField(max_length=200, blank=True)
    preferred_method_of_contact = models.CharField(choices=PARTICIPANT_PREFERRED_METHODS_OF_CONTACT.as_choices(),
                                                   max_length=200, null=True, blank=True)
    location = models.ForeignKey(Location, null=True, blank=True)
    picture = models.FileField('Photo', upload_to='pictures/contacts', blank=True)
    capacities = models.ManyToManyField(Capacity, blank=True)

    def __str__(self):
        return self.pseudo

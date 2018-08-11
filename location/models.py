
from django.db import models

from core.generic.model import GenericModelInterface
from core.utils.gps import gps_utils


class Country(models.Model, GenericModelInterface):
    label = models.CharField(max_length=200)
    flag_file = models.FileField('Flag file', upload_to='flags', blank=True)

    """ Abstract implementations """

    def __str__(self):
        return self.label


class PostalAddress(models.Model, GenericModelInterface):
    name_on_bell = models.CharField(max_length=200, blank=True)
    floor = models.IntegerField(null=True, blank=True)
    number_in_street = models.PositiveIntegerField(null=True, blank=True)
    block = models.CharField(max_length=200, blank=True)
    street = models.CharField(max_length=200)
    postal_code = models.IntegerField()
    city = models.CharField(max_length=200)
    country = models.ForeignKey(Country)
    is_public = models.BooleanField(default=False)

    def as_str(self, expanded=False):
        _address = ''
        if expanded:
            _address += 'Bell %s' % self.name_on_bell if self.name_on_bell else ''

            if self.floor not in ['', None]:
                _address += 'At ' if _address == '' else ' at '
                _address += 'floor %s' % self.floor

            if self.number_in_street:
                _address += 'N. ' if _address == '' else ', n. '
                _address += '%s' % self.number_in_street

            if self.block:
                _address += 'At ' if _address == '' else ', at '
                _address += 'block %s' % self.block

            if _address != '':
                _address += ', '

        _address += '%s, %s %s - %s' % (self.street, self.postal_code, self.city, self.country)
        return _address

    """ Abstract implementations """

    def __str__(self):
        return self.as_str()


class GPSAddress(models.Model, GenericModelInterface):
    _gps_lat = models.CharField(max_length=10)         # from  -90.0 to  90.0
    _gps_lon = models.CharField(max_length=10)         # from -180.0 to 180.0
    is_public = models.BooleanField(default=False)

    @property
    def latitude(self):
        return self.getLatitude()

    @property
    def longitude(self):
        return self.getLongitude()

    @property
    def coordinates(self):
        return self.getCoordinates()

    def getLatitude(self, format=None):
        return gps_utils.format(lat=self._gps_lat, format=format)

    def getLongitude(self, format=None):
        return gps_utils.format(lon=self._gps_lon, format=format)

    def getCoordinates(self, format=None):
        return gps_utils.format(lat=self._gps_lat, lon=self._gps_lon, format=format)

    def updateCoordinates(self, latitude=None, longitude=None):
        _changed = False
        if latitude is not None:
            _changed = True
            self._gps_lat = latitude
        if longitude is not None:
            _changed = True
            self._gps_lon = longitude
        if _changed:
            self.save()

    def as_label(self):
        return self.coordinates

    """ Abstract implementations """

    def __str__(self):
        return self.as_label()


class Location(models.Model, GenericModelInterface):
    label = models.CharField(max_length=200)
    postal_address = models.ForeignKey(PostalAddress, null=True, blank=True)
    gps_address = models.ForeignKey(GPSAddress, null=True, blank=True)
    picture = models.FileField('Picture', upload_to='pictures/locations', blank=True)
    is_public = models.BooleanField(default=False)

    """ Abstract implementations """

    def __str__(self):
        return self.label


class RoadbookAddress(models.Model, GenericModelInterface):
    arriving_by = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='roadbook_address')
    is_public = models.BooleanField(default=False)

    """ Abstract implementations """

    def __str__(self):
        return self.arriving_by

    @staticmethod
    def distance(steps, as_label=None):
        _distance = 0
        for _s in steps:
            if not _s.distance > 0:
                continue
            _distance += _s.distance

        if as_label is None:
            return _distance

        return '%s (todo : convert as km and m)' % _distance

    @staticmethod
    def duration(steps, as_label=None):
        _duration = 0
        for _s in steps:
            if not _s.duration > 0:
                continue
            _duration += _s.duration

        if as_label is None:
            return _duration

        return '%s (todo : convert as hours and minutes)' % _duration


class RoadbookStep(models.Model, GenericModelInterface):
    rank = models.PositiveIntegerField()
    at_description = models.CharField(max_length=200)
    direction_to_follow = models.CharField(max_length=200)
    roadbook = models.ForeignKey(RoadbookAddress, on_delete=models.CASCADE, related_name='roadbook_steps')
    picture = models.FileField('Picture', upload_to='pictures/roadbooks_steps', blank=True)

    distance = models.IntegerField(blank=True, null=True)
    duration = models.DurationField(blank=True, null=True)

    """ Abstract implementations """

    def __str__(self):
        return self.at_description

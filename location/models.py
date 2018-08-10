
from django.db import models


class Country(models.Model):
    label = models.CharField(max_length=200)
    flag_file = models.FileField('Flag file', upload_to='flags', blank=True)

    def __str__(self):
        return self.label


class PostalAddress(models.Model):
    name_on_bell = models.CharField(max_length=200, blank=True)
    floor = models.IntegerField(null=True, blank=True)
    number_in_street = models.PositiveIntegerField(null=True, blank=True)
    block = models.CharField(max_length=200, blank=True)
    street = models.CharField(max_length=200)
    postal_code = models.IntegerField()
    city = models.CharField(max_length=200)
    country = models.ForeignKey(Country)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.as_str()

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


class GPSAddress(models.Model):
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return '%s, %s' % (self.longitude, self.latitude)


class Location(models.Model):
    label = models.CharField(max_length=200)
    postal_address = models.ForeignKey(PostalAddress, null=True, blank=True)
    gps_address = models.ForeignKey(GPSAddress, null=True, blank=True)
    picture = models.FileField('Picture', upload_to='pictures/locations', blank=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.label


class RoadbookAddress(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='roadbook_address')
    from_description = models.CharField(max_length=200)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.from_description


class RoadbookStep(models.Model):
    rank = models.PositiveIntegerField()
    at_description = models.CharField(max_length=200)
    direction_to_follow = models.CharField(max_length=200)
    roadbook = models.ForeignKey(RoadbookAddress, on_delete=models.CASCADE)
    picture = models.FileField('Picture', upload_to='pictures/roadbooks_steps', blank=True)

    def __str__(self):
        return self.at_description


from HTMLParser import HTMLParser

"""
Implements :
DDD.DDDDD^'    : Decimal Degrees signed                 +32.30642, -122.61458
DDD.DDDDD^'    : Decimal Degrees signed GMap            32.30642,-122.61458

Should implement :
DDD^ MM' SS.S" : Degrees, Minutes and Seconds           32^ 18' 23.1" N 122^ 36' 52.5" W
DDD^ MM.MMM'   : Degrees and Decimal Minutes            32^ 18.385' N 122^ 36.875' W
DDD.DDDDD^'    : Decimal Degrees                        32.30642^ N 122.61458^ W
"""


def _FORMAT_GPS_AS_UNIMPLEMENTED_YET(lat=None, lon=None):
    h = HTMLParser()
    _degreeChar = h.unescape('&deg;')
    _res = 'DDD%s MM\' SS.S" (TODO2)' % _degreeChar
    return 'Not implemented yet : %s' % _res


def _FORMAT_GPS_AS_DECIMAL_DEGREES_SIGNED(lat=None, lon=None):
    _res = ''
    if lat:
        _res += '%s%s' % ('+' if lat > 0 else '-', lat)

    if (lat is not None) and (lon is not None):
        _res += ', '

    if lon:
        _res += '%s%s' % ('+' if lon > 0 else '-', lon)

    return _res


def _FORMAT_GPS_AS_DECIMAL_DEGREES_SIGNED_GMAP(lat=None, lon=None):
    _res = ''
    if lat:
        _res += lat

    if (lat is not None) and (lon is not None):
        _res += ','

    if lon:
        _res += lon

    return _res


_GPS_FORMATERS = {
    'DEGREES_MINUTES_AND_SECONDS': _FORMAT_GPS_AS_UNIMPLEMENTED_YET,
    'DEGREES_AND_DECIMAL_MINUTES': _FORMAT_GPS_AS_UNIMPLEMENTED_YET,
    'DECIMAL_DEGREES':             _FORMAT_GPS_AS_UNIMPLEMENTED_YET,
    'DECIMAL_DEGREES_SIGNED':      _FORMAT_GPS_AS_DECIMAL_DEGREES_SIGNED,
    'DECIMAL_DEGREES_SIGNED_GMAP': _FORMAT_GPS_AS_DECIMAL_DEGREES_SIGNED_GMAP,
}


class _GPSUtils(object):
    
    def format(self, lat=None, lon=None, format=None):
        """
            Formats GPS coordinates

        :param lat <float>: latitude
        :param lon <float>: longitude
        :param format <a key of _GPS_FORMATERS>: key of format to apply
        :return: <str>
        """
        if format is None:
            _format = self.default_format()
        else:
            _format = format

        if (lat is None) and (lon is None):
            raise Exception('lat and/or lon is required')

        return _GPS_FORMATERS[_format](lat=lat, lon=lon)

    @staticmethod
    def default_format():
        return 'DECIMAL_DEGREES_SIGNED'

    """ Documentation mechanics """

    @staticmethod
    def formaters_keys():
        return list([_key for _key in _GPS_FORMATERS])


gps_utils = _GPSUtils()


from abc import abstractmethod
import logging

from django.utils.html import format_html


class InterfaceModelRepresentation(object):
    """
        Exposes (NOT formatting BUT) rendering methods to integrated Models
    """

    def __init__(self, instance):
        self._instance = instance

    """ PUBLIC """

    def as_link(self):
        _link = self._buildAdminPageEditLink(self._instance)
        return format_html(_link)

    def as_list(self, instances):

        if not instances.count() > 0:
            return '-'

        _urlsHtml = ''.join(
            [
                '<li>%s</li>' % self._buildAdminPageEditLink(_instance)
                for _instance in instances
            ])
        return format_html('<ul>%s</ul>' % _urlsHtml)

    """ PRIVATE """

    @staticmethod
    def _buildAdminPageEditLink(instance):
        _url = '/admin/{module}/{model}/{id}/change/'.format(
            module=instance.__module__.split('.')[0],
            model=instance.__class__.__name__.lower(),
            id=instance.id,
        )
        return '<a href="%s" target="_blank">%s</a>' % (_url, instance.__str__())


class InterfaceModelLogger(object):
    def __init__(self, logged_object, prefix=''):
        self._logger = logging.getLogger('kino')
        self._obj = logged_object
        self._objectPrefix = '%s%s' % (self._obj.__module__, self._obj.__class__.__name__)
        self._methodPrefix = prefix

    """ PUBLIC """

    def prepare(self, prefix):
        """ MUST be called as first line of every object method """
        self._methodPrefix = prefix

    def debug(self, *args, **kwargs):
        _msg = self._prepareLine(*args, **kwargs)
        self._logger.debug(_msg)

    def info(self, *args, **kwargs):
        _msg = self._prepareLine(*args, **kwargs)
        self._logger.info(_msg)

    def warning(self, *args, **kwargs):
        _msg = self._prepareLine(*args, **kwargs)
        self._logger.warning(_msg)

    def error(self, *args, **kwargs):
        _msg = self._prepareLine(*args, **kwargs)
        self._logger.error(_msg)

    def exception(self, *args, **kwargs):
        _msg = self._prepareLine(*args, **kwargs)
        self._logger.exception(_msg)

    """ PRIVATE """

    def _prepareLine(self, *args, **kwargs):
        # prepare prefix message
        _res = '%s.%s' % (self._objectPrefix, self._methodPrefix)

        # add args to message
        for arg in args:
            if _res != '':
                _res += ' '
            _res += str(arg)

        # add kwargs to message
        for kwarg, value in kwargs.iteritems():
            if _res != '':
                _res += ' '

            _res += '%s : %s' % (kwarg, str(value))

        return _res


class GenericModelInterface(object):
    """
        Gives integrated tools to child Model classes
    """

    def __init__(self):
        self._representation = None
        self.l = InterfaceModelLogger(logged_object=self)

    @abstractmethod
    def __str__(self):
        """
        Overrides __str__ to impact Django integrated behaviors
        :return:<str> A better representation of the model
        """
        return str()

    """ PUBLIC """

    @property
    def representation(self):
        """
        Returns the representation integrated to the Model

        :return: <ModelRepresentation>
        """
        return self._get_or_instantiate_representation()

    """ PRIVATE """

    def _get_or_instantiate_representation(self):
        if self._representation is None:
            self._representation = InterfaceModelRepresentation(self)
        return self._representation

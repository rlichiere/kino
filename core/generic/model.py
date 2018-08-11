
from abc import abstractmethod

from django.utils.html import format_html


class ModelRepresentation(object):
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


class GenericModelInterface(object):
    """
        Gives integrated tools to child Model classes
    """

    def __init__(self):
        self._representation = None

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
            self._representation = ModelRepresentation(self)
        return self._representation

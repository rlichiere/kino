
from abc import abstractmethod

from django.utils.html import format_html


class ModelFormatter(object):

    def __init__(self, instance):
        self._instance = instance

    def __str__(self):
        return self._instance.__str__()

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

    def _buildAdminPageEditLink(self, instance):
        _url = '/admin/{module}/{model}/{id}/change/'.format(
            module=instance.__module__.split('.')[0],
            model=instance.__class__.__name__.lower(),
            id=instance.id,
        )
        return '<a href="%s" target="_blank">%s</a>' % (_url, instance.__str__())
        # return '<a href="%s" target="_blank">%s</a>' % (_url, instance.__repr_in_list__)


class GenericModelInterface(object):
    """
        Generic class must be implemented by all Models classes to take profit of integrated tools:
    """

    # RLI : dirty anticipation of cousin Model.id property
    id = int()

    def render_for_backoffice(self):
        return ModelFormatter(self)

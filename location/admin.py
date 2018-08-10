
from django.contrib import admin
from django.utils.html import format_html

from .models import Country, Location, PostalAddress, GPSAddress, RoadbookAddress, RoadbookStep


class PostalAddressAdmin(admin.ModelAdmin):
    list_display = ('number_in_street', 'street', 'postal_code', 'city', 'is_public', )


class GPSAddressAdmin(admin.ModelAdmin):
    list_display = ('longitude', 'latitude', 'location', 'is_public', )

    def location(self, instance):
        return Location.objects.get(gps_address=instance).label


class LocationAdmin(admin.ModelAdmin):
    list_display = ('label', 'postal_address_', 'gps_address', 'roadbooks', 'is_public', )

    def roadbooks(self, instance):
        _roadbooks = RoadbookAddress.objects.filter(location=instance)

        if _roadbooks.count() == 0:
            _resHtml = '<span title="No roadbook defined.">-</span>'
        else:
            _resHtml = '<br />'.join(
                [
                    '<a href="/admin/location/roadbookaddress/%s/change/" title="%s steps">%s</a>'
                    % (_r.id,
                        RoadbookStep.objects.filter(roadbook=_r).count(),
                        _r.from_description)
                    for _r in _roadbooks
                ])
        return format_html(_resHtml)

    def postal_address_(self, instance):
        _url = '/admin/location/postaladdress/%s/change/' % instance.postal_address.id
        _alt = instance.postal_address.as_str(expanded=True)
        _urlsHtml = '<a href="%s" title="%s">%s</a>' % (_url, _alt, instance.postal_address)
        return format_html(_urlsHtml)


class RoadbookAddressAdmin(admin.ModelAdmin):
    list_display = ('from_description', 'location', 'steps', 'is_public', )

    def steps(self, instance):
        _steps = RoadbookStep.objects.filter(roadbook=instance).order_by('rank')
        _urlsHtml = ''.join(
            [
                '<li><a href="/admin/location/roadbookstep/%s/change/">%02d. %s : %s</a></li>'
                    % (_s.id, _s.rank, _s.at_description, _s.direction_to_follow)
                for _s in _steps
            ])
        return format_html('<ul>%s</ul>' % _urlsHtml)


class RoadbookStepAdmin(admin.ModelAdmin):
    list_display = ('roadbook_to', 'coming_from', 'rank', 'at_description', 'direction_to_follow', )

    def roadbook_to(self, instance):
        return instance.roadbook.location.label

    def coming_from(self, instance):
        return instance.roadbook.from_description


admin.site.register(Country)
admin.site.register(PostalAddress, PostalAddressAdmin)
admin.site.register(GPSAddress, GPSAddressAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(RoadbookAddress, RoadbookAddressAdmin)
admin.site.register(RoadbookStep, RoadbookStepAdmin)

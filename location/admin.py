
from django.contrib import admin

from .models import Country, Location, PostalAddress, GPSAddress, RoadbookAddress, RoadbookStep


class PostalAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_in_street', 'street', 'postal_code', 'city', 'is_public', )


class GPSAddressAdmin(admin.ModelAdmin):
    list_display = ('latitude_longitude', 'location_', 'is_public', )

    def latitude_longitude(self, instance):
        return instance.coordinates

    def location_(self, instance):
        return Location.objects.get(gps_address=instance).render_for_backoffice().as_link()


class LocationAdmin(admin.ModelAdmin):
    list_display = ('label', 'postal_address_', 'gps_address_', 'roadbooks', 'is_public', )

    def roadbooks(self, instance):
        _roadbooks = RoadbookAddress.objects.filter(location=instance)
        if _roadbooks.count() == 0:
            return '-'
        return instance.render_for_backoffice().as_list(_roadbooks)

    def postal_address_(self, instance):
        return instance.postal_address.render_for_backoffice().as_link()

    def gps_address_(self, instance):
        return instance.gps_address.render_for_backoffice().as_link()


class RoadbookAddressAdmin(admin.ModelAdmin):
    list_display = ('arriving_by', 'location', 'steps', 'is_public', )

    def steps(self, instance):
        _steps = RoadbookStep.objects.filter(roadbook=instance).order_by('rank')
        return instance.render_for_backoffice().as_list(_steps)


class RoadbookStepAdmin(admin.ModelAdmin):
    list_display = ('id', 'at_description', 'direction_to_follow', 'rank', 'roadbook_to', 'arriving_by', )

    def roadbook_to(self, instance):
        return instance.roadbook.location.label

    def arriving_by(self, instance):
        return instance.roadbook.arriving_by


admin.site.register(Country)
admin.site.register(PostalAddress, PostalAddressAdmin)
admin.site.register(GPSAddress, GPSAddressAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(RoadbookAddress, RoadbookAddressAdmin)
admin.site.register(RoadbookStep, RoadbookStepAdmin)

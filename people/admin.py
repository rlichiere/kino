
from django.contrib import admin

from .models import Capacity, Participant


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacities_', 'location', 'preferred_method_of_contact')

    def capacities_(self, instance):
        return instance.representation.as_list(instance.capacities.all())


admin.site.register(Capacity)
admin.site.register(Participant, ParticipantAdmin)

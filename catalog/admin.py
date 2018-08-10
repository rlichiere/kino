
from django.contrib import admin

from .models import ItemCategory, Item, ItemPicture


class ItemAdmin(admin.ModelAdmin):
    list_display = ('label', 'list_categories', 'owner_', )

    def list_categories(self, instance):
        _instances = instance.categories.all()
        return instance.representation.as_list(_instances)

    def owner_(self, instance):
        return instance.owner.representation.as_link()


class ItemPictureAdmin(admin.ModelAdmin):
    list_display = ('label', 'item', 'list_categories', )

    def list_categories(self, instance):
        _instances = instance.item.categories.all()
        return instance.representation.as_list(_instances)


admin.site.register(ItemCategory)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemPicture, ItemPictureAdmin)

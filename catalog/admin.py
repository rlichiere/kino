
from django.contrib import admin
from django.utils.html import format_html

from .models import ItemCategory, Item, ItemPicture


class ItemAdmin(admin.ModelAdmin):
    list_display = ('label', 'list_categories', 'owner_', )

    def list_categories(self, instance):
        return ','.join([_.label for _ in instance.categories.all()])

    def owner_(self, instance):
        return format_html('<a href="/admin/catalog/contact/%s/change/" target="_blank">%s</a>' % (instance.owner.id, instance.owner.pseudo))


class ItemPictureAdmin(admin.ModelAdmin):
    list_display = ('label', 'item', 'list_categories', )

    def list_categories(self, instance):
        return ','.join([_.label for _ in instance.item.categories.all()])


admin.site.register(ItemCategory)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemPicture, ItemPictureAdmin)

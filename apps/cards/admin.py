from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from .models import Card, Tag


@admin.action(description='Mark selected cards as visible')
def make_visible(modeladmin, request, queryset):
    queryset.update(visible=True)


@admin.action(description='Mark selected cards as invisible')
def make_invisible(modeladmin, request, queryset):
    queryset.update(visible=False)


class CardAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'visible')
    actions = [make_visible, make_invisible]
    fieldsets = [
        (
            None,
            {
                "fields": ['title', 'description', 'url', 'username', 'password', 'visible', 'tags'],
            },
        ),
        (
            'Choose only one image option:',
            {
                "fields": ['image', 'image_url'],
            },
        ),
    ]


admin.site.register(Card, CardAdmin)
admin.site.register(Tag)

from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import SliderImage


@admin.register(SliderImage)
class SliderImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image_preview')

    def image_preview(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html('<img src="{}" style="width: 45px; height:45px;" />', obj.image.url)
        return ""
    image_preview.short_description = 'Preview'

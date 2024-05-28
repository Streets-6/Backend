from django.contrib import admin

from .models import CoordinatesEvent, Event, PhotoEvent


class CoordinatesAdmin(admin.ModelAdmin):
    list_display = ("pk", "event", "x", "y")
    empty_value_display = "-пусто-"


class PhotoAdmin(admin.ModelAdmin):
    list_display = ("pk", "event", "url")
    empty_value_display = "-пусто-"


class EventAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "city", "start_date", "end_date")
    search_fields = ("title",)
    list_filter = (
        "start_date",
        "end_date",
    )
    empty_value_display = "-пусто-"


admin.site.register(CoordinatesEvent, CoordinatesAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(PhotoEvent, PhotoAdmin)

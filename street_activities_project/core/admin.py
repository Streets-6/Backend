from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Discipline

# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)


class DisciplineAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
    empty_value_display = "-пусто-"


admin.site.register(Discipline, DisciplineAdmin)

from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.db import ProgrammingError

from .models import *


# TODO: Закомментировать при первой миграции
@admin.register(ProjectConfig)
class ProjectConfigAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        try:
            ProjectConfig.load().save()
        except ProgrammingError:
            pass

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class NewFlatPageInline(admin.StackedInline):
    model = NewFlatPage
    verbose_name = 'Содержание'


class FlatPageNewAdmin(FlatPageAdmin):
    inlines = (NewFlatPageInline, )
    fieldsets = (
        (None, {'fields': ('url', 'title', 'sites')}),
        (('Advanced options', ), {
            'fields': ('template_name', ),
        })
    )
    list_display = ('url', 'title')
    list_filter = ('sites', 'registration_required')
    search_fields = ('url', 'title')


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageNewAdmin)
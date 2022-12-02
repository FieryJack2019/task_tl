from django.contrib import admin

from apps.employees.models import Division

from mptt.admin import DraggableMPTTAdmin


class DivisionAdminModel(DraggableMPTTAdmin):
    date_hierarchy = 'created_at'
    list_display = ['tree_actions', 'indented_title', 'name']


admin.site.register(Division, DivisionAdminModel)

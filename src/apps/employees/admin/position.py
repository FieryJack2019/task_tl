from django.contrib import admin

from apps.employees.models import Position


class PositionAdminModel(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ['name']


admin.site.register(Position, PositionAdminModel)

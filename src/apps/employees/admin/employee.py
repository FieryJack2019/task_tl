from django.contrib import admin

from apps.employees.models import Employee


class EmployeeAdminModel(admin.ModelAdmin):
    date_hierarchy = 'date_employment'
    list_display = ['id', 'full_name', 'position', 'date_employment', 'division']


admin.site.register(Employee, EmployeeAdminModel)

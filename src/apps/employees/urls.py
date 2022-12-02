from django.urls import path
from .views import DivisionListView, EmployeesDatatableView

urlpatterns = [
    path('', DivisionListView.as_view(), name='division_list'),
    path('employees-table/', EmployeesDatatableView.as_view(), name='employees_table')
]

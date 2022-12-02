from django.views.generic import ListView
from ajax_datatable.views import AjaxDatatableView
from .models import Division, Employee


class DivisionListView(ListView):
    model = Division
    template_name = 'employees/list_divisions.html'
    context_object_name = 'divisions'


class EmployeesDatatableView(AjaxDatatableView):
    model = Employee
    title = 'Сотрудники подразделения'

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'full_name', 'visible': True},
        {'name': 'position', 'foreign_field': 'position__name', 'visible': True},
        {'name': 'date_employment', 'visible': True},
        {'name': 'salary', 'visible': True},
        {'name': 'division', 'visible': False},
    ]

    def get_initial_queryset(self, request=None):
        if 'division_id' in request.REQUEST:
            division_id = int(request.REQUEST.get('division_id'))
            queryset = Employee.objects.filter(division_id=division_id)
            return queryset

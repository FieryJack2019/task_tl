import datetime

from django.test import TestCase
from apps.employees.models import Division, Employee, Position


class DivisionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Division.objects.create(name='Подразделение 1')

    def test_name_label(self):
        division = Division.objects.first()
        field_label = division._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название')

    def test_name_max_length(self):
        division = Division.objects.first()
        max_length = division._meta.get_field('name').max_length
        self.assertEquals(max_length, 30)


class EmployeeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        position = Position.objects.create(name='Должность')
        division = Division.objects.create(name='Подразделение')
        Employee.objects.create(full_name='Иванов Иван Иванович',
                                position=position,
                                date_employment=datetime.date.today(),
                                salary=130000.0,
                                division=division)

    def test_full_name_label(self):
        employee = Employee.objects.first()
        field_label = employee._meta.get_field('full_name').verbose_name
        self.assertEquals(field_label, 'ФИО')

    def test_full_name_max_length(self):
        employee = Employee.objects.first()
        max_length = employee._meta.get_field('full_name').max_length
        self.assertEquals(max_length, 50)

    def test_position_label(self):
        employee = Employee.objects.first()
        field_label = employee._meta.get_field('position').verbose_name
        self.assertEquals(field_label, 'Должность')

    def test_date_employment_label(self):
        employee = Employee.objects.first()
        field_label = employee._meta.get_field('date_employment').verbose_name
        self.assertEquals(field_label, 'Дата приема на работу')

    def test_salary_label(self):
        employee = Employee.objects.first()
        field_label = employee._meta.get_field('salary').verbose_name
        self.assertEquals(field_label, 'Размер заработной платы')

    def test_division_label(self):
        employee = Employee.objects.first()
        field_label = employee._meta.get_field('division').verbose_name
        self.assertEquals(field_label, 'Подразделение')


class PositionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Position.objects.create(name='Должность 1')

    def test_full_name_label(self):
        position = Position.objects.first()
        field_label = position._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название')

    def test_full_name_max_length(self):
        position = Position.objects.first()
        max_length = position._meta.get_field('name').max_length
        self.assertEquals(max_length, 30)

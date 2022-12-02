import uuid

from apps.utils.models import TimeBasedModel

from django.db import models


class Employee(TimeBasedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=50, verbose_name='ФИО')
    position = models.ForeignKey('Position', on_delete=models.SET_NULL, null=True, verbose_name='Должность')
    date_employment = models.DateField(verbose_name='Дата приема на работу')
    salary = models.FloatField(verbose_name='Размер заработной платы')
    division = models.ForeignKey('Division', on_delete=models.SET_NULL, null=True,
                                 related_name='employees', verbose_name='Подразделение')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

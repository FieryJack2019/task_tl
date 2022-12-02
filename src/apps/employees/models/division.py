from apps.utils.models import TimeBasedModel

from mptt.models import MPTTModel, TreeForeignKey

from django.db import models


class Division(MPTTModel, TimeBasedModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='children', verbose_name='Родительское подразделение')
    name = models.CharField(max_length=30, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

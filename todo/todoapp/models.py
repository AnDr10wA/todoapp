from django.db import models


class TodoModel(models.Model):
    name = models.CharField(max_length=255, verbose_name='')
    date_create = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False, verbose_name="статус")

    class Meta:
        ordering = ('-date_create',)
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.name

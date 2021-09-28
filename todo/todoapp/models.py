from django.db import models
from datetime import datetime, timedelta
from django.urls import reverse

class TodoModel(models.Model):
    choises_priority = (('high', 'high'),
                        ('medium', 'medium'),
                        ('low', 'low'))
    choises_status = (('completed', 'Completed'),
                      ('progress', 'In Progress'),
                      ('postponed', 'Postponed'),
                      )

    name = models.CharField(max_length=50, verbose_name='Задача')

    comment = models.TextField(verbose_name='Описание', blank = True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_deadline = models.DateTimeField(default=datetime.now()+timedelta(days=1))
    date_reminder = models.DateTimeField(default=datetime.now()+timedelta(days=1), blank=True)
    priority = models.CharField(max_length=50, choices=choises_priority)
    status = models.CharField(max_length=50, choices=choises_status)

    class Meta:
        ordering = ('-date_create',)
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.name


from django.db import models


class MyTasks(models.Model):

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    class PriorityChoices(models.TextChoices):
        LOW = 'LO', 'Low'
        NORMAL = 'NO', 'Normal'
        HIGH = 'HI', 'High'

    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    date = models.DateField()
    time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=150)
    done = models.BooleanField()
    priority = models.CharField(max_length=2, choices=PriorityChoices.choices, default=PriorityChoices.NORMAL)
    notification_due_date = models.DateTimeField(null=True, blank=True, verbose_name='User will be notified at')

    def __str__(self):
        return f'{self.name}'

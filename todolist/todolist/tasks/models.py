from django.db import models

class MyTasks(models.Model):
    class PriorityChoices(models.TextChoices):
        LOW = 'LO', 'Low'
        NORMAL = 'NO', 'Normal'
        HIGH = 'HI', 'High'

    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=150)
    done = models.BooleanField()
    priority = models.CharField(max_length=2, choices=PriorityChoices.CHOICES, default=PriorityChoices.NORMAL)


from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

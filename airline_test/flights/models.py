from django.db import models

# Create your models here.
class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.origin} - {self.destination}"

class Airport(models.Model):
    code = models.CharField(max_length=4)
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.code} ({self.city}, {self.country})"

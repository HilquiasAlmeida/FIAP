from django.db import models

class ChildDevice(models.Model):
    name = models.CharField(max_length=100)
    equipment = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=50, default="Online")
    battery = models.CharField(max_length=10, default="100%")
    latitude = models.CharField(max_length=50, default="-23.5505")
    longitude = models.CharField(max_length=50, default="-46.6333")
    location_name = models.CharField(max_length=200, default="Residência")

    def __str__(self):
        return f"{self.name} - {self.equipment}"

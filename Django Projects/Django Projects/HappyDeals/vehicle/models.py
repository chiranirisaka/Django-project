from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=50)
    max_persons = models.IntegerField()
    fuel_efficiency = models.FloatField()
    price_per_km = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    image_url = models.URLField(max_length=200)

    def __str__(self):
        return self.name
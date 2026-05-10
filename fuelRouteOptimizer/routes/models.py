from django.db import models


class FuelStation(models.Model):
    opis_truckstop_id = models.IntegerField()

    truckstop_name = models.CharField(max_length=255)

    address = models.TextField()

    city = models.CharField(max_length=255)

    state = models.CharField(max_length=50)

    rack_id = models.CharField(max_length=100)

    retail_price = models.FloatField()

    latitude = models.FloatField(null=True, blank=True)

    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.truckstop_name} - {self.city}"
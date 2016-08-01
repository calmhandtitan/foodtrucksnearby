from django.db import models


class Foodtruck(models.Model):
    """Foodtruck model stores basic info pulled from DataSF API"""

    objectid = models.IntegerField(primary_key=True)
    applicant = models.CharField(max_length=128, blank=True, null=True)
    facilitytype = models.CharField(
        max_length=64, default='Truck', blank=True, null=True)
    address = models.CharField(max_length=512, blank=True, null=True)
    fooditems = models.CharField(max_length=512, blank=True, null=True)
    latitude = models.DecimalField(
        db_index=True, max_digits=15, decimal_places=12, blank=True, null=True)
    longitude = models.DecimalField(
        db_index=True, max_digits=15, decimal_places=12, blank=True, null=True)

    def __str__(self):
        return self.applicant

    class Meta:
        ordering = ('objectid',)

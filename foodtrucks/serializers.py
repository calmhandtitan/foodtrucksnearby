from rest_framework import serializers
from .models import Foodtruck


class FoodtruckSerializer(serializers.ModelSerializer):
    distance = serializers.DecimalField(
        max_digits=15, decimal_places=12, required=False)

    class Meta:
        model = Foodtruck

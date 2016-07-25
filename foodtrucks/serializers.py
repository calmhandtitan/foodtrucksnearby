from rest_framework import serializers 
from .models import Foodtruck

class FoodtruckSerializer(serializers.ModelSerializer):
	distance = serializers.SerializerMethodField('get_distance')
	
	def get_distance(self, obj):
		return getattr(obj, 'distance', None)
	
	class Meta:
		model = Foodtruck

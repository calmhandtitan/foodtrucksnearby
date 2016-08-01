import geopy
import math
from decimal import *
from geopy.distance import distance
from geopy.geocoders import GoogleV3
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import QueryForm
from .models import Foodtruck
from .serializers import FoodtruckSerializer


def index(request):
    context = {}
    if request.method == 'GET':
        context['form'] = QueryForm()
        return render(request, 'foodtrucks/index.html', context)
    elif request.method == 'POST':
        form = QueryForm(request.POST)
        context['form'] = form

        if not form.is_valid():
            print 'form not valid'
            return render(request, 'foodtrucks/index.html', context)

        lat = form.cleaned_data['latitude']
        lng = form.cleaned_data['longitude']
        rad = form.cleaned_data['radius']
        lim = form.cleaned_data['limit']

        foodtrucks = findFoodTrucksbyLocation(lat, lng, rad, lim)
        context['foodtrucks'] = foodtrucks

    return render(request, 'foodtrucks/index.html', context)


class FoodtruckViewSet(viewsets.ModelViewSet):
    """
        Foodtruck viewset provides basic list() and retrieve() access to Foodtruck model.
    """
    queryset = Foodtruck.objects.all()
    serializer_class = FoodtruckSerializer


@api_view(['GET'])
def foodtruckByLocation(request):
    """
            Retrieve list of foodtrucks within the radius of a given location
            Default Search Result Limit is 10
    """
    if 'latitude' not in request.GET or not request.GET['latitude']:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        latitude = request.GET['latitude']

    if 'longitude' not in request.GET or not request.GET['longitude']:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        longitude = request.GET['longitude']

    radius = Decimal(1)
    limit = 10
    if 'radius' in request.GET and request.GET['radius']:
        radius = Decimal(request.GET['radius'])
    if 'limit' in request.GET and request.GET['limit']:
        limit = request.GET['limit']

    foodtrucks = findFoodTrucksbyLocation(latitude, longitude, radius, limit)
    if request.method == 'GET':
        serializer = FoodtruckSerializer(foodtrucks, many=True)
        return Response(serializer.data)


def findFoodTrucksbyLocation(latitude, longitude, radius, limit):
    """
            Function to find the list of foodtrucks(max = "limit")
            within a circle of radius = "radius" from ("latitude", 
    """
    latitude = Decimal(latitude)
    longitude = Decimal(longitude)
    radius = Decimal(radius)
    limit = int(limit)

    # calculate a bounding box using radius to retrieve trucks within approx.
    # distance
    lat_offset = Decimal(geopy.units.degrees(
        arcminutes=geopy.units.nautical(miles=float(radius))))
    lon_offset = Decimal(geopy.units.degrees(arcminutes=geopy.units.nautical(
        miles=float(radius) / math.cos(int(latitude)))))

    north = latitude + lat_offset
    south = latitude - lat_offset
    east = longitude - lon_offset
    west = longitude + lon_offset

    # convert queryset to list so we can add a distance field
    foodtrucks = list(Foodtruck.objects.filter(latitude__range=(
        south, north)).filter(longitude__range=(east, west)))

    # remove trucks that are too far
    for truck in list(foodtrucks):
        dist = distance((truck.latitude, truck.longitude),
                        (float(latitude), float(longitude))).miles
        if dist > radius:
            foodtrucks.remove(truck)
        else:
            truck.distance = dist
    return foodtrucks[:limit]

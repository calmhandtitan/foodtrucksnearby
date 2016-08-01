import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foodtrucknearby.settings")
django.setup()

import requests
import datetime
import logging
from geopy.geocoders import GoogleV3
from foodtrucks.models import Foodtruck


def getValue(m, key):
    if key in m:
        return m[key]
    else:
        return None

api_url = 'https://data.sfgov.org/resource/6a9r-agq8.json'
geolocator = GoogleV3(api_key="AIzaSyCfBWyrDeF8AUgpS1yqo_HzkTw4UD2_34E")

r = requests.get(api_url)

if r.status_code != 200:
    logging.error("API call failed with status code: " + r.status_code)
else:
    ftrucks = list()
    for item in r.json():
        truck = Foodtruck()
        truck.objectid = getValue(item, 'objectid')
        truck.applicant = getValue(item, 'applicant')
        truck.facilitytype = getValue(item, 'facilitytype')
        truck.address = getValue(item, 'address')
        truck.fooditems = getValue(item, 'fooditems')
        try:
            truck.latitude = getValue(item, 'latitude')
            truck.longitude = getValue(item, 'longitude')
        except KeyError:
            location = geolocator.geocode(truck.address + " San Francisco, CA")
            truck.latitude, truck.longitude = location.latitude, location.longitude
        ftrucks.append(truck)

    Foodtruck.objects.bulk_create(ftrucks)

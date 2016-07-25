from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'foodtrucks', views.FoodtruckViewSet)

urlpatterns = patterns('',
    url(r'^$', views.index, name = 'index'),
)

urlpatterns.append(url(r'^api/', include(router.urls)),)
urlpatterns.append(url(r'^api/nearby', views.foodtruckByLocation, name = 'foodtruckByLocation'),)




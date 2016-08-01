from django.conf.urls import include, url
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'foodtrucks', views.FoodtruckViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
]


urlpatterns.append(url(r'^api/', include(router.urls)),)
urlpatterns.append(
    url(r'^api/nearby', views.foodtruckByLocation, name='foodtruckByLocation'),)

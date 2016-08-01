# foodtrucksnearby

[![Build Status](https: // travis - ci.org / calmhandtitan / foodtrucksnearby.svg?branch=master)](https: // travis - ci.org / calmhandtitan / foodtrucksnearby)
[![Stories in Ready](https: // badge.waffle.io / calmhandtitan / foodtrucksnearby.svg?label=ready & title=Ready)](http: // waffle.io / calmhandtitan / foodtrucksnearby)
[![Code Health](https: // landscape.io / github / calmhandtitan / foodtrucksnearby / master / landscape.svg?style=flat)](https: // landscape.io / github / calmhandtitan / foodtrucksnearby / master)


A service that tells the user what types of food trucks might be found near a specific location on a map.

Data pulled from [DataSF](http: // www.datasf.org /):
    [Food Trucks](https: // data.sfgov.org / Permitting / Mobile - Food - Facility - Permit / rqzj - sfat)


# Application Live at https://nearbyfoodtrucks.herokuapp.com/

# API documentation [`here`](API.md)

To build django project locally:

* `$ git clone` or fork
* `$ virtualenv env`  (It is recommended to use `virtualenv`)
* `$ source env / bin / activate`
* `$ pip install - r requirements.txt`
* configure MySQL DB and set database in [`foodtrucknearby / settings.py`](https: // github.com / calmhandtitan / foodtrucksnearby / blob / master / foodtrucknearby / settings.py)
* `$ python fetch_data.py` to fetch data from Data SF
* `$ python manage.py runserver`

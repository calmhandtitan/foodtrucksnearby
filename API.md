# API documentation
All data is pulled from the [`Mobile Food Facility Permit dataset on DataSF`] (https://data.sfgov.org/Permitting/Mobile-Food-Facility-Permit/rqzj-sfat)


**API Root:** `/api/` 

## Foodtrucks

Basic API to retrieve foodtruck data.

**URL:** `foodtrucks/`  
**Allow:** `GET`, `POST`  
**Content-Type:** `application/json`
**Fields:**  
- `objectid` (integer): primary key of foodtruck
- `applicant` (string): name of foodtruck and/or foodtruck owner
- `facilitytype` (string): either "Truck", "Cart", or blank
- `address` (string): human-readable address of cart
- `fooditems` (string): menu items supplied by cart owner
- `latitude` (float): cart location latitude, in degrees
- `longitude` (float): cart location longitude, in degrees

### Examples:

**`GET /api/foodtrucks/`**   

**Response:**  
```
[
    {
        "objectid": 305727,
        "applicant": "Bombay Blvd.",
        "facilitytype": "Truck",
        "address": "561 MISSION ST",
        "fooditems": null,
        "latitude": "0.000000000000",
        "longitude": "0.000000000000"
    },
    {
        "objectid": 305735,
        "applicant": "Bombay Blvd.",
        "facilitytype": "Truck",
        "address": "86 03RD ST",
        "fooditems": null,
        "latitude": "37.786206082104",
        "longitude": "-122.402532491346"
    },
    {
        "objectid": 321365,
        "applicant": "Sausage Slinger",
        "facilitytype": "Push Cart",
        "address": "100 NEW MONTGOMERY ST",
        "fooditems": null,
        "latitude": "37.787041555872",
        "longitude": "-122.400427155584"
    },
  ... (truncated)
```
**`GET /api/foodtrucks/334914/`**  

**Response:**
```
{
    "objectid": 334914,
    "applicant": "Halal Cart",
    "facilitytype": "Push Cart",
    "address": "901 MARKET ST",
    "fooditems": null,
    "latitude": "37.783470066083",
    "longitude": "-122.408040736138"
}
```

## Nearby

Retrieve list of foodtrucks within a given `radius` of center (`lat` and `lon`).

**URL:** `nearby/`  
**Allow:** `GET`, `POST`  
**Content-Type:** `application/json`

**Query Arguments**: `latitude` (float), `longitude` (float), `radius` (float)[optional], `limit` (integer)[optional]

**Fields:**  
- `objectid` (integer): primary key of foodtruck
- `distance` (float): distance from `lat`,`lon`
- `applicant` (string): name of foodtruck and/or foodtruck owner
- `facilitytype` (string): either "Truck", "Cart", or blank
- `address` (string): human-readable address of cart
- `fooditems` (string): menu items supplied by cart owner
- `latitude` (float): cart location latitude, in degrees
- `longitude` (float): cart location longitude, in degrees

### Examples:

**`GET /api/nearby?latitude=37.7919&longitude=-122.4038`**  

**Response:**  
```
 [
    {
        "objectid": 305735,
        "distance": "0.398776235162",
        "applicant": "Bombay Blvd.",
        "facilitytype": "Truck",
        "address": "86 03RD ST",
        "fooditems": null,
        "latitude": "37.786206082104",
        "longitude": "-122.402532491346"
    },
    {
        "objectid": 321365,
        "distance": "0.382561854800",
        "applicant": "Sausage Slinger",
        "facilitytype": "Push Cart",
        "address": "100 NEW MONTGOMERY ST",
        "fooditems": null,
        "latitude": "37.787041555872",
        "longitude": "-122.400427155584"
    },
    {
        "objectid": 334914,
        "distance": "0.626012373824",
        "applicant": "Halal Cart",
        "facilitytype": "Push Cart",
        "address": "901 MARKET ST",
        "fooditems": null,
        "latitude": "37.783470066083",
        "longitude": "-122.408040736138"
    },
    {
        "objectid": 338539,
        "distance": "0.391381724217",
        "applicant": "Bacon Bacon",
        "facilitytype": "Truck",
        "address": "250 CLAY ST",
        "fooditems": null,
        "latitude": "37.795700905317",
        "longitude": "-122.398489753587"
    },
    {
        "objectid": 338548,
        "distance": "0.464190020347",
        "applicant": "Bacon Bacon",
        "facilitytype": "Truck",
        "address": "600 FRONT ST",
        "fooditems": null,
        "latitude": "37.797455156782",
        "longitude": "-122.399011222821"
    },
    {
        "objectid": 364218,
        "distance": "0.329277964747",
        "applicant": "The Chai Cart",
        "facilitytype": "Push Cart",
        "address": "79 NEW MONTGOMERY ST",
        "fooditems": null,
        "latitude": "37.787889699906",
        "longitude": "-122.400535326777"
    },
    {
        "objectid": 427471,
        "distance": "0.297095288997",
        "applicant": "French Creme Brulee",
        "facilitytype": "Push Cart",
        "address": "720 MARKET ST",
        "fooditems": null,
        "latitude": "37.787598415555",
        "longitude": "-122.404090439434"
    },
    {
        "objectid": 437214,
        "distance": "0.932440728263",
        "applicant": "Natan's Catering",
        "facilitytype": "Truck",
        "address": "950 HARRISON ST",
        "fooditems": null,
        "latitude": "37.778388615787",
        "longitude": "-122.403191783229"
    },
    {
        "objectid": 494439,
        "distance": "0.930838410720",
        "applicant": "Sinthya's Hot Dogs",
        "facilitytype": "Truck",
        "address": "301 06TH ST",
        "fooditems": null,
        "latitude": "37.778441899211",
        "longitude": "-122.405086420952"
    },
    {
        "objectid": 498134,
        "distance": "0.404408053696",
        "applicant": "The Sandwich Stand, LLC.",
        "facilitytype": "Truck",
        "address": "50 MAIN ST",
        "fooditems": null,
        "latitude": "37.792363514411",
        "longitude": "-122.396434007976"
    }
]
```

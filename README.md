violence
========

Maps of police murders in USA. Data is based on the investigation from this [article](http://gawker.com/what-ive-learned-from-two-years-collecting-data-on-poli-1625472836) 


## Run

    python run.py # access on http://127.0.0.1:5000/ 


## JSON api

You can access all data through the (basic) API:

```GET /api/murders```
return an array of objects containing all murders with only a few fields _id, title and geo

    [
        {
            CleanDateOfDeath: ""2013-02-18T00:00:00+00:00"",
            FullName: "Taft Sellars",
            _id: : "54cd10d4eea7216d79d0948f",
            geo: {
                geometry: {},
                type: "Feature",
                properties: {
                    status: "OK",
                    city: "Alexandria",
                    confidence: 7,
                    ok: true,
                    country: "United States",
                    address: "3400 Duke St, Alexandria, VA 22304",
                    housenumber: 3400,
                    state: "VA",
                    street: "3400 Duke St",
                    location: "3400 block of Duke St. Alexandria Alexandria City VA 22304 , USA",
                    provider: "bing",
                    lat: 38.808353,
                    lng: -77.089843,
                    postal: "22304",
                    quality: "Address",
                    accuracy: "Interpolation"
                },
                bbox: [
                    -77.09645196157521,
                    38.80449028242932,
                    -77.08323403842479,
                    38.81221571757067
                ]
            }
        },
        ....
        ]

* ```GET /api/murders/:id```
return an object containing a single murder



## Setup

You need Python, Virtualenv, Pip, Bower & Mongo to run this

    virtualenv venv
    . venv/bin/activate
    pip install -r requirements.txt

Install [Mapbox.js]( https://www.mapbox.com/mapbox.js/api/v2.1) and other frontend dependencies into ```static/lib```

    bower install

Upload the Mongo dump in the DB ```violence```, collections ```murders``` 

    mongoimport -d violence -c murders data/db.json 
    # 2015-01-31T17:15:39.281+0100 imported 3681 objects


## Deploy

We can easily deploy using [those scripts](https://github.com/clemsos/flask-fabric-deploy)

## How to Prepare the Data

You Should 1) download CSV file from the  [Google Spreadsheet](https://docs.google.com/spreadsheet/ccc?key=0Aul9Ys3cd80fdHVMd0luQW5NYkVZNkhORmI0ajFma2c&usp=sharing#gid=0 ) and place it into the ```data``` folder, 2) store it into MongoDB, 3) geocode all the addresses, 4) parse the time correctly

    cd data
    python csv2mongo.py # store the data into MongoDB
    python geocode.py # get coordinates from address 
    python parse_date.py # get coordinates from address 

### About the geocoder

* Data is geocoded using [Python Geocoder](https://github.com/DenisCarriere/geocoder/wiki/Confidence-Score)
* Geocoders may reach the limit while processing so you should 1) change the geocoder in ```data/geocode.py``` or 2) wait an hour and retry.
* Coordinates are stored as [geojson](https://github.com/DenisCarriere/geocoder/wiki/GeoJSON-Support)
* A [confidence score](https://github.com/DenisCarriere/geocoder/wiki/Confidence-Score) will help you determinate the correctness of the geocoding for each record

### Export the data

    mongoexport --db violence --collection murders --out db.json
    # exported 3681 records


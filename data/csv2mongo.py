import os
import csv
import json
import re
import pymongo
# from geopy.geocoders import Nominatim

def csv2mongo(csv_file, collection):
    with open(csv_file,"r") as i:
        csv_data=csv.DictReader(i)

        for row in csv_data:
            clean_row={}
            for  rec in row :
                clean_name = "".join([c for c in rec.title() if re.match(r'\w', c)])
                clean_row[clean_name] = row[rec]

            try :
                collection.insert(clean_row)
            except Exception as exc:
                print("Failed to insert record {0} - {1}".format(clean_name, exc))

def geocode(record):
        try :
            geo = Geocoder.geocode(clean_row["City"])
        except :
            try :
                geo = Geocoder.geocode(clean_row["ZipCode"])
            except :
                geo = Geocoder.geocode(clean_row["State"])
        # print geo[0]
        return geo.raw

if __name__ == '__main__':

    db = pymongo.Connection("localhost").violence
    raw_data_path = "murders.csv"

    csv2mongo(raw_data_path, db.murders)

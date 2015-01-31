#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import geocoder


def geocode(geo_info):
        """ Get GeoJSON coordinates from an address 

         List of availables geocoders :
         
         * geocoder.geolytica 
         * geocoder.mapquest
         * geocoder.arcgis 
         * geocoder.geonames 
         * geocoder.nokia
         * geocoder.bing 
         * geocoder.google 
         * geocoder.yahoo
         * geocoder.tomtom

        Just change the geocoder below when you hit the limit
        """

        geo = geocoder.bing(geo_info)
        return geo.geojson

if __name__ == '__main__':
    db = pymongo.Connection("localhost").violence
    murders  = [ x for x in db.murders.find() ]
    print "%s murders in the db"%len(murders)
    
    # geocode
    for i,murder in enumerate(murders): 
        try : 
            murder["geo"] # check if geo info exists
        except KeyError : 
            # parse geo information correctly 
            geo_info =""
            for g in murder["StreetAddress"], murder["City"], murder["County"], murder["State"], murder["ZipCode"] : 
                if g != "":geo_info +=  g +" "

            # geocode or ignore
            if geo_info != "" : 
                print i, "geocoding ", geo_info
                geocoded_info = geocode(geo_info + ", USA") # add country
                murder["geo"] = geocoded_info
                db.murders.save(murder)
            else :
                print i, "not geocoding - no info"
                pass 

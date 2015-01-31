#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo
import datetime

if __name__ == '__main__':
    db = pymongo.Connection("localhost").violence
    murders  = [ x for x in db.murders.find() ]
    print "%s murders in the db"%len(murders)
    
    # geocode
    for i,murder in enumerate(murders): 
        
        # February 18, 2013
        try:
            d = datetime.datetime.strptime( murder["DateOfDeath"], "%B %d, %Y" )
            print d.weekday()
        except ValueError:
            d = None

        murder["CleanDateOfDeath"] = d
        db.murders.save(murder)


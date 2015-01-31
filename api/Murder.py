#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from flask.ext import restful
from api import app, api, mongo
from bson.objectid import ObjectId
from datetime import datetime 
from bson import json_util

def json_serial(obj):
    """JSON serializer for murders - not serializable by default json code"""

    if isinstance(obj, datetime):
        serial = obj.isoformat()
        return serial

    if isinstance(obj, ObjectId):
        return str(obj)

class Murder(restful.Resource):
    """ Add or delete a single record """

    def get(self, murder_id):
        murder = mongo.db.murders.find_one_or_404({"_id": murder_id})
        return  json.loads(json.dumps(murder, default=json_serial))

    def delete(self, murder_id):
        mongo.db.murders.find_one_or_404({"_id": murder_id})
        mongo.db.murders.remove({"_id": murder_id})
        return '', 204

class MurderList(restful.Resource):
    """ List multiple records """
    
    def get(self):
        records = [x for x in mongo.db.murders.find()]
        murders =[]

        for record in records :
            
            murder = {}
            
            # id
            murder["_id"] = record["_id"]
            
            # geo
            try :
                murder["geo"] = record["geo"]
            except KeyError:
                murder["geo"] = {}

            # date
            murder["CleanDateOfDeath"] = record["CleanDateOfDeath"]
           
           # name of the guy
            murder["FullName"] = record["FullName"]
            murders.append(murder)

        return  json.loads(json.dumps(murders, default=json_serial))

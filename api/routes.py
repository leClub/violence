#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json
import random
from flask import render_template, jsonify, send_from_directory, request, make_response
from api import app, api, mongo
from api.Murder import Murder, MurderList

# HOME
@app.route('/')
def home():
    murders =  [x for x in mongo.db.murders.find()]
    return render_template('index.html', murders=murders)

# STATIC
@app.route('/js/<path:path>')
def js_static_proxy(path):
    """ send_static_file will guess the correct MIME type"""
    return app.send_static_file(os.path.join('js', path))

@app.route('/css/<path:path>')
def css_static_proxy(path):
    """ send_static_file will guess the correct MIME type"""
    print os.path.join('css', path)
    return app.send_static_file(os.path.join('css', path))

@app.route('/lib/<path:path>')
def lib_static_proxy(path):
    """ send_static_file will guess the correct MIME type"""
    return app.send_static_file(os.path.join('lib', path))

@app.route('/img/<path:path>')
def img_static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(os.path.join('img', path))


# API
api.add_resource(MurderList, '/api/murders')
api.add_resource(Murder, '/api/murders/<ObjectId:murder_id>')

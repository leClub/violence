import os 
from flask import Flask, make_response
from flask.ext import restful
from flask.ext.pymongo import PyMongo
from flask.ext.assets import Environment, Bundle
from bson.json_util import dumps
import jinja2

# basic paths
MONGO_URL = "mongodb://localhost:27017/violence"
ASSETS_DIR=os.path.join(os.path.dirname(os.path.abspath(__file__)), '../static')

# app
app = Flask(__name__)
app._static_folder = ASSETS_DIR
app.config['SECRET_KEY'] = 'secret!'
app.debug = True
app.jinja_loader=jinja2.FileSystemLoader('templates')

# compass config
assets = Environment(app)

main_scss = Bundle('assets/scss/style.scss', 'assets/scss/media.scss', filters='compass', output='css/style.css')
assets.register('main_scss', main_scss)

dashboard_css = Bundle('assets/scss/dashboard.scss', filters='compass', output='css/dashboard.css')
assets.register('dashboard_css', dashboard_css)

# bootstrap_css = Bundle('assets/dashboard/bootstrap-cyborg.min.css', output='css/bootstrap.css')
# assets.register('bootstrap_css', bootstrap_css)

print_css = Bundle('assets/scss/print.scss', filters='compass', output='css/print.css')
assets.register('print_css', print_css)

terminal_css = Bundle('assets/scss/partials/terminal.scss', filters='compass', output='css/terminal.css')
assets.register('terminal_css', terminal_css)

# mongo db
app.config['MONGO_URI'] = MONGO_URL
mongo = PyMongo(app)

def output_json(obj, code, headers=None):
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
api = restful.Api(app)
api.representations = DEFAULT_REPRESENTATIONS

import api.routes

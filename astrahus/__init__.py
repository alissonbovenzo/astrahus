from flask import Flask, url_for
from flask_pymongo import PyMongo
import json
from bson import ObjectId


application = Flask(__name__)


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)



def config(application: Flask):
    application.config.from_mapping(
        SECRET_KEY='Astrahus',
        MONGO_URI='mongodb://develop:develop1@ds247170.mlab.com:47170/astrahus'
    )
    application.json_encoder = JSONEncoder


config(application)
mongo = PyMongo(application)
from users.api import users_api

application.register_blueprint(users_api)


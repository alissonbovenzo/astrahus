from flask import Blueprint, jsonify
from astrahus import mongo

users_api = Blueprint('users', __name__, url_prefix='/users')

@users_api.route('/')
def listAllUsers():
    online_users = list(mongo.db.users.find({'online':True}))
    print(online_users)
    for _ in online_users:
        print(_)
    return jsonify(online_users), 200

@users_api.route('/create')
def create():
    new_user = mongo.db.users.insert({'online': True, 'nome':'Alisson'})

    return jsonify(new_user)
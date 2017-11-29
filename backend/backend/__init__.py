from flask import Flask, make_response, jsonify, g
from flask_restful import Api
from .db import DBServer
from .config import config

app = Flask(__name__, static_url_path='/pethub/static')
db = DBServer()
session = db.session
apiobj = Api(app)

cfg = config['development']
app.config.from_object(cfg)
cfg.init_app(app)

def register_api():
    from .api import AdoptApi,AdoptsApi,UserApi,UsersApi
    apiobj.add_resource(AdoptApi, '/pethub/api/adopt/<int:id>', endpoint = 'adopt')
    apiobj.add_resource(AdoptsApi, '/pethub/api/adopts', endpoint = 'adopts')
    apiobj.add_resource(UserApi, '/pethub/api/user/<int:id>', endpoint = 'user')
    apiobj.add_resource(UsersApi, '/pethub/api/users', endpoint = 'users')

register_api()









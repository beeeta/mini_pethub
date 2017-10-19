from . import app
from .middlewire import auth
from .modeles import Pet

from flask_restful import Api,Resource

from .db import session

api = Api(app)

class AdoptApi(Resource):
    # decorators = [auth.login_required]
    def get(self, id):
        print('get method:{}'.format(id))
        return {'msg':'hahahaha'}

    def put(self, id):
        print('put method:{}'.format(id))

    def delete(self, id):
        print('delete method:{}'.format(id))

class AdoptsApi(Resource):

    def get(self):
        Pet.query_all
        return {"msg":"success"}




@app.teardown_request
def shutdown_session(exception=None):
    session.remove()

api.add_resource(AdoptApi, '/pethub/api/v0.1/adopts/<int:id>', endpoint = 'adopt')
api.add_resource(AdoptsApi, '/pethub/api/v0.1/adopts', endpoint = 'adopts')

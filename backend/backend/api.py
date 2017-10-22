from flask import request
from . import app

from .middlewire import auth
from .modeles import Pet

from flask_restful import Api,Resource

from .db import session

api = Api(app)

class AdoptApi(Resource):
    # decorators = [auth.login_required]
    def get(self, id):
        pet = session.query(Pet).filter(Pet.id==id).one()
        return write_resp("success",pet.to_json_dict())

    def put(self, id):

        data_dic = {}
        for i in request.form:
            if hasattr(Pet,i):
                data_dic[i] = request.form[i]
        session.query(Pet).filter(Pet.id==id).update(data_dic)
        return write_resp("success",id)


    def delete(self, id):
        print('delete method:{}'.format(id))

class AdoptsApi(Resource):

    def get(self):
        pets = session.query(Pet).all()
        return write_resp("success",[pet.to_json_dict() for pet in pets])

    def post(self):
        pet = Pet()
        for i in request.form:
            if hasattr(pet,i):
                setattr(pet,i,request.form[i])
        session.add(pet)
        session.commit()
        return write_resp("success",pet.id)

def write_resp(errMsg,data):
    return {"errMsg":errMsg,"data":data}

@app.teardown_request
def shutdown_session(exception=None):
    session.remove()

api.add_resource(AdoptApi, '/pethub/api/v0.1/adopts/<int:id>', endpoint = 'adopt')
api.add_resource(AdoptsApi, '/pethub/api/v0.1/adopts', endpoint = 'adopts')

from flask import request,g,make_response,jsonify

from . import session,api,app
# from .authority import auth
from .models import Pet,User
# from .db import DBServer

from flask_restful import Resource

class AdoptApi(Resource):
    # decorators = [auth.login_required]
    def get(self, id):
        pet = session.query(Pet).filter(Pet.id==id).first()
        return write_resp("success",pet.to_json_dict())

    def put(self, id):

        data_dic = {}
        for i in request.form:
            if hasattr(Pet,i):
                data_dic[i] = request.form[i]
        session.query(Pet).filter(Pet.id==id).update(data_dic)
        return write_resp("success",id)

    def delete(self, id):
        session.query(Pet).filter(Pet.id == id).delete()

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


class UserApi(Resource):
    # decorators = [auth.login_required]
    def get(self, id):
        user = session.query(User).filter(User.id==id).first()
        return write_resp("success",user.to_json_dict())

    def put(self, id):
        data_dic = {}
        for i in request.form:
            if hasattr(User,i):
                data_dic[i] = request.form[i]
        session.query(User).filter(User.id==id).update(data_dic)
        return write_resp("success",id)

    def delete(self, id):
        print('delete method:{}'.format(id))


class UsersApi(Resource):
    # decorators = [auth.login_required]

    # @auth.login_required
    def get(self):
        users = session.query(User).all()
        return write_resp("success",[user.to_json_dict() for user in users])

    def post(self):
        user = User()
        for i in request.form:
            if hasattr(user,i):
                setattr(user,i,request.form[i])
        session.add(user)
        session.commit()
        return write_resp("success",user.id)

def write_resp(errMsg,data):
    return {"errMsg":errMsg,"data":data}

# @app.route("/pethub/api/token", methods=['GET'])
# @auth.login_required
def get_token():
    token = g.user.generate_auth_token()
    return make_response(jsonify(write_resp('success', token.decode('ascii'))))


@app.teardown_request
def shutdown_session(exception=None):
    session.remove()





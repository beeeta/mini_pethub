from flask import request,g,make_response,jsonify
from . import app

from .authority import auth
from .modeles import Pet,User

from flask_restful import Api,Resource

from .db import session

api = Api(app)

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


class UserApi(Resource):
    decorators = [auth.login_required]
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

api.add_resource(AdoptApi, '/pethub/api/{}/adopts/<int:id>'.format(app.config['VERSION']), endpoint = 'adopt')
api.add_resource(AdoptsApi, '/pethub/api/{}/adopts'.format(app.config['VERSION']), endpoint = 'adopts')

api.add_resource(UserApi, '/pethub/api/{}/users/<int:id>'.format(app.config['VERSION']), endpoint = 'user')
api.add_resource(UsersApi, '/pethub/api/{}/users'.format(app.config['VERSION']), endpoint = 'users')

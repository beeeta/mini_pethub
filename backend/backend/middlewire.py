from . import app,make_response,jsonify
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.get_password
def getPasswd(username):
    if username == 'beta':
        return 'beta'
    else:
        return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
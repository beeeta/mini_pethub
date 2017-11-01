from . import app,make_response,jsonify,g

from flask_httpauth import HTTPBasicAuth
from .db import session
from .modeles import User


auth = HTTPBasicAuth()

@auth.verify_password
def verify_passwd(username,password):
    print('username:{},password:{}'.format(username,password))
    user = User.verify_token(username)
    # token验证失败
    if user is not None:
        g.user = user
        return True
    else:
        user = session.query(User).filter(User.name == username).first()
        if user is not None:
            if user.verify_password(password):
                g.user = user
                return True
    return False


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)





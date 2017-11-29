from flask import Flask, make_response, jsonify, g
from flask_restful import Api
from .bp import bp
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .config import configer

app = Flask(__name__, static_url_path='/static')
# config
cfg = configer['development']
app.config.from_object(cfg)
cfg.init_app(app)
# db
# db = DBServer()
# session = db.session
Base = declarative_base()

engine = create_engine(cfg.SQLALCHEMY_DATABASE_URI, echo=True)
session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))
Base.query = session.query_property()


app.register_blueprint(bp)

# register restful
apiobj = Api(app)
def register_api():
    from .api import AdoptApi,AdoptsApi,UserApi,UsersApi
    apiobj.add_resource(AdoptApi, '/pethub/api/adopt/<int:id>', endpoint = 'adopt')
    apiobj.add_resource(AdoptsApi, '/pethub/api/adopts', endpoint = 'adopts')
    apiobj.add_resource(UserApi, '/pethub/api/user/<int:id>', endpoint = 'user')
    apiobj.add_resource(UsersApi, '/pethub/api/users', endpoint = 'users')
register_api()











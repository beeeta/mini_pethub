from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime,timedelta
from .config import DevelopmentConfig

Base = declarative_base()
engine = None
session = None

def init_session(app):
    if not app:
        engine = create_engine(DevelopmentConfig.SQLALCHEMY_DATABASE_URI, echo=True)
    else:
        engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
    session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    Base.query = session.query_property()



def init_db():
    init_session(None)
    from .modeles import Pet,User,Relation
    Base.metadata.create_all(bind=engine)
    user = User(name='beta2',vx='bbqq2',qq='121212',email='soso@gmail.com',province='湖北',city='武汉')
    pet = Pet(imgurl='2.jpg',province='gd',city='sz',describe='aaaaa')
    relations = Relation(user=user,pet=pet)
    session.add(user)
    session.add(pet)
    session.add(relations)
    session.commit()


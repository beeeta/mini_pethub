from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime,timedelta
from .config import DevelopmentConfig

class DBServer():

    def __init__(self,config=None):
        self.base = declarative_base()
        if not config:
            self.engine = create_engine(DevelopmentConfig.SQLALCHEMY_DATABASE_URI, echo=True)
        else:
            self.engine = create_engine(config['SQLALCHEMY_DATABASE_URI'], echo=True)
        self.session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=self.engine))
        self.base.query = self.session.query_property()


    def init_db(self):
        from .models import Pet,User,Relation
        self.base.metadata.create_all(bind=self.engine)
        user = User(name='beta2',vx='bbqq2',qq='121212',email='soso@gmail.com',province='湖北',city='武汉')
        pet = Pet(imgurl='2.jpg',province='gd',city='sz',describe='aaaaa')
        relations = Relation(user=user,pet=pet)
        self.session.add(user)
        self.session.add(pet)
        self.session.add(relations)
        self.session.commit()


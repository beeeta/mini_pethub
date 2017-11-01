from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime,timedelta

engine = create_engine("mysql+pymysql://root:123456@localhost:3307/pethub?charset=utf8", echo=True)
session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = session.query_property()

def init_db():
    from .modeles import Pet,User
    Base.metadata.create_all(bind=engine)
    user = User(name='beta',vx='bbqq',qq='121212',email='soso@gmail.com',province='湖北',city='武汉')
    session.add(user)
    for i in range(5):
        pet = Pet(imgurl=str(i)+'.jpg',province='广东',city='深圳',describe='一个小狗',
                  createtime=datetime.now().strftime(Pet.timeformater),
                  valitime=(datetime.now()+timedelta(days=30)).strftime(Pet.timeformater),
                  user=user)
        session.add(pet)
    session.commit()


from datetime import datetime,timedelta

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .db import Base

class Pet(Base):

    __tablename__ = 'pets'
    id = Column(Integer, primary_key=True)
    imgurl = Column(String(200))
    province = Column(String(10))
    city = Column(String(10))
    connection = Column(String(64))
    describe = Column(String(128))
    createtime = Column(String(32))
    updatetime = Column(String(32))
    valitime = Column(String(32))
    user_id = Column(ForeignKey('users.id'), nullable=False)
    user = relationship("User", lazy='joined')

    out_pros = ('id','imgurl','province','city','describe','createtime','updatetime','valitime')

    timeformater = '%Y-%m-%d %H:%M:%S'

    def to_json_dict(self):
        json_dic = {}
        for i in self.out_pros:
            json_dic[i] = getattr(self,i)
        return json_dic

    def __init__(self, imgurl=None, province=None,city=None,describe=None,createtime=datetime.now().strftime(timeformater),
                 valitime=(datetime.now()+timedelta(days=30)).strftime(timeformater), user = None, user_id = None):
        self.imgurl = imgurl
        self.province = province
        self.city = city
        self.describe = describe
        self.createtime = createtime
        self.valitime = valitime
        self.user = user
        self.user_id = user_id

    def __repr__(self):
        return '<Pet %r>' % (self.id)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    vx = Column(String(32))
    qq = Column(String(16))
    email = Column(String(64))
    province = Column(String(32))
    city = Column(String(64))
    type = Column(Integer)  #0,管理员，1,普通用户，2,异常状态
    createtime = Column(String(32))

    timeformater = '%Y-%m-%d %H:%M:%S'

    def __init__(self, name=None, vx=None,qq=None,email=None,province=None,city=None,type=1,createtime=datetime.now().strftime(timeformater)):
        self.name = name
        self.vx = vx
        self.qq = qq
        self.email = email
        self.province = province
        self.city = city
        self.type = type
        self.createtime = createtime

    def __repr__(self):
        return '<User %r>' % (self.id)


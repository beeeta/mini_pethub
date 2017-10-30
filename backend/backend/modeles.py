from collections import Iterable

from datetime import datetime,timedelta
from passlib.hash import pbkdf2_sha256 as shalib

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship,backref

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,SignatureExpired,BadSignature

from . import app
from .db import Base

class CommonEntity(object):

    out_pros = ()

    timeformater = '%Y-%m-%d %H:%M:%S'

    def to_json_dict(self):
        json_dic = {}
        for i in self.out_pros:
            if type(getattr(self, i)) is str or type(getattr(self, i)) is int:
                json_dic[i] = getattr(self, i)
            elif hasattr(getattr(self,i),'to_json_dict'):
                json_dic[i] = getattr(self,i).to_json_dict()
            elif isinstance(getattr(self,i),Iterable):
                # json_dic[i] = [item.to_json_dict() for item in getattr(self,i)]
                print('-------------------')
                print([item for item in getattr(self,i)])
        return json_dic


class Pet(Base,CommonEntity):

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
    user = relationship('User', lazy='joined')

    out_pros = ('id','imgurl','province','city','describe','createtime','updatetime','valitime','user')

    def __init__(self, imgurl=None, province=None,city=None,describe=None,createtime=datetime.now().strftime(CommonEntity.timeformater),
                 valitime=(datetime.now()+timedelta(days=30)).strftime(CommonEntity.timeformater), user = None, user_id = None):
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


class User(Base,CommonEntity):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password_hash = Column(String(256))
    vx = Column(String(32))
    qq = Column(String(16))
    email = Column(String(64))
    province = Column(String(32))
    city = Column(String(64))
    role_type = Column(Integer)  #0,管理员，1,普通用户，2,异常状态
    createtime = Column(String(32))
    pets = relationship('Pet')

    out_pros = ('id', 'name', 'vx', 'qq', 'email', 'province', 'city', 'type','createtime','pets')

    def hash_password(self, password):
        self.password_hash = shalib.hash(password)

    def verify_password(self, password):
        return shalib.verify(password, self.password_hash)

    def generate_auth_token(self, expiration=600):
        s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = User.query.get(data['id'])
        return user


    def __init__(self, name=None, vx=None,qq=None,email=None,province=None,city=None,role_type=1,createtime=datetime.now().strftime(CommonEntity.timeformater)):
        self.name = name
        self.vx = vx
        self.qq = qq
        self.email = email
        self.province = province
        self.city = city
        self.role_type = role_type
        self.createtime = createtime

    def __repr__(self):
        return '<User %r>' % (self.id)


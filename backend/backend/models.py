from collections import Iterable
from datetime import datetime, timedelta

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from . import db

Base = db.base


class CommonEntity(object):

    out_pros = ()

    timeformat = '%Y-%m-%d %H:%M:%S'

    def to_json_dict(self,isiter=True):
        json_dic = {}
        for i in self.out_pros:
            if type(getattr(self, i)) is str or type(getattr(self, i)) is int:
                json_dic[i] = getattr(self, i)
            elif isiter and hasattr(getattr(self,i),'to_json_dict'):
                json_dic[i] = getattr(self,i).to_json_dict(False)
            elif isiter and isinstance(getattr(self,i),Iterable):
                json_dic[i] = [item.to_json_dict(False) for item in getattr(self,i)]
        return json_dic


class Pet(Base,CommonEntity):

    __tablename__ = 'pets'
    id = Column(Integer, primary_key=True)
    imgurl = Column(String(200))
    province = Column(String(10))
    city = Column(String(10))
    # connection = Column(String(64))
    describe = Column(String(128))
    createtime = Column(String(32))
    updatetime = Column(String(32))
    valitime = Column(String(32))
    users = relationship("Relation", back_populates="pet")

    out_pros = ('id','imgurl','province','city','describe','createtime','updatetime','valitime')

    def __init__(self, imgurl=None, province=None, city=None, describe=None, createtime=datetime.now().strftime(CommonEntity.timeformat),
                 valitime=(datetime.now()+timedelta(days=30)).strftime(CommonEntity.timeformat)):
        self.imgurl = imgurl
        self.province = province
        self.city = city
        self.describe = describe
        self.createtime = createtime
        self.valitime = valitime
        # self.user = user
        # self.user_id = user_id

    def __repr__(self):
        return '<Pet %r>' % (self.id)


class User(Base,CommonEntity):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    # password_hash = Column(String(256))
    vx = Column(String(32))
    qq = Column(String(16))
    email = Column(String(64))
    province = Column(String(32))
    city = Column(String(64))
    role_type = Column(Integer)  #0,管理员，1,普通用户，2,异常状态
    createtime = Column(String(32))

    out_pros = ('id', 'name', 'vx', 'qq', 'email', 'province', 'city', 'role_type', 'createtime')

    pets = relationship("Relation", back_populates="user")

    # def hash_password(self, password):
    #     self.password_hash = shalib.hash(password)
    #
    # def verify_password(self, password):
    #     return shalib.verify(password, self.password_hash)

    # def generate_auth_token(self, expiration=600):
    #     s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
    #     return s.dumps({'id': self.id})

    # @staticmethod
    # def verify_token(token):
    #     s = Serializer(app.config['SECRET_KEY'])
    #     try:
    #         print('token:{}'.format(token))
    #         data = s.loads(token)
    #     except SignatureExpired:
    #         print('================ signature expireds')
    #         return None  # valid token, but expired
    #     except BadSignature:
    #         print('================ bad signature')
    #         return None  # invalid token
    #     user = User.query.get(data['id'])
    #     return user


    def __init__(self, name=None, vx=None, qq=None, email=None, province=None, city=None, role_type=1, createtime=datetime.now().strftime(CommonEntity.timeformat)):
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



class Relation(Base):
    __tablename__ = 'relations'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    pet_id = Column(Integer, ForeignKey('pets.id'), primary_key=True)
    relatypes = Column('relatypes', String(32))
    createtime = Column('createtime', String(32))
    pet = relationship("Pet", back_populates="users")
    user = relationship("User", back_populates="pets")

    def __init__(self,pet=None,user=None):
        self.pet = pet
        self.user = user


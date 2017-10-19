from datetime import datetime

from sqlalchemy import Column, Integer, String, DATETIME
from .db import Base

class Pet(Base):
    __tablename__ = 'pets'
    id = Column(Integer, primary_key=True)
    imgurl = Column(String(200))
    province = Column(String(10))
    city = Column(String(10))
    connection = Column(String(64))
    describe = Column(String(128))
    createtime = Column(DATETIME)
    valitime = Column(DATETIME)


    def __init__(self, imgurl=None, province=None,city=None,connection=None,describe=None,createtime=datetime.now(),valitime=None):
        self.imgurl = imgurl
        self.province = province
        self.city = city
        self.connection = connection
        self.describe = describe
        self.createtime = createtime
        self.valitime = valitime

    def __repr__(self):
        return '<Pet %r>' % (self.imgurl)
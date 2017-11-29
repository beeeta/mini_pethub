from . import Base,session,engine


def init_db():
    from .models import Pet,User,Relation
    Base.metadata.create_all(bind=engine)
    user = User(name='beta2',vx='bbqq2',qq='121212',email='soso@gmail.com',province='湖北',city='武汉')
    pet = Pet(imgurl='2.jpg',province='gd',city='sz',describe='aaaaa')
    relations = Relation(user=user,pet=pet)
    session.add(user)
    session.add(pet)
    session.add(relations)
    session.commit()


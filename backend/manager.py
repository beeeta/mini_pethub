import fire
from backend.db import DBServer

def init():
    db = DBServer()
    db.init_db()

if __name__ == '__main__':
    fire.Fire()





import fire
from backend.db import init_db as init

def init_db():
    init()

if __name__ == '__main__':
    fire.Fire()





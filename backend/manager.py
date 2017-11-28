import fire
from backend.db import init_db

def init():
    init_db()

if __name__ == '__main__':
    fire.Fire()
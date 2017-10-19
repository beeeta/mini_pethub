import click
from backend.db import init_db

@click.command()
def init():
    init_db()

if __name__ == '__main__':
    init()
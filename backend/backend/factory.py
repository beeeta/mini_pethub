from . import app
from .config import config

def create_app(level='default',addconfig={}):
    cfg = config[level]
    cfg.init_app(app)
    app.config.update(addconfig)
    return app

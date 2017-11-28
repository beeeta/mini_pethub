from . import app
from .config import config

def create_app(level='default',ap_config={}):
    cfg = config[level]
    cfg.init_app(app)
    app.config.update(ap_config)
    return app

from . import app
from .config import config
from .db import init_session

def create_app(level='default',ap_config={}):
    cfg = config[level]
    app.config.from_object(cfg)
    cfg.init_app(app)
    app.config.update(ap_config)
    #after load config, begin to init modules
    init_session(app)

    return app

from . import app

def create_app(type='default',ap_config={}):

    app.config.update(ap_config)
    return app

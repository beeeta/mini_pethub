import datetime as dt
import logging
from logging.handlers import RotatingFileHandler
import pytz

from flask import request, session
from structlog import wrap_logger
from structlog.processors import JSONRenderer

from . import app

# Set the logging level
app.logger.setLevel(app.config['LOG_LEVEL'])

# Remove the stdout handler
app.logger.removeHandler(app.logger.handlers[0])

TZ = pytz.timezone(app.config['TIMEZONE'])

def add_fields(_, level, event_dict):
    ''' Add custom fields to each record. '''
    now = dt.datetime.now()
    event_dict['timestamp'] = TZ.localize(now, True).astimezone(pytz.utc).isoformat()
    event_dict['level'] = level

    if session:
        event_dict['session_id'] = session.get('session_id')

    if request:
        try:
            event_dict['ip_address'] = request.headers['X-Forwarded-For'].split(',')[0].strip()
        except:
            event_dict['ip_address'] = 'unknown'

    return event_dict

# Add a handler to write log messages to a file
if app.config.get('LOG_FILE'):
    file_handler = RotatingFileHandler(app.config['LOG_FILENAME'],
                                       app.config['LOG_MAXBYTES'],
                                       app.config['LOG_BACKUPS'],
                                       'a',
                                       encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(file_handler)

# Wrap the application logger with structlog to format the output
logger = wrap_logger(
    app.logger,
    processors=[
        add_fields,
        JSONRenderer(indent=None)
    ]
)
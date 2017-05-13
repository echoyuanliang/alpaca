# coding: utf-8

"""
  __author__ = allen

"""

DEBUG = False

HOST = '0.0.0.0'
PORT = '1993'
SECRET_KEY = 'qwertyuiopasdfghjklzxcvbnm'
LOG_HANDLERS = {
    'FILE': {
        'LOG_PATH': 'logs/app.log',
        'LOG_LEVEL': 'DEBUG' if DEBUG else 'WARNING',
        'MAX_BYTES': 1024 * 1024 * 100,
        'BACKUP_COUNT': 7
    }
}

AUTH_USER = []
AUTH_IP = []

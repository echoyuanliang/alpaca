# coding: utf-8

"""
  __author__ = allen

"""

DEBUG=True

HOST='0.0.0.0'
PORT='1993'
SECRET_KEY = 'qwertyuiopasdfghjklzxcvbnm'
LOG_HANDLERS = {
    'FILE': {
        'LOG_PATH': 'logs/app.log',
        'LOG_LEVEL': 'INFO' if DEBUG else 'WARNING',
        'MAX_BYTES': 1024 * 1024 * 100,
        'BACKUP_COUNT': 7
    }
}

AUTH_USER = ['zhangyuanliang', 'root', 'allen']
AUTH_IP = ['127.0.0.1', '180.153.132.29', '192.168.8.103', '180.159.101.128', '211.161.244.63']

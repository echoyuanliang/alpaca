# coding: utf-8

"""
  __author__ = allen

"""

import socket
import logging
from flask import request
from logging.handlers import RotatingFileHandler

class CustomFormatter(logging.Formatter):

    def format(self, record):
        try:
            setattr(record, 'url', request.path)
        except RuntimeError:
            setattr(record, 'url', 'Null')
        setattr(record, 'hostname', socket.gethostname())
        return logging.Formatter.format(self, record)


class AppLogger:
    def __init__(self, app):
        self.app = app

    @staticmethod
    def get_file_handler(handler_config):
        format_strings = [
            '%(asctime)s',
            '%(levelname)s',
            '%(hostname)s',
            '[URL:%(url)s]',
            '[%(filename)s:%(lineno)d]',
            '%(message)s'
        ]

        file_format = CustomFormatter('  '.join(format_strings))
        file_handle = RotatingFileHandler(filename=handler_config.get('LOG_PATH', 'app.log'), mode='a',
                                          maxBytes=handler_config.get('MAX_BYTES', 1024 * 1024 * 100),
                                          backupCount=handler_config.get('BACKUP_COUNT', 7))
        file_handle.setFormatter(file_format)
        file_handle.setLevel(handler_config.get('LOG_LEVEL', 'ERROR'))
        return file_handle

    def init_handlers(self):
        for handle_name, handler_config in self.app.config['LOG_HANDLERS'].items():
            fn_name = 'get_{0}_handler'.format(handle_name.lower())
            handler = getattr(self, fn_name)(handler_config)
            self.app.logger.addHandler(handler)

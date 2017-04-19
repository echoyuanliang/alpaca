# coding: utf-8

"""
  __author__ = allen

"""

from flask import request, session, abort
from app.lib.logger import AppLogger

class MakeApp:
    def __init__(self, app):
        self.app = app

    def init_all(self):
        self.init_config()
        self.init_log()
        self.init_before()


    def init_config(self):
        self.app.config.from_object('config')

    def init_log(self):
        AppLogger(self.app).init_handlers()

    def init_before(self):
        @self.app.before_request
        def before_request():
            ip_list = request.headers.getlist("X-Forwarded-For")
            session['remote_address'] = ip_list[0].split(',')[0] if ip_list else request.remote_addr
            if session['remote_address'] in self.app.config['AUTH_IP']:
                return
            else:
                abort(403)


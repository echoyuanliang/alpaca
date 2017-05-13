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
        self.init_modules()

    def init_config(self):
        self.app.config.from_object('config')
        self.app.config.from_pyfile('config.py')

    def init_log(self):
        AppLogger(self.app).init_handlers()

    def init_before(self):
        @self.app.before_request
        def before_request():

            ip_list = request.headers.getlist("X-Forwarded-For")
            session['remote_address'] = ip_list[0].split(',')[0] if ip_list else request.remote_addr
            if self.app.config['AUTH_IP'] and session['remote_address'] not in self.app.config['AUTH_IP']:
                abort(403)
            if not session.get('login') and request.path != '/login':
                abort(403)

    def init_modules(self):
        from app.views import *

        modules = (
            (basic_bp, '/api/basic'),
            (network_bp, '/api/network'),
            (system_bp, '/api/system')
        )

        for module, url_prefix in modules:
            self.app.register_blueprint(module, url_prefix=url_prefix)

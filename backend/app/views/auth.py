# coding: utf-8

"""
  __author__ = allen

"""

import time
from flask import request, session, make_response, jsonify, abort
from simplepam import authenticate
from app.main import app


@app.route('/api/login', methods=['POST'])
def login():
    params = request.json
    auth_users = app.config.get('AUTH_USER', [])
    try:
        username = str(params.get('username', '').strip())
        password = str(params.get('password', '').strip())

        if username and password and username in auth_users:
            auth = authenticate(username, password, service='login', encoding='utf-8', resetcred=True)
            if auth:
                app.logger.info('user {0} login from {1}'.format(username, session['remote_address']))
                session['login'] = '{0}-{1}'.format(username, time.time())
                return make_response(jsonify(code=200, data={'user': username, 'code': 200}), 200)
    except Exception as e:
        abort(403, msg=str(e))

    abort(403)

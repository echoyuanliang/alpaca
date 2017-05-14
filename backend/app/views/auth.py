# coding: utf-8

"""
  __author__ = allen

"""

import time
from flask import request, session, make_response, jsonify, abort
from simplepam import authenticate
from app.main import app


@app.route('/login', methods=['POST'])
def login():
    params = request.json
    auth_users = app.config.get('AUTH_USER', [])
    try:
        username = str(params.get('username', '').strip())
        password = str(params.get('password', '').strip())

        if auth_users and username not in auth_users:
            abort(401, msg='user {0} has no privilege login'.format(username))

        if username and password:
            auth = authenticate(username, password, service='login', encoding='utf-8', resetcred=True)
            if auth:
                app.logger.info('user {0} login from {1}'.format(username, session['remote_address']))
                session['login'] = '{0}-{1}'.format(username, time.time())
                return make_response(jsonify(code=200, data={'user': username, 'code': 200}), 200)
        else:
            abort(401, msg='username and password is required')
    except Exception as e:
        abort(401, msg=str(e))

    abort(401, msg='auth failed')

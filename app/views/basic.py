# coding: utf-8

"""
  __author__ = allen

"""

from flask import make_response, jsonify
from app.main import app

@app.route('/basic', methods=['GET'])
def basic_info():
    return make_response(jsonify(code=200, message='ok'), 200)



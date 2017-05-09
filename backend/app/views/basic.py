# coding: utf-8

"""
  __author__ = allen

"""

from flask import make_response, jsonify, Blueprint
from app.lib import basic

basic_bp = Blueprint('basic', __name__)


@basic_bp.route('/', methods=['GET'])
def basic_info():
    basic_item = {
        'general': basic.get_general(),
        'cpu': basic.get_cpu_info(),
        'disk': basic.get_disk_info(),
        'net': basic.get_net_info()
    }
    return make_response(jsonify(code=200, data=basic_item), 200)


@basic_bp.route('/general', methods=['GET'])
def basic_general():
    return make_response(jsonify(code=200, data=basic.get_general()))


@basic_bp.route('/cpu', methods=['GET'])
def basic_cpu():
    return make_response(jsonify(code=200, data=basic.get_cpu_info()))


@basic_bp.route('/disk', methods=['GET'])
def basic_net():
    return make_response(jsonify(code=200, data=basic.get_net_info()))

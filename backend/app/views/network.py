# coding: utf-8

"""
  __author__ = allen

"""

from flask import make_response, jsonify, Blueprint
from app.lib import network

network_bp = Blueprint('network_bp', __name__)

@network_bp.route('/')
def network_info():
    data = {
        'connections': network.get_connections(),
        'iface_status': network.get_iface_status()
    }
    return make_response(jsonify(data=data, code=200), 200)

@network_bp.route('/conn/')
def network_conns():
    return make_response(jsonify(data=network.get_connections(), code=200), 200)

@network_bp.route('/iface')
def network_iface():
    return make_response(jsonify(data=network.get_iface_status(), code=200), 200)

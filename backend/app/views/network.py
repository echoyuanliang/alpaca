# coding: utf-8

"""
  __author__ = allen

"""

from flask import make_response, jsonify, Blueprint
from app.handler import net_handler

network_bp = Blueprint('network_bp', __name__)


@network_bp.route('/')
def network_info():
    data = net_handler.get_network_info()
    return make_response(jsonify(data=data, code=200), 200)


@network_bp.route('/conn/')
def network_conns():
    data = net_handler.get_network_info()
    return make_response(jsonify(data=data.get('connections', {}), code=200), 200)


@network_bp.route('/iface')
def network_iface():
    data = net_handler.get_network_info()
    return make_response(jsonify(data=data.get('iface_status', []), code=200), 200)

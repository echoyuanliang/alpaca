# coding: utf-8

"""
  __author__ = allen

"""

from flask import make_response, jsonify, Blueprint, request
from app.lib import system
from app.handler import system_handler
system_bp = Blueprint('system_bp', __name__)


@system_bp.route('/')
def system_info():
    data = system_handler.get_system()
    return make_response(jsonify(code=200, data=data), 200)


@system_bp.route('/load')
def system_load():
    data = system_handler.get_system()
    return make_response(jsonify(code=200, data=data.get('loadavg', {})), 200)


@system_bp.route('/cpu_stat')
def system_cpu_stat():
    data = system_handler.get_system()
    return make_response(jsonify(code=200, data=data.get('cpu_stat', {})), 200)


@system_bp.route('/processes')
def system_intensive_processes():
    data = system_handler.get_system()
    return make_response(jsonify(code=200, data=data.get('intensive_processes', {})), 200)


@system_bp.route('/io_counters')
def system_io_counters():
    data = system_handler.get_system()
    return make_response(jsonify(code=200, data=data.get('io_counters', {})), 200)


@system_bp.route('/mem')
def system_mem_info():
    data = system_handler.get_system()
    return make_response(jsonify(code=200, data=data.get('mem_info', {})))


@system_bp.route('/process/<int:pid>')
def system_process_detail(pid):
    return make_response(jsonify(code=200, data=system.get_process_detail(pid)))


@system_bp.route('/process_search')
def system_process_search():
    q = request.values.get('q', '')
    return make_response(jsonify(code=200, data=system.search_process(q)))


@system_bp.route('/process_simple')
def system_process_simple():
    pids = request.values.get('pids', [])
    return make_response(jsonify(code=200, data=system.get_simple_process(pids)))

# coding: utf-8

"""
  __author__ = allen

"""

from flask import make_response, jsonify, Blueprint, request

from app.lib import system

system_bp = Blueprint('system_bp', __name__)

@system_bp.route('/')
def system_info():
    data = {
        'loadavg': system.get_loadavg(),
        'cpu_stat': system.get_cpu_stat(),
        'intensive_processes': system.get_intensive_processes(),
        'pstree': system.get_pstree()
    }

    return make_response(jsonify(code=200, data=data), 200)

@system_bp.route('/load')
def system_load():
    return make_response(jsonify(code=200, data=system.get_loadavg()), 200)

@system_bp.route('/cpu_stat')
def system_cpu_stat():
    return make_response(jsonify(code=200, data=system.get_cpu_stat()), 200)

@system_bp.route('/processes')
def system_intensive_processes():
    return make_response(jsonify(code=200, data=system.get_intensive_processes()), 200)

@system_bp.route('/pstree')
def system_intensive_process():
    return make_response(jsonify(code=200, data=system.get_pstree()), 200)

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

# coding: utf-8

"""
  __author__ = allen

"""

import psutil
import datetime
import socket
from collections import defaultdict
from app.lib.util import obj2dict
from app.lib.const import SOCK_TYPE


def get_loadavg():
    load_file = '/proc/loadavg'

    with open(load_file, 'r') as lfp:
        line = lfp.readline()
        items = [item.strip() for item in line.split(' ') if item.strip()]
        return {
            '1min': float(items[0]) * 100,
            '3min': float(items[1]) * 100,
            '5min': float(items[2]) * 100
        }


def _parse_cpu_fields(fields):
    field_list = [int(field) for field in fields]
    total = sum(field_list)
    return {
        'total': total,
        'user': field_list[1],
        'nice': field_list[2],
        'system': field_list[2],
        'idle': field_list[3],
        'iowait': field_list[4],
        'irq': field_list[5],
        'soft_irq': field_list[6],
        'steal': field_list[7],
        'guest': field_list[8]
    }


def get_cpu_stat():
    cpu_stat_file = '/proc/stat'

    cpu_stat = dict(cpus=dict())
    with open(cpu_stat_file, 'r') as cfp:
        for line in cfp.xreadlines():
            fields = [field.strip() for field in line.split(' ') if field.strip()]
            if len(fields) < 2:
                continue

            field_name = fields[0]
            if field_name.startswith('cpu'):
                cpu_stat['cpus'][field_name] = _parse_cpu_fields(fields[1:])
            elif field_name in ['ctxt', 'processes', 'procs_running', 'procs_blocked']:
                cpu_stat[field_name] = int(fields[1])

    return cpu_stat


def _proc2simple(proc):

    with proc.oneshot():
        return {
            'pid': proc.pid,
            'name': proc.name(),
            'cmdline': ''.join(proc.cmdline()),
            'username': proc.username(),
            'create_time': datetime.datetime.fromtimestamp(proc.create_time()).strftime("%Y-%m-%d %H:%M:%S"),
            'cpu_percent': round(proc.cpu_percent(), 2),
            'memory_percent': round(proc.memory_percent(), 2),
            'status': proc.status()
        }


def get_intensive_processes():
    procs = map(_proc2simple, psutil.process_iter())
    cpu_intensive = sorted(procs, cmp=lambda x, y: x['cpu_percent'] < y['cpu_percent'], reverse=True)[0: 20]
    mem_intensive = sorted(procs, cmp=lambda x, y: x['memory_percent'] < y['memory_percent'], reverse=True)[0:20]

    return {
        'cpu_intensive': cpu_intensive,
        'mem_intensive': mem_intensive
    }


def get_simple_process(pids):
    simple_process = []
    for process in psutil.process_iter():
        if pids and process.pid not in pids:
            continue

        simple_process.append(_proc2simple(process))

    return simple_process


def get_children(nodes_dict, parent):

    nodes = nodes_dict[parent]
    children = list()

    for child in nodes:
        children.append({
            'process': child,
            'children': get_children(nodes_dict, child)
        })

    return children


def transfer_nodes2tree(nodes_dict, child_nodes):

    tree = list()
    for parent, cur_children in nodes_dict.items():
        if parent not in child_nodes:  # first level
            tree.append({
                'process': parent,
                'children': get_children(nodes_dict, parent)
            })
    return tree


def conn2json(conn):
    laddr = map(str, conn.laddr)
    raddr = map(str, conn.raddr)
    return {
        'fd': conn.fd,
        'laddr': ':'.join(laddr),
        'raddr': ':'.join(raddr),
        'status': conn.status,
        'type': SOCK_TYPE.get(socket.SOCK_STREAM, 'raw')
    }


def get_pstree():

    nodes_dict = dict()
    child_nodes = []
    for process in psutil.process_iter():
        cur_child_nodes = ['{0}-{1}'.format(child.pid, child.name()) for child in process.children()]
        nodes_dict['{0}-{1}'.format(process.pid, process.name())] = cur_child_nodes
        child_nodes.extend(cur_child_nodes)

    return transfer_nodes2tree(nodes_dict, child_nodes)


def children_processor(children):
    return [{'pid': child.pid, 'name': child.name()} for child in children]


def get_process_detail(pid):
    for process in psutil.process_iter():
        if process.pid == pid:
            cur_process = process
            break
    else:
        raise Exception('No such process: {0}'.format(pid))

    override = {
        type(cur_process): {
            'children': children_processor,
            'parent': lambda p: {'pid': p.pid, 'name': p.name()} if p else None,
            'cmdline': lambda lines: ' '.join(lines),
            'connections': lambda conns: map(conn2json, conns),
            'create_time': lambda timestamp: datetime.datetime.fromtimestamp(
                timestamp).strftime("%Y-%m-%d %H:%M:%S")
        }
    }

    ignore = {
        type(cur_process): ['kill', 'oneshot', 'environ', 'send_signal', 'suspend',
                            'as_dict', 'uids', 'gids', 'terminal', 'is_running',
                            'ionice', 'rlimit', 'memory_info_ex', 'memory_info',
                            'resume', 'terminate', 'wait', 'memory_maps']
    }

    return obj2dict(cur_process, methods=True,
                    override=override, ignore=ignore)


def search_process(q):
    process_map = defaultdict(list)

    for process in psutil.process_iter():
        name = process.name()
        pid = process.pid
        pid_str = str(process.pid)
        cmdline = ''.join(process.cmdline())

        if name != '' and name.find(q) != -1:
            process_map[name].append(pid)
        if cmdline != '' and cmdline.find(q) != -1:
            process_map[cmdline].append(pid)
        if pid_str.find(q) != -1:
            process_map[pid_str].append(pid)
    return process_map

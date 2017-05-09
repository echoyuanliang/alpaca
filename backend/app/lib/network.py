# coding: utf-8

"""
  __author__ = allen

"""

import subprocess


def get_connections():
    conn_cmd = 'netstat -natp'
    conn_out = subprocess.check_output(conn_cmd, shell=True)
    conn_lines = conn_out.splitlines()[2:]
    count = len(conn_lines)
    conns = {'conns': list(), 'count': count}
    for line in conn_lines:
        items = [item.strip() for item in line.split(' ') if item.strip()]
        conns['conns'].append({
            'status': items[5],
            'recv_q': int(items[1]),
            'send_q': int(items[2]),
            'l_addr': items[3],
            'r_addr': items[4],
            'pid': items[6].split('/')[0]
        })

    return conns


def get_iface_status():
    iface_files = '/proc/net/dev'
    iface_info = dict()
    with open(iface_files, 'r') as ifp:
        lines = ifp.readlines()[2:]
        for line in lines:
            items = [item.strip() for item in line.split(' ') if item.strip()]

            iface_info[items[0][:-1]] = {
                'receive_bytes': int(items[1]),
                'receive_packets': int(items[2]),
                'send_bytes': int(items[9]),
                'send_packets': int(items[10])
            }

    return iface_info

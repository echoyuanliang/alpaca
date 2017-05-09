# coding: utf-8

"""
  __author__ = allen

"""

import datetime
import platform
import socket
import subprocess
import psutil
from uptime import uptime
from app.lib.util import bytes2human


def _seconds2human(seconds):
    m,s = divmod(seconds, 60)
    h,m = divmod(m, 60)
    d,h = divmod(h, 24)

    time_str = u'{0}天, {1}小时, {2}分, {3}秒'.format(int(d), int(h), int(m), int(s))
    return time_str


def get_general():
    return {
        'hostname': socket.gethostname(),
        'os_name': platform.system(),
        'os_version': platform.release(),
        'server_time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'sys_up': _seconds2human(uptime())
    }


def get_disk_info():
    disk_info = []

    partitions = psutil.disk_partitions(all=False)
    for partition in partitions:
        disk_usage = psutil.disk_usage(partition.mountpoint)
        disk_item = {
            'device': partition.device,
            'mountpoint': partition.mountpoint,
            'fstype': partition.fstype,
            'total': bytes2human(disk_usage.total),
            'used': bytes2human(disk_usage.used),
            'free': bytes2human(disk_usage.free),
            'percent': disk_usage.percent
        }

        disk_info.append(disk_item)
    return disk_info


def get_cpu_info():
    cmd = '/usr/bin/lscpu'
    out = subprocess.check_output(cmd, shell=True)
    cpu_info = dict()
    public_keys = ['Architecture', 'Byte Order', 'CPU MHz', 'CPU(s)']
    public_pattern = 'cache'

    for line in out.splitlines():
        k, v = [item.strip() for item in line.split(':')]
        if k in public_keys or k.find(public_pattern) != -1:
            k = k.replace(' ', '_').replace('(', '').replace(')', '').lower()
            cpu_info[k] = v
    return cpu_info


def get_net_info():
    if_addrs = psutil.net_if_addrs()
    net_info = list()
    for interface, addrs in if_addrs.items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                net_info.append({
                    'interface': interface,
                    'address': addr.address,
                    'netmask': addr.netmask
                })

    return net_info

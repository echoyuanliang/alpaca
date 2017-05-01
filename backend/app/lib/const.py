# coding: utf-8

"""
  __author__ = allen

"""

import socket

SOCK_TYPE = {
    socket.SOCK_STREAM: 'tcp',
    socket.SOCK_DGRAM: 'udp',
    socket.SOCK_RAW: 'raw',
    socket.SOCK_RDM: 'rdm',
    socket.SOCK_SEQPACKET: 'seqpkg'
}

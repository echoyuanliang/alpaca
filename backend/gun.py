# -*- coding: utf-8 -*-
import multiprocessing

bind = "0.0.0.0:8080"
pidfile = 'var/gunicorn.pid'
workers = multiprocessing.cpu_count() * 2 + 1

worker_class = 'sync'
backlog = 2048
daemon = True
loglevel = 'info'
accesslog = 'logs/access.log'
errorlog = 'logs/error.log'
access_log_format = "%({X-Real-IP}i)s %(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s"

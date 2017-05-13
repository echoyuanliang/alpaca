# alpaca 

> 一个基于`vue2.0` `python2.7` `flask`的简单linux dashboard, 用于收集、统计和展示linux操作系统信息,主要包括四个维度的信息：
> 
> 1. 基本信息: ip，hostname，cpu配置信息，磁盘分区信息等;
> 
> 2. 系统信息: 前load及变化趋势，cpu空闲率，cpu时间分布，内存使用率，内存使用分布，占用 
> cpu／内存比较多的进程， IO读写数量，以及耗费的时间等；
> 
> 3. 网络信息: 各个网卡的进出流量统计和走势，网络连接的详情以及各状态统计；
> 
> 4. 进程信息: 显示特定进程的详情，包括进程的内存使用情况，cpu使用情况，创建时间，状态，
> IO情况，子进程列表，网络连接列表，打开的文件描述符列表，启动的线程列表等；

## 安装
### 环境要求
linux操作系统；python2.7; node >= 4.0.0; npm>= 3.0.0
### 安装和启动
> 1. 确保目标机器环境符合要求
> 
> 2. 将代码clone到目标机器，进入代码文件目录，可以看到其中有以alpaca命名的管理脚本, 管理脚本提供了`build`(安装程序依赖包，打包前端的js，css文件等操作）, `start`， `stop`，`restart`，`status`等功能，因此，代码刚clone到本地或者修改以后，需要重新build，然后再start.
> 


	git clone git@github.com:echoyuanliang/alpaca.git
	cd alpaca 
	bash alpaca build
	bash alpaca start

### 相关配置

* 程序使用gunicorn托管（也可以直接使用run.py启动）,guncorn启动配置文件路径为`backend/gun.py`.默认配置如下，默认端口为`8080`，也是此处配置:


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


* 应用程序配置文件路径为`backend/config.py`, alpaca使用linux的用户，密码来管理登陆的用户，因此需要配置那些用户具有访问权限，配置项为`AUTH_USER`, 如果不配置或配置为空数组，则所有用户均有权限登录, 同时，alpaca仅对白名单ip授予访问权限，配置项为`AUTH_IP`，如果不配置或配置项为空数组，则所有ip均有权限登录。
## 技术栈
`python` `flask` `ecmascript6` `vue2.0`

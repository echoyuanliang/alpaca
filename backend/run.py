# coding: utf-8

"""
  __author__ = allen

"""

from flask_script import Manager, Server
from flask_script.commands import ShowUrls, Clean

from app.main import app

manager = Manager(app)

manager.add_command('clean', Clean())
manager.add_command('url', ShowUrls())
manager.add_command('server', Server(host=app.config.get('HOST', '0.0.0.0'),
                                     port=app.config.get('PORT', 8080)))

if __name__ == '__main__':
    manager.run()

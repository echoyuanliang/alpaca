# coding: utf-8

"""
  __author__ = allen

"""

from flask import Flask, render_template
from app.make_app import MakeApp

app = Flask(__name__, instance_relative_config=True)

with app.app_context():
    make = MakeApp(app)
    make.init_all()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')




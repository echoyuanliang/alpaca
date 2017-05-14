# coding: utf-8

"""
  __author__ = allen

"""

from flask import Flask, render_template, make_response, jsonify
from app.make_app import MakeApp

app = Flask(__name__, instance_relative_config=True)

with app.app_context():
    make = MakeApp(app)
    make.init_all()


@app.errorhandler(404)
def page_not_found(e):
    return make_response(jsonify(msg=str(e), code=404), 404)


@app.errorhandler(401)
def unauthorized_visit(e):
    return make_response(jsonify(msg=str(e), code=401), 401)


@app.errorhandler(500)
def unauthorized_visit(e):
    return make_response(jsonify(msg=str(e), code=500), 500)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')




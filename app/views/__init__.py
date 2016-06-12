#-*- coding: UTF-8 -*-

from flask import Blueprint
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.admin import Admin


admin = Admin(name="Interface")
auth = HTTPBasicAuth()
users = Blueprint('users', __name__, url_prefix='/users')

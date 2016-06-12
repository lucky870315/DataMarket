#-*- coding: UTF-8 -*-
from flask import Blueprint

admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates', static_url_path='', static_folder='static')
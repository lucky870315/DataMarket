#-*- coding: UTF-8 -*-
from flask import Blueprint

dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard', template_folder='templates', static_url_path='', static_folder='static')
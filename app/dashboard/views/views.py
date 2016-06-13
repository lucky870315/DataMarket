#-*- coding: UTF-8 -*-

from flask import render_template
from app.dashboard import dashboard


@dashboard.route('/index', methods=['GET'])
def index():
    return render_template("dashboard/index.html")
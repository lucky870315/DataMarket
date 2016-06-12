#-*- coding: UTF-8 -*-

from flask import render_template
from . import dashboard


@dashboard.route('/test', methods=['GET'])
def get_resource():
    return render_template("dashboard/test.html")
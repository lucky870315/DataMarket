#-*- coding: UTF-8 -*-

from flask import render_template
from app.dashboard import dashboard


@dashboard.app_errorhandler(404)
def handle_404(err):
    return render_template('dashboard/404.html'), 404


@dashboard.app_errorhandler(500)
def handle_500(err):
    return render_template('dashboard/500.html'), 500
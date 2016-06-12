#-*- coding: UTF-8 -*-

from flask import render_template


def register_errorhandlers(app):
    def render_error(error):
        error_code = getattr(error, 'code', 500)
        return render_template("admin/{0}.html".format(error_code)), error_code

    for errcode in [404,500]:
        app.errorhandler(errcode)(render_error)

    return None
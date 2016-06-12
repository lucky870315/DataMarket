#-*- coding: UTF-8 -*-

from flask import Flask

from config import *


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # from app.admin.views.admin import admin1, add_views, security, user_datastore
    # admin1.init_app(app)
    # security.init_app(app, user_datastore)
    # add_views()

    from app.admin.models import db
    db.init_app(app)

    from app.admin import admin
    app.register_blueprint(admin)

    from api.views.views import api
    app.register_blueprint(api)

    from dashboard.views.views import dashboard
    app.register_blueprint(dashboard)

    from app.errors import register_errorhandlers
    register_errorhandlers(app)

    return app
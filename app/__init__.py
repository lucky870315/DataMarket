#-*- coding: UTF-8 -*-

from flask import Flask
from config import *


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from views.admin import admin, add_views, security, user_datastore
    admin.init_app(app)
    security.init_app(app, user_datastore)
    add_views()

    from app.models import db
    db.init_app(app)

    from views.errors import register_errorhandlers
    register_errorhandlers(app)

    from views.users import users
    app.register_blueprint(users)

    from api.views.views import api
    app.register_blueprint(api)

    from dashboard.views.views import dashboard
    app.register_blueprint(dashboard)

    return app
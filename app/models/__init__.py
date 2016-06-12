#-*- coding: UTF-8 -*-

from flask import current_app, request, json
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import *
from flask.ext.security import current_user, login_required, RoleMixin, Security, SQLAlchemyUserDatastore, UserMixin, utils

db = SQLAlchemy()

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.String(128), db.ForeignKey('user.id')),
    db.Column('role_id', db.String(128), db.ForeignKey('role.id'))
)


class Serializer(object):
    __public__ = None
    "Must be implemented by implementors"
    def to_serializable_dict(self):
        dict = {}
        for public_key in self.__public__:
            value = getattr(self, public_key)
            if value:
                dict[public_key] = value
        return dict


class SWEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Serializer):
            return obj.to_serializable_dict()
        if isinstance(obj, (datetime)):
            return obj.isoformat()
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


def SWJsonify(*args, **kwargs):
    return current_app.response_class(json.dumps(dict(*args, **kwargs), cls=SWEncoder, indent=None if request.is_xhr else 2), mimetype='application/json')
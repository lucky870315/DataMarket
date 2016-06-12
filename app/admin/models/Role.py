#-*- coding: UTF-8 -*-

from flask.ext.security import RoleMixin

from app.admin.models import db


# Role class
class Role(db.Model, RoleMixin):

    # Our Role has three fields, ID, name and description
    id = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    # __str__ is required by Flask-Admin, so we can have human-readable values for the Role when editing a User.
    # If we were using Python 2.7, this would be __unicode__ instead.
    def __str__(self):
        return self.name

    # __hash__ is required to avoid the exception TypeError: unhashable type: 'Role' when saving a User
    def __hash__(self):
        return hash(self.name)

#-*- coding: UTF-8 -*-

import uuid
from flask import current_app
from app.models import db, roles_users, Serializer as ModelSerializer
from passlib.apps import custom_app_context as password_context
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)


class User(db.Model, ModelSerializer):
    __tablename__ = 'user'
    __public__ = ['id','username','password','sex']

    id = db.Column(db.String(128), primary_key=True)
    username = db.Column(db.String(128))
    password = db.Column(db.String(255))
    sex = db.Column(db.Integer)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())

    roles = db.relationship(
        'Role',
        secondary=roles_users,
        backref=db.backref('users', lazy='dynamic')
    )

    # def __init__(self, username, password):
    #     self.id = uuid.uuid1()
    #     self.username = username
    #     self.password = password_context.encrypt(password)

    def hash_password(self, password):
        self.password = password_context.encrypt(password)

    def verify_password(self, password):
        return password_context.verify(password, self.password)

    def generate_auth_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None    # valid token, but expired
        except BadSignature:
            return None    # invalid token
        user = User.query.get(data['id'])
        return user

    def __repr__(self):
        return "id:{}-name:{}-pwd:{}".format(self.user_id, self.username, self.password)
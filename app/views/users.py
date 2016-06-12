#-*- coding: UTF-8 -*-

from flask import g, jsonify, request, abort, url_for, make_response

from ..views import users, auth
from ..models import SWJsonify, db
from ..models.User import User


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@users.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return SWJsonify({'users': users})


@users.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(400)
    return jsonify({'username': user.username})


@users.route('/token', methods=['GET'])
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})


@users.route("/reg", methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400) # missing arguments
    if User.query.filter_by(username=username).first() is not None:
        abort(400) # existing user
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({ 'username': user.username }), 201, {'Location': url_for('users.get_user', user_id=user.user_id, _external=True)}
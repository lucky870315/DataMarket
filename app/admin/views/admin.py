# #-*- coding: UTF-8 -*-
#
# import uuid
#
# from flask import url_for, render_template
# from flask.ext.admin import BaseView, expose
# from flask.ext.admin.contrib.sqla import ModelView
# from flask.ext.security import Security, utils, SQLAlchemyUserDatastore, current_user, login_required
# from wtforms.fields import PasswordField
# from ..models import db
# from ..models.Role import Role
#
# from app.admin.models.User import User
# from . import admin1
# from app.admin import admin
#
# security = Security()
# user_datastore = SQLAlchemyUserDatastore(db, User, Role)
#
#
# class MyView(BaseView):
#     @expose('/')
#     def index(self):
#         url = url_for(".test")
#         return self.render('admin/index.html', url=url)
#
#     @expose('/test/')
#     def test(self):
#         return self.render('admin/test.html')
#
# @admin.route('/')
# # Users must be authenticated to view the home page, but they don't have to have any particular role.
# # Flask-Security will display a login form if the user isn't already authenticated.
# @login_required
# def index():
#     return render_template('admin/index.html')
#
#
# # Customized Role model for SQL-Admin
# class RoleAdmin(ModelView):
#
#     # Prevent administration of Roles unless the currently logged-in user has the "admin" role
#     def is_accessible(self):
#         return current_user.has_role('admin')
#
#     def __init__(self, session, **kwargs):
#         super(RoleAdmin, self).__init__(Role, session, **kwargs)
#
#
# class UserAdmin(ModelView):
# #    can_create = False
#     column_exclude_list = ('password', )
#     form_excluded_columns = ('password', )
#     # form_overrides = dict(sex=SelectField)
#     # form_args = dict(
#     #     # Pass the choices to the `SelectField`
#     #     sex=dict(
#     #         choices=[(0, u'男'), (1, u'女')]
#     #     ))
#
#     def scaffold_form(self):
#
#         # Start with the standard form as provided by Flask-Admin. We've already told Flask-Admin to exclude the
#         # password field from this form.
#         form_class = super(UserAdmin, self).scaffold_form()
#
#         # Add a password field, naming it "password2" and labeling it "New Password".
#         form_class.password2 = PasswordField('New Password')
#         return form_class
#
#     def on_model_change(self, form, model, is_created):
#
#         model.id = uuid.uuid1()
#
#         # If the password field isn't blank...
#         if len(model.password2):
#             # ... then encrypt the new password prior to storing it in the database. If the password field is blank,
#             # the existing password in the database will be retained.
#             model.password = utils.encrypt_password(model.password2)
#
#     def __init__(self, session, **kwargs):
#         super(UserAdmin, self).__init__(User, session, **kwargs)
#
#
# def add_views():
#     admin1.add_view(MyView(name='hello'))
#     admin1.add_view(UserAdmin(db.session))
#     admin1.add_view(RoleAdmin(db.session))
#
#

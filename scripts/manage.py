#!/usr/bin/env python
from app.models import db
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager, Shell, prompt_bool

from app import create_app
from app.admin.models.User import User

app = create_app("development")
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def create():
    db.create_all()

@manager.command
def drop():
    if prompt_bool("Are you sure you want to drop all your data"):
        db.drop_all()

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()
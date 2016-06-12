#-*- coding: UTF-8 -*-

import flask_sqlalchemy
from flask_sqlalchemy import (
    SQLAlchemy,
    _BoundDeclarativeMeta,
)


class ModelMeta(_BoundDeclarativeMeta):
    pass

# 此处类似于 gevent monkey patch 将 socket hook 的方式,
# 这里对 _BoundDeclarativeMeta 运行时被重新赋值.
flask_sqlalchemy._BoundDeclarativeMeta = ModelMeta


db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True
    _column_name_sets = NotImplemented

    def to_dict(self):
        """
        """
        return dict(
            (column_name, getattr(self, column_name, None)) \
            for column_name in self._column_name_sets
        )

    @classmethod
    def get_column_name_sets(cls):
        """
        """
        return cls.__column_name_sets

    __str__ = lambda self: str(self.to_dict())
    __repr__ = lambda self: repr(self.to_dict())


    def modelmeta__new__(cls, name, bases, namespace, **kwds):
        column_name_sets = set()
        for k, v in namespace.items():
            if getattr(v, '__class__', None) is None:
                continue
            if v.__class__.__name__ == 'Column':
                column_name_sets.add(k)

        obj = type.__new__(cls, name, bases, dict(namespace))
        obj._column_name_sets = column_name_sets
        return obj

# modify BaseModel' metatype ModelMeta' __new__ definition
setattr(ModelMeta, '__new__', modelmeta__new__)
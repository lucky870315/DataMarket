#-*- coding: UTF-8 -*-

from sqlalchemy import *
from sqlalchemy.schema import *
from config import *


def create_db():
    db = create_engine(config['api'].SQLALCHEMY_DATABASE_URI, echo=True)
    return db

db_engine = create_db()
meta = MetaData()
quotation_h = Table("T_QUOTATION_H", meta, autoload=True, autoload_with=db_engine)

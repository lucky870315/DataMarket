#-*- coding: UTF-8 -*-

from flask import g, jsonify
import json

from app.views import auth
from . import api
from sqlalchemy import *
from sqlalchemy.sql import select
from sqlalchemy.schema import *
from ..models import db_engine, meta, quotation_h
from app.models import SWJsonify


@api.route('/res', methods=['GET'])
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello,%s' % g.user.username})



@api.route('/quotation/<string:commodity>', methods=['GET'])
def get_quotation(commodity):
    sql=select([quotation_h]).where(quotation_h.c.commodityid==commodity) # 提供查询条件
    conn=db_engine.connect()
    result=conn.execute(sql)
    quotation = []

#    result.close()
    for row in result:
        row_data = [row[quotation_h.c.cleardate].strftime("%Y-%m-%d"), row[quotation_h.c.openprice], row[quotation_h.c.closeprice], row[quotation_h.c.lowprice], row[quotation_h.c.highprice]]
        quotation.append(row_data)
    conn.close()
    return SWJsonify({'quotation': quotation})
#    return jsonify({quotation})  # 看这里，直接用t.c.name就可以调用name列的值了，c代表column。不用做映射，不用配置文件，简单到无语吧？...

# remember to close the cursor

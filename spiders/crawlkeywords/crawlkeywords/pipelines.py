# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json,os,codecs
from . import settings
import pymongo
from scrapy.exceptions import DropItem

basedir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


class CrawlkeywordsPipeline(object):
    def __init__(self):
        self.file = codecs.open(basedir + '/jsons/keywords.json', 'wb', encoding='utf-8')
        # self.server = settings['MONGODB_SERVER']
        # self.port = settings['MONGODB_PORT']
        # self.db = settings['MONGODB_DB']
        # self.col = settings['MONGODB_COLLECTION']
        # connection = pymongo.Connection(self.server, self.port)
        # db = connection[self.db]
        # self.collection = db[self.col]

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line.decode("unicode_escape"))
        # return item
#        self.collection.insert(dict(item))
        return item


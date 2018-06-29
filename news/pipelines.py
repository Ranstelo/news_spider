# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from news.items import NewsItem

client = MongoClient()
collection = client["news"]["toutiao"]

class NewsPipeline(object):
    def process_item(self, item, spider):
        print(item)
        if isinstance(item,NewsItem):
            collection.insert(dict(item))
        return item

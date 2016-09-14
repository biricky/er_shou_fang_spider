# -*- coding: utf-8 -*-
import json
import codecs
import os

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HireToolPipeline(object):
    def __init__(self):
        if not os.path.exists('../data'):
            os.system('mkdir data')
        file_name = 'data/chaoyang.dat'
        self.file = codecs.open(file_name, 'wb', encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode("unicode_escape"))
        return item

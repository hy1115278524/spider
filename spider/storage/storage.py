#!/usr/bin/env python
# encoding: utf-8
# Author: Feniox

import logging
from pymongo import MongoClient
from datetime import datetime

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./storage.log',
                    filemode='w')

class Modules:
    '''存储数据'''
    def __init__(self):
        '''初始化数据'''
        self.client = MongoClient()
        self.db = self.client.pic
        self.collection = self.db.pic_collection
        logging.info('pic database start!')

    def insert(self, pic_info, pic):
        '''向数据库插入图片信息'''
        pic_id = pic_info['pic_id']
        pic_format = pic_info['pic_format']
        self.insert_one(pic_info)
        with open('./pic/'+pic_id+pic_format, 'wb') as f:
            f.write(pic)
        logging.info('Insert a new pic_info!')

    def find(self, pic_id):
        '''在数据库中查询图片信息'''
        info = self.collection.find_one({'pic_id'}:pic_id)
        logging.info('User find a pic_info!')
        return info


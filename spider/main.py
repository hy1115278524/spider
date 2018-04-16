#!/usr/bin/env python
# encoding: utf-8
# Author: Feniox

import requests
import json
from lxml import etree
from pymongo import MongoClient
from datetime import datetime


class Modules:
    '''存储类'''
    def __init__(self, img_id):
        '''初始化Modules的信息'''
        self.img_id = img_id
        self.client = MongoClient()
        self.db = self.clietn.picdb
        self.collection = self.db.response

    def save(self, img_format, pic):
        '''先记录文档信息，再将图片保存在文件夹中.'''

        pic_info = {'img_id':self.img_id,
                    'img_format':img_format
                      }
        self.collection.insert_one(pic_info)
        pic_filename = './pic/' + self.img_id
        with open(pic_filename, 'wb') as f:
            pic_cont = pic.content
            f.write(pic_cont)


    def find_pic(self, img_id):
        '''将以保存的文档的信息提供给用户.'''
        res = self.collection.find_one({'img_id'}, img_id)
        if res:
            return res
        else:
            return False

class Analyze:
    '''分析传输过来的网页'''
    img_id = 1
    def __init__(self, text, headers):
        self.text = text
        self.headers = headers
        self.modules = Modules(Analyze.img_id)

    def analyze(self, text):
        selector = etree.HTML(text)
        img_box = selector.xpath("//*[@id='base_index']/div[3]/div[5]/div/div[3]/[@class='img']")
        for img in img_box:
            img_path = img.xpath('//img/@src')
            img_format = img_path.split('.')[-1]
            url = 'http://' + img_path
            res = requests.get(url, headers)
            self.modules.save(img_format, res)


class Fetch:
    '''提取网页内容交给下层分析'''
    def __init__(self, url):
        self.url = url
        self.headers = {'user-agent':'''Mozilla/5.0 (Windows NT 10.0; Win64; x64)
                         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'''
                        }
        self.analyze = Analyze(text, self.headers)

    def fetch(self):
        res = requests.get(url, headers=self.headers)
        res_text = res.text
        self.analyze.analyze(res_text)

class Spider:
    '''爬虫程序入口'''
    def __init__(self, spider_name, url):
        self.spider_name
        self.url = url
        self.fetch = Fetch(self.url)

    def run(self):
        self.fetch.fetch()





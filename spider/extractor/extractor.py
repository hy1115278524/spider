#!/usr/bin/env python
# encoding: utf-8
# Author: Feniox

from lxml import etree
from ..processor.processor import Processor

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./processor.log',
                    filemode='w')

class Extractor:
    '''提取信息类'''
    pic_id = 0
    def __init__(self):
        self.host = None
        self.text = None
        self.processor = Processor()

    def analyze(self, text, host):
        self.text = text
        self.host = host
        self.pic_info = {}
        self.pic = None
        Extractor.pic_id += 1
        selector = etree.HTML(text.text)
        '''根据host的不同执行不同的语句块.'''
        if host=='photo.poco.cn':
            img_box = selector.xpath("//*[@id='base_index']/div[3]/div[5]/div/div[3]/[@class='img']")
            for img in img_box:
                img_path = img.xpath('//img/@src')
                img_format = img_path.split('.')[-1]
                url = 'http://' + img_path
                pic = requests.get(url, headers)
                self.pic = pic.content
                self.pic_info['pic_id'] = Extractor.pic_id
                self.pic_info['img_path'] = img_path
                self.pic_info['img_format'] = img_format
                self.pass_info()
        elif host=='tuchong.com':
            pass
        elif host=='www.duitang.com':
            pass
        logging.info('成功解析webpage!')


    def pass_info(self):
        self.processor.process(self.pic_info, self.pic)#pic要通过前面的analyz


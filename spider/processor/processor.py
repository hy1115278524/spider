#!/usr/bin/env python
# encoding: utf-8
# Author: Feniox

from ..storage.storage import Modules

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./processor.log',
                    filemode='w')

class Processor:
    '''处理类'''
    def __init__(self):
        self.modules = Modules()

    def process(self, pic_info, pic):
        self.modules.insert(pic_info, pic)



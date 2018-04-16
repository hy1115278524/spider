#!/usr/bin/env python
# encoding: utf-8
# Author: Feniox

from ..downloader.downloader import Downloader

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./scheduler.log',
                    filemode='w')

class Scheduler:
    '''调度器'''
    def __init__(self):
        self.downloader = Downloader()

    def start(self, url):
        self.downloader.download(url)
        logging.info('开始下载网页!')

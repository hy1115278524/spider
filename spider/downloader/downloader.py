#!/usr/bin/env python
# encoding: utf-8
# Author: Feniox

import requests
from ..extractor.extractor import Extractor

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='./downloader.log',
                    filemode='w')

class Downloader:
    '''下载器'''
    def __init__(self):
        self.headers = {'user-agent':'''Mozilla/5.0 (Windows NT 10.0; Win64; x64)
                         AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'''
                        }
        self.extractor = Extractor()
        self.text = None
        self.host = None

    def download(self, url):
        self.url = url
        self.host = self.url.split('/')[0].split('//')[1]
        self.text = requests.get(url, headers)
        self.pass_info()
        logging.info('downloaded a webpage!')

    def pass_info(self):
        self.extractor.analyze(self.text, self.host)



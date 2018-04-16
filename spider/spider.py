#!/usr/bin/env python
# encoding: utf-8
# Author: Feniox

import sys
from scheduler.scheduler import Scheduler

print(sys.path)
class Spider:
    def __init__(self):
        self.scheduler = Scheduler()

    def run(self, url):
        self.scheduler.start(url)

if __name__ == '__main__':
    spider = Spider()
    spider.run('http://photo.poco.cn/')

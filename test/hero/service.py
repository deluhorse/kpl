# -*- coding:utf-8 -*-

"""
@author: delu
@file: service.py
@time: 2020-04-01 18:45
"""
from test.tester import Tester


class MyTest(Tester):
    def query_hero_list(self):
        # 退款成功
        self.path = 'hero.service'
        self.method = 'query_hero_list'
        self.params = {}


if __name__ == '__main__':
    refund = MyTest()
    refund.run('query_hero_list')

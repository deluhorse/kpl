# -*- coding:utf-8 -*-

"""
@author: delu
@file: query.py
@time: 2020-04-01 12:56
"""

from base.base import Base
import tornado.gen


class Controller(Base):

    @tornado.gen.coroutine
    def get(self):
        params = self.params()
        res = yield self.do_service('hero.service', 'query_hero_list', params=params)
        self.out(res)

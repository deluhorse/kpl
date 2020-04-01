# -*- coding:utf-8 -*-

"""
@author: delu
@file: query.py
@time: 2020-04-01 14:19
"""

from base.base import Base
import tornado.gen


class Controller(Base):
    auth = (('seller',), False)

    @tornado.gen.coroutine
    def post(self):
        params = self.params()
        params['shop_id'] = self.user_data['shop_id']
        res = yield self.do_service('buyer.service', 'update_buyer', params=params)
        self.out(res)
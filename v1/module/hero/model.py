# -*- coding:utf-8 -*-

"""
@author: delu
@file: model.py
@time: 2020-04-01 18:32
"""

from source.async_model import AsyncModelBase
import tornado.gen


class Model(AsyncModelBase):
    @tornado.gen.coroutine
    def query_hero_list(self, params):
        """
        查询英雄列表
        :param params:
        :return:
        """
        condition = ' 1=1 '

        value_list = []

        result = yield self.find(
            'heros',
            {
                self.sql_constants.CONDITION: condition
            },
            tuple(value_list),
            self.sql_constants.LIST
        )

        raise self._gr(result)

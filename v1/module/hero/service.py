# -*- coding:utf-8 -*-

"""
@author: delu
@file: service.py
@time: 2020-04-01 12:57
"""
import tornado.gen
from base.service import ServiceBase


class Service(ServiceBase):
    """
    service
    """
    model = None

    def __init__(self):
        """
        对象初始化方法
        添加你需要使用的model
        格式 项目model文件夹下的文件名或者 包名1.包名2.文件名 (无.py后缀)
        """
        self.model = self.import_model('hero.model')

    @tornado.gen.coroutine
    def query_hero_list(self, params):
        """
        查询英雄基本信息
        :param params: 
        :return: 
        """
        if self.common_utils.is_empty([], params):
            raise self._gre('PARAMS_NOT_EXIST')

        hero_list = yield self.model.query_hero_list(params)

        if not hero_list:
            raise self._gre('HERO_NOT_FOUND')

        raise self._grs(hero_list)

    @tornado.gen.coroutine
    def query_hero_detail(self, params):
        """
        查询英雄详情
        :param params:
        :return:
        """
        pass

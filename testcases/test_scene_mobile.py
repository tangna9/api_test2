#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/19 9:47
# @Author  : Tang Na
# @Site    : 
# @File    : test_scene_mobile.py
# @Software: PyCharm Community Edition

import unittest
from lib import base_func, data_parse, comm
from lib.data_parse import *
from lib.excl_operation import ExcelOperation
from ddt import data, ddt
from conf import para, constant_para
import sys
import json
import random
import time, datetime

testc = ExcelOperation("test_api")
headers = testc.get_headers(flag=2, row_n=1)

class MyTestCaseSceneMobile(unittest.TestCase):

    def setUp(self):
        log.debug("手机场景")
        log.debug("*testcase*%s" % sys._getframe().f_code.co_name)
        log.debug("用户开始录制")
        mobilephone_start_url = data_parse.r_url(url=para.tag["mobilephone_start"]["url"], tag="mobilephone_start")
        mobilephone_start_data = testc.get_data_config(tag="mobilephone_start")
        base_func.post_https(url=mobilephone_start_url, data=mobilephone_start_data, headers=headers)

    def tearDown(self):
        log.debug("*testcase*%s" %sys._getframe().f_code.co_name)
        log.debug("用户结束录制")
        mobilephone_end_url = data_parse.r_url(url=para.tag["mobilephone_end"]["url"], tag="mobilephone_end")
        mobilephone_end_data = testc.get_data_config(tag="mobilephone_end")
        base_func.post_https(url=mobilephone_end_url, data=mobilephone_end_data, headers=headers)


    def test_show_broadcaster_ad(self):
        log.debug("*testcase*%s" % sys._getframe().f_code.co_name)
        log.debug("用户获取特效列表分组")
        group_url = data_parse.r_url(url=para.tag["group"]["url"], tag="group")
        group_data = testc.get_data_config(tag="group")
        h, c, re = base_func.post_https(url=group_url, data=group_data, headers=headers)
        log.debug("用户获取特效列表")
        materials_url = data_parse.r_url(url=para.tag["materials"]["url"], tag="materials")
        constant_para.group_id = "SE_LIST"
        materials_data = testc.get_data_config(tag="materials")
        h, c, re = base_func.post_https(url=materials_url, data=materials_data, headers=headers)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCaseSceneMobile)
    unittest.TextTestRunner(verbosity=2).run(suite)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/19 10:19
# @Author  : Tang Na
# @Site    : 
# @File    : test_scene_short_vedio.py
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

class MyTestCaseSceneShortVedio(unittest.TestCase):

    def setUp(self):
        log.debug("短视频场景")

    def tearDown(self):
        pass

    def test_show_broadcaster_ad(self):
        log.debug("*testcase*%s" % sys._getframe().f_code.co_name)
        log.debug("用户视频数据上报")
        smallvideo_publish_url = data_parse.r_url(url=para.tag["smallvideo_publish"]["url"], tag="smallvideo_publish")
        smallvideo_publish_data = testc.get_data_config(tag="smallvideo_publish")
        h, c, re = base_func.post_https(url=smallvideo_publish_url, data=smallvideo_publish_data, headers=headers)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCaseSceneShortVedio)
    unittest.TextTestRunner(verbosity=2).run(suite)
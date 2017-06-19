#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/14 19:48
# @Author  : Tang Na
# @Site    :
# @File    : tt.py
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

testc = ExcelOperation("test_api")
rown = testc.get_cases_row()
test_line = [i for i in range(1, rown)]
print "test_line", test_line
headers = testc.get_headers(flag=2, row_n=1)
@ddt
class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def tearDown(self):
        pass

    @data(*test_line)
    def test_api_200(self, row_n):
        print "row_n", row_n
        log.debug("row_n%s" % row_n)
        tag = testc.get_tag(row_n)
        url = data_parse.r_url(tag=tag, url=testc.get_url(tag=tag, row_n=row_n))

        test_data = testc.get_test_data(row_n=row_n, tag=tag)
        expect_code = testc.get_expect_code(row_n=row_n)
        expect_mes = testc.get_expect_mes(row_n=row_n)
        h, c, re = base_func.post_https(url=url, data=test_data, headers=headers)
        self.assertEqual(c, expect_code)
        self.assertIn(expect_mes, re)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
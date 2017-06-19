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
import time, datetime

testc = ExcelOperation("test_api")
headers = testc.get_headers(flag=2, row_n=1)

class MyTestCaseSceneLive(unittest.TestCase):

    def setUp(self):
        log.debug("直播场景")
        log.debug("*testcase*%s" % sys._getframe().f_code.co_name)
        log.debug("主播信息上报")
        user_info_url = data_parse.r_url(url=para.tag["user_info"]["url"], tag="user_info")
        user_info_data = testc.get_data_config(tag="user_info")
        base_func.post_https(url=user_info_url, data=user_info_data, headers=headers)
        log.debug("粉丝信息上报")
        user_info_url = data_parse.r_url(url=para.tag["user_info"]["url"], tag="user_info")
        user_info_data = testc.get_data_config(tag="user_info")
        base_func.post_https(url=user_info_url, data=user_info_data, headers=headers)
        log.debug("主播开播")
        broadcaster_enter_url = data_parse.r_url(url=para.tag["broadcaster_enter"]["url"], tag="broadcaster_enter")
        broadcaster_enter_data = testc.get_data_config(tag="broadcaster_enter")
        base_func.post_https(url=broadcaster_enter_url, data=broadcaster_enter_data, headers=headers)
        log.debug("粉丝进入主播直播间")
        fans_enter_url = data_parse.r_url(url=para.tag["fans_enter"]["url"], tag="fans_enter")
        fans_enter_data = testc.get_data_config(tag="fans_enter")
        base_func.post_https(url=fans_enter_url, data=fans_enter_data, headers=headers)

    def tearDown(self):
        log.debug("*testcase*%s" %sys._getframe().f_code.co_name)
        log.debug("主播退播")

        broadcaster_quit_url = data_parse.r_url(url=para.tag["broadcaster_quit"]["url"], tag="broadcaster_quit")
        broadcaster_quit_data = testc.get_data_config(tag="broadcaster_quit")
        base_func.post_https(url=broadcaster_quit_url, data=broadcaster_quit_data, headers=headers)
        log.debug("粉丝退播")
        fans_quit_url = data_parse.r_url(url=para.tag["fans_quit"]["url"], tag="fans_quit")
        fans_quit_data = testc.get_data_config(tag="fans_quit")
        base_func.post_https(url=fans_quit_url, data=fans_quit_data, headers=headers)


    def test_show_broadcaster_ad(self):
        log.debug("*testcase*%s" %sys._getframe().f_code.co_name)
        log.debug("主播获取广告列表")
        materials_url = data_parse.r_url(url=para.tag["materials"]["url"],tag="materials")
        materials_data = testc.get_data_config(tag="materials")
        h, c, re = base_func.post_https(url=materials_url, data=materials_data, headers=headers)
        grabable = []
        infos = json.loads(re)["data"]
        current_time_ms = int(round(time.time()*1000))
        for ad in json.loads(infos):
            for i in ad["ads"]:
                if i["grab_status"] == 1 and current_time_ms >= i["start_time"]:
                    grabable.append(i["advertisement_id"])
        if grabable:
            print "grabable", grabable
            grab_url = data_parse.r_url(url=para.tag["grab"]["url"],tag="grab")
            constant_para.advertisement_id = random.choice(grabable)
            grab_data = testc.get_data_config(tag="grab")
            base_func.post_https(url=grab_url, data=grab_data, headers=headers)
        else:
            raise Exception("no grabable ads, please prepare ad first!")
        log.debug("主播检查广告状态")
        check_url = data_parse.r_url(url=para.tag["check"]["url"],tag="check")
        check_data = testc.get_data_config(tag="check")
        base_func.post_https(url=check_url, data=check_data, headers=headers)
        log.debug("主播启用广告")
        action_url = data_parse.r_url(url=para.tag["action"]["url"],tag="action")
        action_data = testc.get_data_config(tag="action")
        base_func.post_https(url=action_url, data=action_data, headers=headers)
        log.debug("粉丝端获取广告信息")
        fansad_url = data_parse.r_url(url=para.tag["fans_ad"]["url"], tag="fans_ad")
        fansad_data = testc.get_data_config(tag="fans_ad")
        base_func.post_https(url=fansad_url, data=fansad_data, headers=headers)
        log.debug("粉丝端展示广告")
        fans_ad_show_url = data_parse.r_url(url=para.tag["fans_ad_show"]["url"], tag="fans_ad_show")
        fans_ad_show_data = testc.get_data_config(tag="fans_ad_show")
        base_func.post_https(url=fans_ad_show_url, data=fans_ad_show_data, headers=headers)

        log.debug("主播展示广告结束")
        constant_para.action_type = 2
        action_data2 = testc.get_data_config(tag="action")
        base_func.post_https(url=action_url, data=action_data2, headers=headers)
        log.debug("广告任务完成上报")
        complete_url = data_parse.r_url(url=para.tag["complete"]["url"], tag="complete")
        complete_data = testc.get_data_config(tag="complete")
        base_func.post_https(url=complete_url, data=complete_data, headers=headers)

    def test_show_se(self):
        log.debug("*testcase*%s" % sys._getframe().f_code.co_name)
        log.debug("主播获取特效列表")
        materials_url = data_parse.r_url(url=para.tag["materials"]["url"], tag="materials")
        constant_para.group_id = "SE_LIST"
        materials_data = testc.get_data_config(tag="materials")
        h, c, re = base_func.post_https(url=materials_url, data=materials_data, headers=headers)
        infos = json.loads(re)["data"]
        se_list = []
        for se in json.loads(infos):
            se_list.append(se["advertisement_id"])
        if se_list:
            log.debug("展示特效开始")
            action_url = data_parse.r_url(url=para.tag["action"]["url"], tag="action")
            constant_para.advertisement_id = random.choice(se_list)
            action_data = testc.get_data_config(tag="action")
            base_func.post_https(url=action_url, data=action_data, headers=headers)
            log.debug("主播展示特效结束")
            constant_para.action_type = 2
            action_data2 = testc.get_data_config(tag="action")
            base_func.post_https(url=action_url, data=action_data2, headers=headers)
        else:
            raise Exception("no se, please prepare data!")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCaseSceneLive)
    unittest.TextTestRunner(verbosity=2).run(suite)
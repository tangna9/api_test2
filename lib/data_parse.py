#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/13 11:38
# @Author  : Tang Na
# @Site    : 
# @File    : data_parse.py
# @Software: PyCharm Community Edition
import json
from lib.confparser import cf
import base64
import logging
from logging.config import fileConfig
fileConfig("../conf/logging.conf")
log = logging.getLogger("api")

def parse_test_data(test_data1, test_data2=""):

    # test_data1 = '"test_data app_id=0001",\n\'timestamp\'=1231231112，'
    # test_data2 = 'data={"user_id":"YZB0001","uuid":"23213123sdfsdsd89s8d8s"}'

    # if '"' or "'" in test_data1:
    #     test_data1 = test_data1.replace("'", '')
    #     test_data1 = test_data1.replace('"', '')
    if test_data1:
        test_data1 = test_data1.split("\n")
        test_dic = {}
        for i in test_data1:
            i = i.split("=")
            #print i
            test_dic[i[0]] = i[1]
    else:
        raise Exception("test_data1 is empty!")
    if test_data2:
        v = json.loads(test_data2)
        test_dic["data"] = v
    # print test_dic
    log.debug("test_data from excel parsed: %s" %test_dic)
    return test_dic

def r_url(url, tag=""):
    if tag in ["logreport"]:
        ip = cf().get("host","IP2")
    else:
        ip = cf().get("host", "IP1")
    url = "https://" + ip + url
    return url

def base64decode(str):
    lens = len(str)
    lenx = lens - (lens % 4 if lens % 4 else 4)
    try:
        result = base64.decodestring(str[:lenx])
    except:
        pass
    log.debug("base64 decoded:%s (original str:%s)" %(result, str))
    return result
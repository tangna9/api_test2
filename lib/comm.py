#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/15 10:17
# @Author  : Tang Na
# @Site    :
# @File    : base_func.py
# @Software: PyCharm Community Edition

from lib.base_func import *
from conf import para
from lib.data_parse import *
import json

fileConfig("../conf/logging.conf")
log = logging.getLogger("api")

host = cf().get("host", "IP1")
h = para.headers1

def get_sign(r_data, flag=1):
    '''
    :param app_id:
    :param sdk_v:
    :param flag: 1鉴权sign 2datasign
    :return: sign
    '''
    if flag == 1:
        url = cf().get("url", "SIGN1")
    else:
        url = cf().get("url", "SIGN2")
    url = r_url(url)
    header, code, re = post_https(url=url, data=r_data, headers=h)
    return re

def crypt(flag, app_id, data):
    '''
    :param flag: 1加密 2解密
    :param app_id:
    :param data:
    :return:
    '''

    r_data = {}
    r_data["app_id"] = app_id
    r_data["data"] = data
    if flag == 1:
        url = cf().get("url", "ENCRYPT")
        r_data["data"] = json.dumps(data)
    else:
        url = cf().get("url", "DECRYPT")
    url = "http://" + host + url
    code, re = post_http(url=url, data=r_data, headers=h)
    return re

def get_Authorization(r_data, url=cf().get("url","AUTH"), header=h, flag=0):
    if "http" not in url:
        url = r_url(url)
    h, c, text = post_https(url=url, data=r_data, headers=header)
    #print "$$$$", h["Authorization"]
    if flag:
        return h["Authorization"]
    #print "***", h["Authorization"]
    return h["Authorization"].split(".")


if __name__ == "__main__":
    data = {
        "app_id":"c1b2c2ade01a4b4a80808f8e0e55f96f",
    "time_s":"1497334747",
    "sdk":"250"}
    print get_sign(r_data=data, flag=2)

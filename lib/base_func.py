#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/15 10:17
# @Author  : Tang Na
# @Site    : 
# @File    : base_func.py
# @Software: PyCharm Community Edition

import requests
from conf import para
from lib.data_parse import *
__all__ = ['post_https', 'post_http']

#host = cf().get("host", "IP")
h = para.headers1
def post_https(url, data, headers=h):
    '''
    :param url: 请求url
    :param data: 请求数据
    :param headers: 请求headers
    :return:
    '''
    s = requests.Session()
    r = s.post(url=url, data=data, headers=headers, verify=False)
    log.debug("request:%s" %url)
    log.debug("request_header:%s" % headers)
    log.debug("request_data:%s" %data)
    log.debug("response_headers:%s" %r.headers)
    log.debug("response:(code:%s)(mess:%s)" %(r.status_code, r.text))
    #print "***", r.headers
    return r.headers, r.status_code, r.text

def post_http(url, data, headers=h):
    '''
    :param url: 请求url
    :param data: 请求数据
    :param headers: 请求headers
    :return:
    '''
    r = requests.post(url=url, data=data, headers=headers)
    log.debug("request:%s" % url)
    log.debug("request_data:%s" %data)
    log.debug("response:(code:%s)(mess:%s)" % (r.status_code, r.text))
    return r.status_code, r.text
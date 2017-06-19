#!/usr/bin/env python
#encoding:utf8
import ConfigParser
__all__ = ['cf']

def cf():
    '''

    :return: 返回解析后的配置文件
    '''

    cf = ConfigParser.ConfigParser()
    cf.read(["../conf/url.conf"])
    return cf
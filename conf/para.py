#!/usr/bin/env python
#encoding:utf8

import datetime
import time
import data_para

headers1 = {"content-type": "application/x-www-form-urlencoded"}
headers2 = {"content-type":"application/x-www-form-urlencoded","Authorization":""}
current_time = str(int(time.mktime(datetime.datetime.now().timetuple())))
#timest = "1497334747"
APPid = "0f5ac712774e4594ab43a6365c872e2c"
SDK_V = "250"

BASE_PARA = {
    "app_id": APPid,
    "timestamp": current_time,
    "sdk_version": SDK_V,
    "sign":""
}
authorize = {
    "url": "/sensear/v2/sdk/authorize/",
    "base_para": BASE_PARA,
}
prelist = {
    "url": "/sensear/v2/materials/prelist/",
    "base_para": BASE_PARA,
    "data":data_para.prelist
}
materials = {
    "url": "/sensear/v2/materials/list",
    "base_para": BASE_PARA,
    "data": data_para.materials
}

group = {
    "url": "/sensear/v2/group/list/",
    "base_para": BASE_PARA,
}

logreport ={
    "url":"/sensear/logreport",
    "base_para": BASE_PARA,
    "data": data_para.logreport
}

material = {
    "url":"/sensear/v2/material",
    "base_para": BASE_PARA,
    "data": data_para.material
}
user_info ={
    "url": "/sensear/v2/userinfo/",
    "base_para": BASE_PARA,
    "data": data_para.user_info
}

grab = {
    "url": "/sensear/v2/ad/grab",
    "base_para": BASE_PARA,
    "data": data_para.grab
}
history ={
    "url": "/sensear/v2/ad/history",
    "base_para": BASE_PARA,
    "data": data_para.history
}

complete = {
    "url": "/sensear/v2/ad/complete",
    "base_para": BASE_PARA,
    "data": data_para.complete
}

check ={
    "url": "/sensear/v2/ad/check",
    "base_para": BASE_PARA,
    "data": data_para.check
}

action ={
    "url": "/sensear/v2/ad/action",
    "base_para": BASE_PARA,
    "data": data_para.action
}

configdata = {
    "url": "/sensear/v2/sdk/configdata",
    "base_para": BASE_PARA
}
broadcaster_enter = {
    "url": "/sensear/v2/broadcaster/enter",
    "base_para": BASE_PARA,
    "data": data_para.broadcaster_enter
}

broadcaster_quit = {
    "url": "/sensear/v2/broadcaster/quit",
    "base_para": BASE_PARA,
    "data": data_para.broadcaster_quit
}

supportad = {
    "url": "/sensear/v2/broadcaster/supportad",
    "base_para": BASE_PARA,
    "data": data_para.supportad
}

fans_enter ={
    "url": "/sensear/v2/fans/enter",
    "base_para": BASE_PARA,
    "data": data_para.fans_enter
}


fans_ad ={
    "url": "/sensear/v2/fans/ad",
    "base_para": BASE_PARA,
    "data": data_para.fans_ad
}
fans_ad_show ={
    "url": "/sensear/v2/fans/ad/show",
    "base_para": BASE_PARA,
    "data": data_para.fans_ad_show
}
fans_quit ={
    "url": "/sensear/v2/fans/quit",
    "base_para": BASE_PARA,
    "data": data_para.fans_quit
}
smallvideo_publish ={
    "url": "/sensear/v2/smallvideo/publish",
    "base_para": BASE_PARA,
    "data": data_para.smallvideo_publish
}
mobilephone_start ={
    "url": "/sensear/v2/mobilephone/start",
    "base_para": BASE_PARA,
    "data": data_para.mobilephone_start
}
mobilephone_end ={
    "url": "/sensear/v2/mobilephone/end",
    "base_para": BASE_PARA,
    "data": data_para.mobilephone_end
}


tag = {"authorize":authorize, "prelist":prelist,"materials": materials,
       "group":group, "logreport":logreport, "material":material, "user_info":user_info,
       "grab": grab, "history":history, "complete":complete, "logreport":logreport,
        "check": check, "action":action, "configdata":configdata,"broadcaster_enter":broadcaster_enter,
        "broadcaster_quit":broadcaster_quit,"supportad":supportad, "fans_enter":fans_enter,
        "fans_ad": fans_ad, "fans_ad_show":fans_ad_show, "fans_quit":fans_quit,
        "smallvideo_publish": smallvideo_publish, "mobilephone_start":mobilephone_start,
        "mobilephone_end":mobilephone_end}

excel_map = {"NO": 0, "TEST_DESCRIP": 1, "TAG":2, "URL": 3, "HEADERS":4,
             "TESTDATA":5, "EXPECTCODE":6, "EXPECTMESS":7}

MATERIAL_LIST_PARA = {"broadcaster_id": "SenseTime001", "group_id": "AD_LIST", "support_ad_modes":"31"}


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/6/15 9:52
# @Author  : Tang Na
# @Site    : 
# @File    : data_para.py
# @Software: PyCharm Community Edition
from constant_para import *

prelist = {"data":{"user_id":user_id}}

materials = {"data":{
    "broadcaster_id":broadcaster_id,
    "group_id":group_id,
    "support_ad_modes":"31,32"
}}

logreport = {"data":
    [{"id":log_report_id,
      "timestamp": log_report_time,
        "data":{"url":log_report_url,
                "time":log_report_time}
    }]
}

material ={"data":{
"user_id":user_id,
"advertisement_id":advertisement_id
}}

grab = {"data":{
"user_id":user_id,
"advertisement_id":advertisement_id
}}

complete = {"data":{
"user_id":user_id,
"advertisement_id":advertisement_id
}}

check = {"data":{
"user_id":user_id,
"advertisement_id":advertisement_id
}}

user_info = {"data":{
    "user_id": user_id,
    "uuid": uuid,
    "user_name": user_name,
    "birthday": birthday,
    "gender":gender,
    "address":address,
    "latitude":latitude,
    "longitude":longitude,
    "follow_count":follow_count,
    "fans_count":fans_count,
    "tags":tags,
    "imei":imei,
    "imei_md5":imei_md5,
    "device_id":device_id,
    "device_id_md5":device_id_md5,
    "os_version":os_version,
    "model":model,
    "network_type":network_type,
    "channel":channel
}}

history = {"data":{
"user_id":user_id,
"cur_page":cur_page,
"page_size":page_size
}}

action = {"data":{ "user_id":user_id,
            "advertisement_id":advertisement_id,
            "type": action_type,
            "audience_count":audience_count,
            "request_id":request_id,
            "triggers":[
                {"trigger_action":trigger_action,
                "start_time":act_start_time,
                "end_time":act_end_time,
            }],
            "display_time":act_display_time,
            "display_frames":display_frames
}}

broadcaster_enter = {"data":{"broadcaster_id":broadcaster_id,
        "last_broadcast_seconds":last_broadcast_seconds,
        "video_url":video_url
}}

broadcaster_quit = {"data": { "broadcaster_id":broadcaster_id,
        "current_audience_count":current_audience_count
}}

supportad ={"data":{
"broadcaster_id":broadcaster_id
}}

fans_enter ={"data":{"fans_id":fans_id,
 "broadcaster_id":broadcaster_id
}}

fans_ad = {"data":{"fans_id":fans_id,
"broadcaster_id":broadcaster_id}}

fans_ad_show = {"data":{"fans_id":fans_id,
"broadcaster_id":broadcaster_id,
"advertisement_id":advertisement_id,
"display_time":display_time
}}

fans_quit = {"data":{"fans_id":fans_id,
"broadcaster_id":broadcaster_id,
"stay_time":140231}}

smallvideo_publish = {"data":{"user_id":user_id,
    "video_id": video_id,
    "video_link":"http://...",
    "advertisment_infos":[
        {"advertisment _id":advertisement_id,
            "start_time":start_time,
            "end_time":end_time,
            "triggers":[
        {"trigger_action":trigger_action,
            "start_time":start_time,
            "end_time":end_time,
 }]
    }]
}}
mobilephone_start = {"data":{"user_id":user_id}}
mobilephone_end = {"data":{"user_id":user_id,
                    "video_id":video_id,
                     "video_link":video_link}}

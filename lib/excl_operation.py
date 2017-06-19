#!/usr/bin/env python
#encoding:utf8

import xlrd
from lib import confparser, comm
import logging
from logging.config import fileConfig
import json
from conf import para, constant_para
import copy
from lib.data_parse import parse_test_data, r_url

fileConfig("../conf/logging.conf")
log = logging.getLogger("api")
__all__ = ['ExcelOperation', 'get_raw_cases_data']
col = para.excel_map

def repalce_value(dict_a, key, value):
    if isinstance(dict_a, dict):
        for x in range(len(dict_a)):
            temp_key = dict_a.keys()[x]
            temp_value = dict_a[temp_key]
            if temp_key == key:
                dict_a[temp_key] = value
            repalce_value(temp_value, key, value)
    return dict_a

def repalce_value2(dict_a, change_list):
    if isinstance(dict_a, dict):
        for x in range(len(dict_a)):
            temp_key = dict_a.keys()[x]
            temp_value = dict_a[temp_key]
            for i in change_list:
                i = i.split("=")
                if temp_key == i[0]:
                    dict_a[temp_key] = i[1]
                repalce_value2(temp_value, change_list)
    return dict_a

class ExcelOperation(object):
    '''
    测试case的excel文件相应处理
    '''
    def __init__(self, sheet):

        try:
            file = confparser.cf().get("file", "TESTCASES")
            self.data = xlrd.open_workbook(file)
            self.table = self.data.sheet_by_name(sheet)
        except Exception, e:
            log.debug(str(e))

    def get_cases_row(self):
        nrow = self.table.nrows
        return nrow

    def get_url(self, tag, row_n):
        url = self.table.cell(row_n, col["URL"]).value
        if url:
            return url
        else:
            return para.tag[tag]["url"]

    def get_tag(self, row_n):
        return self.table.cell(row_n, col["TAG"]).value

    def get_headers(self, row_n=1, flag=1):
        header = self.table.cell(row_n, col["HEADERS"]).value
        if header:
            return json.loads(header)
        elif flag == 1:
            return para.headers1
        else:
            headers2 = para.headers2
            data = copy.deepcopy(para.BASE_PARA)
            data.pop("sign", None)
            print "1111", data
            a_sign = comm.get_sign(r_data=data)
            data["sign"] = a_sign
            print "2222", data
            log.debug("2222222%s" %data)
            au = comm.get_Authorization(r_data=data, flag=1)
            headers2["Authorization"] = au
            return headers2

    def get_test_data(self, tag, row_n=1):
        excel_data = self.table.cell(row_n, col["TESTDATA"]).value

        if tag in ["authorize", "group", "configdata"]:
            re_data = copy.deepcopy(para.BASE_PARA)
            re_data.pop("sign", None)
            if tag == "authorize":
                a_sign = comm.get_sign(r_data=re_data, flag=1)
                re_data["sign"] = a_sign
            elif tag in ["group", "configdata"]:
                a_sign = comm.get_sign(r_data=re_data, flag=2)
                re_data["sign"] = a_sign
            if not excel_data:
                return re_data
            else:
                change_list = excel_data.split("\n")
                #print "change_list1", change_list
                #print "re_data1", re_data
                re_data = repalce_value2(dict_a=re_data, change_list=change_list)
                return re_data
        else:
            data_dict1 = copy.deepcopy(para.tag[tag]["base_para"])
            data_dict = data_dict1.copy()
            data_dict2 = copy.deepcopy(para.tag[tag]["data"])
            print "data_dict2121212", data_dict2["data"]
            if not excel_data:
                cryped_dict2 = comm.crypt(flag=1, app_id=data_dict1["app_id"], data=data_dict2["data"])
                data_dict2["data"] = cryped_dict2

                data_dict.update(data_dict2)
                data_dict.pop("sign", None)
                d_sign = comm.get_sign(r_data=data_dict, flag=2)
                data_dict["sign"] = d_sign
                return data_dict
            else:
                data_dict.update(data_dict2)
                change_list = excel_data.split("\n")
                re_data = repalce_value2(dict_a=data_dict, change_list=change_list)
                print "data_dict['data']2121212", data_dict["data"]
                cryped_dict2 = comm.crypt(flag=1, app_id=data_dict["app_id"], data=data_dict["data"])
                data_dict["data"] = cryped_dict2
                if "sign" not in change_list:
                    data_dict.pop("sign", None)
                    d_sign = comm.get_sign(r_data=data_dict, flag=2)
                    data_dict["sign"] = d_sign
                return re_data

    def get_data_config(self, tag):
        if tag in ["authorize", "group", "configdata"]:
            c_re_data = copy.deepcopy(para.BASE_PARA)
            c_re_data.pop("sign", None)
            if tag == "authorize":
                a_sign = comm.get_sign(r_data=c_re_data, flag=1)
                c_re_data["sign"] = a_sign
            elif tag in ["group", "configdata"]:
                a_sign = comm.get_sign(r_data=c_re_data, flag=2)
                c_re_data["sign"] = a_sign
            return c_re_data
        else:
            c_data_dict1 = copy.deepcopy(para.tag[tag]["base_para"])
            c_data_dict = c_data_dict1.copy()
            print "11111", para.tag[tag]["data"]
            c_data_dict2 = copy.deepcopy(para.tag[tag]["data"])
            keys = c_data_dict2["data"].keys()
            if "advertisement_id" in keys or "type" in keys or "group_id" in keys:
                c_data_dict2["data"]["advertisement_id"] = constant_para.advertisement_id
                c_data_dict2["data"]["type"] = constant_para.action_type
                c_data_dict2["data"]["group_id"] = constant_para.group_id

            cryped_dict2 = comm.crypt(flag=1, app_id=c_data_dict1["app_id"], data=c_data_dict2["data"])
            c_data_dict2["data"] = cryped_dict2
            c_data_dict.update(c_data_dict2)
            c_data_dict.pop("sign", None)
            d_sign = comm.get_sign(r_data=c_data_dict, flag=2)
            c_data_dict["sign"] = d_sign
            return c_data_dict

    def get_expect_code(self, row_n):
        return self.table.cell(row_n, col["EXPECTCODE"]).value

    def get_expect_mes(self, row_n):
        return self.table.cell(row_n, col["EXPECTMESS"]).value


        #return json.loads(self.table.cell(row_n, col["TESTDATA"]).value)


if __name__ == "__main__":
    teste = ExcelOperation("2.5.1")
    #teste.get_single_wrong_para()
    teste.all_test_info()



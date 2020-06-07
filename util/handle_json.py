# coding:utf-8
import requests
import pytest
import sys
import os
import json
import configparser
sys.path.append('../')

class HandleJson:
    # 读取json文件
    def load_json(self, file_name):
        if file_name == None:
            file_path = ""
        else:
            file_path = file_name
        try:
            with open(file_path, encoding='UTF-8') as f:
                data = json.load(f)
            return data
        except Exception:
            print("未找到json文件")
            return {}

    # 读取json文件里具体的字段值
    def getJson_value(self, key, file_name):
        if file_name == None:
            return ""
        jsonData = self.load_json(file_name)
        if key == None:
            getJsonValue = ""
        else:
            getJsonValue = jsonData.get(key)
        return getJsonValue


handle_jsonData = HandleJson()
# if __name__ == "__main__":
#     hjson = HandleJson()
#     params = hjson.getJson_value(
#         "params", '/ApiTestProject/Apiautomation/test_data/getrequest.json')
#     print(params)
import sys
sys.path.append("D:/yiq/Demo")
from deepdiff import DeepDiff
import os

base_path = os.getcwd()  #当前路径
path = os.path.abspath(os.path.dirname(os.getcwd()))  #上级路径
from Util.get_json import get_value


def handle_result(url, code):
    data = get_value(url, "/Config/code_message.json")
    #data = get_value(url, "/Demo/Config/code_message.json")
    if data !=None:
        for i in data:
            message = i.get(str(code))
            if message:
                return message
    return None

def get_result_json(url,status):
    data = get_value(url, "/Config/result.json")
    #data = get_value(url, "\Config\result.json")
    if data !=None:
        for i in data:
            message = i.get(status)
            if message:
                return message
    return None

def handle_result_json(dict1,dict2):
    '''
    校验格式
    '''
    if isinstance(dict1, dict) and isinstance(dict2, dict):
        cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
        if cmp_dict.get("dictionary_item_added"):
            return False
        else:
            return True
    return False

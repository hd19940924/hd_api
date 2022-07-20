import sys
sys.path.append("D:/yiq/Demo")
import os

from Util.get_json import read_json
base_path = os.getcwd()  #当前路径
path = os.path.abspath(os.path.dirname(os.getcwd()))  #上级路径


def get_header():
    #data = read_json("/Config/header.json")
    data = read_json("/Config/header.json")
    return data

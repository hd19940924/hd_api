import json
import os
import unittest
import ddt
#from Base import HTMLTestRunner_PY3
import Base.HTMLTestRunner_PY3 as HTMLTestRunner_py3
from Util.get_condition import get_data
from Util.get_result import handle_result, get_result_json, handle_result_json
from Util.get_header import get_header
base_path = os.getcwd()  #当前路径
path = os.path.abspath(os.path.dirname(os.getcwd()))  #上级路径
from Util.get_excel import excel_data
from Base.base_request import base_request

data = excel_data.get_excel_data()
print(data)
@ddt.ddt
class TestRunCaseDdt(unittest.TestCase):
    @ddt.data(*data)
    def test_main_case(self, data):
       print(data)
if __name__ == '__main__':
    tt=TestRunCaseDdt()
    tt.test_main_case()
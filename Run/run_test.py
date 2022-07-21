import json
import os
import unittest
import ddt
from ddt import ddt, data
#from Base import HTMLTestRunner_PY3
import Base.HTMLTestRunner_PY3 as HTMLTestRunner_py3
from Util.get_condition import get_data
from Util.get_result import handle_result, get_result_json, handle_result_json
from Util.get_header import get_header
base_path = os.getcwd()  #当前路径
path = os.path.abspath(os.path.dirname(os.getcwd()))  #上级路径
print(path)
from Util.get_excel import GetExcel#excel_data
excel_data = GetExcel()
from Base.base_request import base_request
from BeautifulReport import BeautifulReport
data1 = excel_data.get_excel_data()
import paramunittest
@ddt
class TestRunCase(unittest.TestCase):
    def setUp(self):
        print("======开始执行测试用例======")

    def tearDown(self):
        print("======测试用例执行完毕======")
    @data(*data1)
    def test_main_case1(self, data2):
               method = data2[6]
               url = data2[5]
               data = data2[7]
               header=get_header()
               res = base_request.run_main(method, url, data, header).json()
               self.assertEqual(res["code"], 1)
               #print(data2)
if __name__ == '__main__':
     unittest.main()

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
print(path)
from Util.get_excel import excel_data
from Base.base_request import base_request
from BeautifulReport import BeautifulReport
data = excel_data.get_excel_data()
#print(data)
@ddt.ddt
class TestRunCaseDdt(unittest.TestCase):
    @ddt.data(*data)
    def test_main_case(self, data):
       print(data)
       header = None
       # data = excel_data.get_rows_value(i + 2)   #使用ddt，就不需要获取这个data了
       is_run = data[2]  # 是否执行
       case_id = data[7]  # 获取case_id编辑
       line_num = excel_data.get_row_number(case_id)  # 通过case_id 获取行号；结果回写的时候就需要这个
       print(is_run)
       print(case_id)
if __name__ == '__main__':
    #tt=TestRunCaseDdt()
   # tt.test_main_case()
    case_path = path + "/hd_api/Run"
    report_path = path + "/hd_api/Report/report2.html"
    discover = unittest.defaultTestLoader.discover("C:/Users/admin/PycharmProjects/hd_api/Run", pattern="run_case_test.py")
    #test_suite = unittest.defaultTestLoader.discover('E:\pythonJIAO\test1\jiekou\scripts', pattern='jieko*.py')
    result = BeautifulReport(discover)
    result.report(filename='测试报告', description='自动化测试报告', report_dir= "C:/Users/admin/PycharmProjects/hd_api/report",
                  theme='theme_default')
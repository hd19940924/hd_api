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
class TestRunCase(unittest.TestCase):
    @ddt.data(*data)
    def test_main_case1(self, data):
       res=None
       #print(data)
       header = None
       # data = excel_data.get_rows_value(i + 2)   #使用ddt，就不需要获取这个data了
       is_run = data[2]  # 是否执行
       case_id = data[7]  # 获取case_id编辑
       line_num = excel_data.get_row_number(case_id)  # 通过case_id 获取行号；结果回写的时候就需要这个
       """if is_run == 'yes':
           #print(is_run)
           #print(data[3])
           method = data[6]
           url = data[5]
           is_header = data[9]
           excepect_method = data[10]
           excepect_result = data[11]
           data1 = data[7]
           condition = data[3]
           if is_header == 'yes':
               header = get_header()
           res = base_request.run_main(method, url, data1, header).json()
           self.assertEqual(res["code"],1)"""
       if is_run == 'yes':
           data1 = data[7]
           # data1 = json.loads(data[7])  #将data数据转成dict格式
           is_depend = data[3]
           # 获取依赖数据
           if is_depend:  # 如果有依赖数据
               depend_key = data[4]  # 依赖的值
               depend_data = get_data(is_depend)  # 依赖数据：将前置条件赋值给依赖数据
               depend_data = depend_data[0]  # 最终依赖的数据
                   # data1[depend_key] = depend_data    #这个主要目前也是提取，但是目前报错，待处理。
               method = data[6]
               url = data[5]
               is_header = data[9]
               excepect_method = data[10]
               excepect_result = data[11]
               condition = data[3]
               if condition:
                   pass
               if is_header == 'yes':
                   header = get_header()
               res = base_request.run_main(method, url, data1, header).json()
               self.assertEqual(res["code"], 1)
if __name__ == '__main__':
     unittest.main()

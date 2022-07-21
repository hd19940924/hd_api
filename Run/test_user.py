import json
import unittest
import os
import ddt
from Util.excel_handler import ExcelHandler
from Util import dir_config
from Base.base_request import base_request
from Util.get_header import get_header

# 读取测试数据
data1 = ExcelHandler(os.path.join(dir_config.testcases_dir,"testcase.xlsx")).read_key_value("case")

@ddt.ddt
class Test_Verify_Code(unittest.TestCase):

    def setUp(self) -> None:
        print("======开始执行测试用例======")

    def tearDown(self) -> None:
        print("======执行测试用例结束======")

    @ddt.data(*data1)
    def test_verify_phone(self,data2):
        method = data2["method"]
        url = data2["url"]
        data = data2["data"]
        header = get_header()
        is_run=data2["是否执行"]
        is_header=data2["header操作"]
        if is_run == 'yes':
            if is_header == 'yes':
                header = get_header()
            res = base_request.run_main(method, url, data, header).json()
            self.assertEqual(res["code"], 1)
       # print(data2["是否执行"])



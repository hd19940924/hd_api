#coding:utf-8
import ddt
import unittest

testdata = [{"username":"wangm","password":1234567},
            {"username":"WXK","password":1234567},
            {"username":"Wyyy","password":1234567},
            {"username":"WANGMIN","password":1234567}]

@ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        print("开始")

    def tearDown(self):
        print("结束")

    @ddt.data(*testdata)
    def test_ddt(self,data):
        print(data)


if __name__ =="__main__":
    unittest.main()

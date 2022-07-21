#from case.chandaologin2 import login
#from HTMLyy.HTMLYY import HTMLTestRunner
from Run.run_test import TestRunCase
from Base import HTMLTestRunner_PY3
import unittest
from Base import HTMLTestRunner
from Base.HTMLYY import HTMLTestRunner
from Run.test_user import Test_Verify_Code
import time
if __name__ == '__main__':
    suite =unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test_Verify_Code))
    #suite.addTests(TestUserLogin("test_01case"))
    #suite.addTests(tests)
    a =time.strftime("%Y-%m-%d %H_%M_%S")
    #fp="//report/(a+"result.html")
    #fp='./report/' + a + '_result.html'
    fp="C:/Users/admin/PycharmProjects/hd_api/Report/"+a+'_result.html'
    with open(fp, 'w',encoding="utf-8",errors='ignore') as f:
               runner = HTMLTestRunner(stream=f,
                                title='测试报告',
                                description='测试用例的执行情况',
                                verbosity=2,

                                )
               runner.run(suite)
import os

#框架项目顶层目录的绝对路径
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]


# 测试数据路径
testdatas_dir =  os.path.join(base_dir,"test_datas")


# 测试用例路径
testcases_dir =  os.path.join(base_dir,"case")


# 测试报告路径
htmlreport_dir =  os.path.join(base_dir,"reports")
print(testcases_dir)
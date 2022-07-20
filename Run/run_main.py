import sys
sys.path.append(r"C:\Users\admin\Desktop\yiq_api_demo-master")
import json
import os
from Util.get_condition import get_data
from Util.get_result import handle_result, get_result_json, handle_result_json
from Util.get_header import get_header
base_path = os.getcwd()  #当前路径
path = os.path.abspath(os.path.dirname(os.getcwd()))  #上级路径
from Util.get_excel import excel_data
from Base.base_request import base_request



class RunMain:
    def run_main(self):
        rows = excel_data.get_rows()
        for i in range(rows):
            header = None
            data = excel_data.get_rows_value(i+2)
            is_run = data[2] #是否执行
            if is_run == 'yes':
                data1 = data[7]
                print("data1类型：", type(data1), data1)
                # data1 = json.loads(data[7])  #将data数据转成dict格式
                # print("data1类型：", type(data1), data1)
                depend_key=data[4]                         #依赖的值
                print("依赖的值为：",depend_key)
                is_depend = data[3]
                #获取依赖数据
                if is_depend:   #如果有依赖数据
                    depend_key = data[4]
                    depend_data = get_data(is_depend)   #依赖数据：将前置条件赋值给依赖数据
                    print("依赖的数据集为：", depend_data)
                    depend_data = depend_data[0]    #最终依赖的数据
                    print("最终提取处理依赖的数据为：", depend_data)

                    #data1[depend_key] = depend_data    #将提取出来的数据depend_data；赋值为依赖数据，进行替换；大致就是将参数进行替换；
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
                code = res['code']
                message = res['msg']
                if excepect_method == "mec":    #mec表示:用例里面的预期结果方式为message+code
                    config_message = handle_result(url, code)
                    if message == config_message:
                        excel_data.write_excel_data(i+2, 13, "通过")
                        excel_data.write_excel_data(i+2, 14, json.dumps(res, ensure_ascii=False))

                    else:
                        excel_data.write_excel_data(i+2, 13, "失败")
                        excel_data.write_excel_data(i+2, 14, json.dumps(res, ensure_ascii=False))

                if excepect_method == "code":   #code表示：用例里面的预期结果方式为code
                    if excepect_result == code:
                        excel_data.write_excel_data(i+2, 13, "通过")
                        excel_data.write_excel_data(i+2, 14, json.dumps(res, ensure_ascii=False))

                    else:
                        excel_data.write_excel_data(i+2, 13, "失败")
                        excel_data.write_excel_data(i+2, 14, json.dumps(res, ensure_ascii=False))

                if excepect_method == 'json':  #json表示：用例里面的预期结果方式为json； 主要是用来做对比，将期望的result.json里面的与最终请求返回的数据进行对比
                    if code == 0:
                        status_str = 'sucess'
                    else:
                        status_str = 'error'
                    excepect_result = get_result_json(url, status_str)
                    result = handle_result_json(res, excepect_result)
                    if result:
                        excel_data.write_excel_data(i+2, 13, "通过")
                        excel_data.write_excel_data(i+2, 14, json.dumps(res, ensure_ascii=False))

                    else:
                        excel_data.write_excel_data(i+2, 13, "失败")
                        excel_data.write_excel_data(i+2, 14, json.dumps(res, ensure_ascii=False))


if __name__ == '__main__':
    run = RunMain()
    run.run_main()

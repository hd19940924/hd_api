import sys
sys.path.append("D:/yiq/Demo")
import requests

from Util.get_server import server_data


class BaseRequests:
    #1-1：封装发送post方法；
    def send_post(self, url, data,  header=None):
        res = requests.post(url=url, data=data, headers=header)
        return res

    #1-1：封装发送get方法；
    def send_get(self, url, data, header=None):
        res = requests.get(url=url, params=data, headers=header)
        return res

    #1-1：封装请求的主方法；
    def run_main(self, method, url, data,  header=None):

        #通过封装读取server配置后，拼接url
        base_url = server_data.get_value('host') #获取host
        if 'http' not in url:   #如果原来url中没有http，那么新的url = host+url
            url = base_url + str(url)

        if method =='get':
            res = self.send_get(url, data, header)
        else:
            res = self.send_post(url, data, header)
        return res
base_request = BaseRequests()

if __name__ == '__main__':
    res = BaseRequests()
    data1 = "phone=13612996061&pwd=yiqing0406"
    header = {
 "Content-Type" : "application/x-www-form-urlencoded"
 }

    data = res.run_main('POST', '/pub/api/v1/web/web_login', data=data1, header=header).json()
    print(data)



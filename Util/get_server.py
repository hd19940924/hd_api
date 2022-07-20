import sys
sys.path.append("D:/yiq/Demo")
import configparser
import os

base_path = os.getcwd()  #当前路径
path = os.path.abspath(os.path.dirname(os.getcwd()))  #上级路径


class GetServer:
    def load_ini(self):
        file_path = path +'/Config/server.ini'  #读取ini文件的路径
        #file_path = 'D:/yiq/Demo/Config/server.ini'  #读取ini文件的路径
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding='utf-8-sig')
        return cf

    def get_value(self, key, section=None):
        if section == None:
            section = 'server'
        cf = self.load_ini()
        try:
            data = cf.get(section, key)
        except Exception:
            print("没有获取到值")
            data = None
        return data

server_data = GetServer()
#print(server_data.get_value("host"))
#print(type(server_data.get_value("host")))

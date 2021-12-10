import requests
from core.my_log import MyLog
import json
from conf.get_path import *
# from pack6.tool.get_code import GetCode
class HttpRequest:
    @staticmethod
    def http_request(url,  method, data=None,headers=None, Cookie=None, files=None):
        try:
            if method.lower() == 'get':
                res = requests.get(url=url, headers=headers, params=data)
            elif method.lower() == 'post':
                res = requests.post(url=url, headers=headers, data=data, files=files)
            else:
                MyLog().info('请求方法错误')
        except Exception as e:
            MyLog().info('请求报错：%s'%e)
            raise e
        return res

    @staticmethod
    def getJson(key,value):
        with open(json_path, 'r', encoding='utf-8') as f:
            line = json.loads(f.read())
            f.close()
        for i in range(len(key)):
            line['cardinfo'][key[i]]=value[i]
        line = json.dumps(line)
        return line

    @staticmethod
    def getHeaders():
        with open(headers_path, 'r', encoding='utf-8') as f:
            line = json.loads(f.read())
            f.close()

        return line
if __name__ == '__main__':
    url='http://192.168.0.203:5007/api/CardInfoCheck/CheckData/'
    a = '{ "usercode": "UniCheckDev","userpwd": "UniCheckDev2021$",  "": ""}'
    headers={
 "POST": "/api/CardInfoCheck/CheckData HTTP/1.1",
 "Host": "192.168.0.203:5007",
 "Connection": "keep-alive",
 "Content-Length": "96",
 "accept": "application/json",
 "request-from": "swagger",
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
 "Content-Type": "application/json-patch+json",
 "Origin": "http://192.168.0.203:5007",
 "Referer": "http://192.168.0.203:5007/index.html",
 "Accept-Encoding": "gzip, deflate",
 "Accept-Language": "zh-CN,zh;q=0.9"
}





    # res = requests.post(url=url,data=a,headers=headers)
    # print(res.status_code)
    # print(res.content)
    # print(res.text)
    # # data={"guid": "1"}
    # # # print(type(data))
    # # # data_json=json.dumps(data)
    # # # print(data_json)
    # # res=HttpRequest.http_request(url='http://192.168.0.203:1011/api/Img',data=data,method='get')
    # # print(res.content)
    # # print(res.text)
    #




    headers='''
       Connection	keep-alive
Accept	text/plain, */*; q=0.01
Accept-Encoding	gzip, deflate
Accept-Language	zh-CN,zh;q=0.9
Content-Type	application/x-www-form-urlencoded;charset=UTF-8
Host	202.61.88.12:8280
Origin	http://202.61.88.12:8280
Referer	http://202.61.88.12:8280/succezci/meta/SCWSZBCI/collections/index?selectedId=314867725
supsvg	1
User-Agent	Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36
X-Requested-With	XMLHttpRequest
Content-Length	38
Cookie	JSESSIONID=FEF48F0BA1C899008E51BCE5518A2BDD; SRV=back1-172-18-81-85-8080; JSESSIONID=A869ABA88758C1EA32E7D0A69C19CC68
    '''



    # 去除参数头尾的空格并按换行符分割
    headers = headers.strip().split('\n')
    # 使用字典生成式将参数切片重组，并去掉空格，处理带协议头中的://
    headers = {x.split(':')[0].strip(): ("".join(x.split(':')[1:])).strip().replace('//', "://") for x in headers}

    # 使用json模块将字典转化成json格式打印出来
    print(json.dumps(headers, indent=1))

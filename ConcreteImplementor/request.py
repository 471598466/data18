import trace
from conf.get_path import *
from conf.get_config import ReadConfig
from core.http_request import HttpRequest
import json
import re
import sys
class Request:
    #####################登录##################################################
    @staticmethod
    def login():
        url=ReadConfig.read_config(config_path,'LOGIN','url')+ReadConfig.read_config(config_path,'LOGIN','login')
        headers=ReadConfig.read_config(config_path,'LOGIN','headers')
        headers=eval(headers)
        par=eval(ReadConfig.read_config(config_path,'LOGIN','par'))
        res = HttpRequest.http_request(url=url, method='post',data=par, headers=headers)
        resHeaders=str(res.headers)
        #去除单引号及括号
        resHeaders=resHeaders.replace('{','')
        resHeaders=resHeaders.replace('}','')
        resHeaders=resHeaders.replace("'","")
        # 去除参数头尾的空格并按换行符分割
        resHeaders = resHeaders.strip().split(';')
        # 使用字典生成式将参数切片重组，并去掉空格，处理带协议头中的://
        resHeaders = {x.split(':')[0].strip(): ("".join(x.split(':')[1:])).strip().replace("/", "://") for x in resHeaders}

        # 使用json模块将字典转化成json格式打印出来
        resHeaders=json.dumps(resHeaders, indent=1)
        JSESSIONID=str(eval(resHeaders)['Set-Cookie']).split('=')[1]
        return JSESSIONID

    @staticmethod
    def hospcode(JSESSIONID):
        url=ReadConfig.read_config(config_path,'HOSPCODE','url')
        headers=str(ReadConfig.read_config(config_path,'HOSPCODE','headers'))
        headers=headers.replace('@@@@@@','%')
        headers=eval(headers%(JSESSIONID))
        par = ReadConfig.read_config(config_path, 'HOSPCODE', 'par')
        par=par.replace('@@@@@@','%')
        par = par % str((ReadConfig.read_config(config_path, 'MONTH', 'month')))
        par=par.replace('#####','%')
        par=eval(par)
        res = HttpRequest.http_request(url=url, method='post', data=par, headers=headers)
        response=json.loads(res.text[1:-1])
        list=[]
        list1=[]
        for i in range(len(response)):
            list1.append(response['children'][i]['$realid'])
            list1.append(response['children'][i]['caption'])
            list.append(list1)
            list1 = []
        return  list

    @staticmethod
    def hospital(JSESSIONID,hospcode):
        url = ReadConfig.read_config(config_path, 'HOSPITAL', 'url')
        headers = str(ReadConfig.read_config(config_path, 'HOSPITAL', 'headers'))
        headers = headers.replace('@@@@@@', '%')
        headers = eval(headers % (JSESSIONID))
        par = ReadConfig.read_config(config_path, 'HOSPITAL', 'par')
        par = par.replace('@@@@@', '%')
        month=str((ReadConfig.read_config(config_path, 'MONTH', 'month')))
        par = par % (hospcode,month)
        par = par.replace('@@@', '%')
        try:

            res = HttpRequest.http_request(url=url, method='post', data=par, headers=headers)
            response = json.loads(res.text)
            list = []
            list1 = []
            for i in range(len(response)):
                list1.append(response[i]['$realid'])
                list1.append(response[i]['caption'])
                list.append(list1)
                list1 = []

            return list
        except Exception as e:
            print('请求医院名称失败：%s'%e)

        except:
            return []
    @staticmethod
    def dataProcessing(JSESSIONID,orgcode,hospcode):
        print('orgcode %s'%type(orgcode))
        print('hospcode %s' % type(hospcode))
        url = ReadConfig.read_config(config_path, 'DATAPROCESSING', 'url')
        headers = str(ReadConfig.read_config(config_path, 'DATAPROCESSING', 'headers'))
        headers = headers.replace('@@@@@@', '%')
        headers = eval(headers % (JSESSIONID))
        par = ReadConfig.read_config(config_path, 'DATAPROCESSING', 'par')
        par = par.replace('@@@@@', '%')
        month = str((ReadConfig.read_config(config_path, 'MONTH', 'month')))
        monthold = str((ReadConfig.read_config(config_path, 'MONTH', 'monthold')))
        #当前月、区域机构编码、医院编码、上月、区域机构编码、医院编码
        par = par % (month,orgcode,hospcode,monthold,orgcode,hospcode)
        par = par.replace('@@@', '%')
        try:
            list = []
            res = HttpRequest.http_request(url=url, method='post', data=par, headers=headers)
            root = res.text
            root = re.findall(r'<table name="B0">(.+?)</table>', root)
            root1 = re.findall(r'<row>(.+?)</row><row>', str(root))
            root2 = re.findall(r'</row><row>(.+?)</row>', str(root))
            print('root1 :{}  :{}'.format(type(root1),root1))
            print('root2 :{}  :{}'.format(type(root2), root2))
            if root1==[]:
                root1.append(monthold)
                for root1aa in range(0,100):
                    root1.append('')
                    a=root1
            else:
                a = "['" + root1[0] + "']"
                a = a.replace(",", "','")
                a=eval(a)

            if root2==[]:
                root2.append(month)
                for root2bb in range(0,100):
                    root2.append('')
                    b=root2
            else:
                b = "['" + root2[0] + "']"
                b = b.replace(",", "','")
                b=eval(b)


            list.append(a)
            list.append(b)
            return list
        except Exception as e:
            print('爬取医院数据失败：%s'%e)

if __name__ == '__main__':

    JSESSIONID= Request.login()
    res = Request.dataProcessing(JSESSIONID, '510000000300', '510000006294')
    print(res)

    # orglist=Request.hospcode(JSESSIONID)
    # for a in range(len(orglist)):
    #     hosplist = Request.hospital(JSESSIONID, orglist[a][0])
    #     print(orglist[a][0],orglist[a][1])
    #     for b in range(len(hosplist)):
    #         print(orglist[a][0], hosplist[b][0])
    #         res = Request.dataProcessing(JSESSIONID, orglist[a][0], hosplist[b][0])
    #         print( hosplist[b][0], hosplist[b][1])
    #         print('res : {}'.format(res))

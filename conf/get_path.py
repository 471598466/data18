import os

'''专门来读取路径的值'''
#os.path.split(os.path.realpath(__file__))[0]
path=os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]
# print(path)

#测试用例的路径
case_path=os.path.join(path,'data18/conf','data.xlsx')
# print(case_path)
#json文件路径
json_path=os.path.join(path,'data18/conf','jxkh.json')

#创表的sql路径
getCreate_path=os.path.join(path,'data18/conf','createSql')
#插入数据sql路径
getInsert_path=os.path.join(path,'data18/conf','insertSql')
#查询列名sql路径
getSelect_path=os.path.join(path,'data18/conf','selectSql')
#请求头路径
headers_path=os.path.join(path,'data18/conf','headers.json')
#配置文件路径
config_path=os.path.join(path,'data18/conf','case.config')
# print(config_path)

#识别的验证码保存的路径
code_path=os.path.join(path,'pack6/tool','code.png')
# print(code_path)

#测试报告路径
report_path=os.path.join(path,'pack6/result','report.html')
# print(report_path)

#日志路径
log_path=os.path.join(path,'data18/conf','all_log.txt')
# print(log_path)



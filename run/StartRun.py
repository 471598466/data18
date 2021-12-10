from core.do_sql import DoMysql
from conf.get_config import ReadConfig
from conf.get_path import *
import  time
from ConcreteImplementor.request import Request
import datetime
from core.gettime import *
import logging
import inspect
import sys
import traceback
class operation:
    isrun = 0
    def __init__(self):
        self.logger = self._getLogger()
        self.isrun=0
    def _getLogger(self):
        logger = logging.getLogger('[PythonServiceErr]')

        this_file = inspect.getfile(inspect.currentframe())
        dirpath = os.path.abspath(os.path.dirname(this_file))
        handler = logging.FileHandler(os.path.join(dirpath, "serviceErr.log"))

        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        return logger
    def run(self):

        # 当前日期

        now = datetime.datetime.now().date()
        year, month, day = str(now).split("-")  # 切割
        # 年月日，转换为数字
        year = int(year)
        month = int(month)
        day = int(day)
        # 获取这个月最后一天
        last_day = last_day_of_month(datetime.date(year, month, day))
        # 判断当前日期是否为月末
        if str(now) == str(last_day):
            if self.isrun == 0:
                try:
                    setTime()
                    res = ReadConfig.read_config(config_path, 'DB', 'db_config')
                    print(res)
                    # 读取创表语句
                    with open(getCreate_path, 'rt', encoding='utf-8') as f:
                        res = f.readlines()
                        cre = ''
                        for x in res:
                            if r'\n' in x:
                                x = x.replace(r'\n', ' ')
                            cre = cre + x
                        print(cre)
                        cre = str(cre)
                        f.close()
                    print(cre)

                    # 修改要创建的表名
                    tableName = 'WT_1_8' + time.strftime("%Y_%m_%d_%H%M%S")
                    cre = cre % (tableName)
                    # 创建表
                    DoMysql('DB', 'db_config').create(cre)

                    # 获取查询列名的语句
                    # 读取创表语句
                    with open(getSelect_path, 'rt', encoding='utf-8') as f:
                        res = f.readlines()
                        select = ''
                        for x in res:
                            if r'\n' in x:
                                x = x.replace(r'\n', ' ')
                            select = select + x
                        print(select)
                        select = str(select)
                        f.close()
                    print(select)
                    # 查询表列名
                    selectColumns = select % (tableName)
                    print(selectColumns)
                    list = DoMysql('DB', 'db_config').select(selectColumns, 1)
                    print(list)
                    insertColumns = ''
                    for i in range(len(list)):
                        insertColumns = insertColumns + str(list[i][0]) + ','
                    insertColumns = insertColumns[:-1]
                    insertColumns = '[' + insertColumns + ']'
                    insertColumns = insertColumns.replace(',', '],[')
                    # 获取插入语句
                    with open(getInsert_path, 'rt', encoding='utf-8')as f:
                        res = f.readlines()
                        insert = ''
                        for x in res:
                            if r'\n' in x:
                                x = x.replace(r'\n', ' ')
                            insert = insert + x
                        print(insert)
                        select = str(insert)
                        f.close()
                    ########请求医院数据
                    tablelsit = eval(ReadConfig.read_config(config_path, 'INSERT', 'tablelist'))
                    JSESSIONID = Request.login()
                    orglist = Request.hospcode(JSESSIONID)  # 获取医疗机构(大类)名
                    for a in range(len(orglist)):
                        hosplist = Request.hospital(JSESSIONID, orglist[a][0])  # 获取医院编码及名称
                        print(orglist[a][0], orglist[a][1])
                        for b in range(len(hosplist)):
                            print(orglist)
                            insertValue = Request.dataProcessing(JSESSIONID, orglist[a][0], hosplist[b][0])
                            d = str(hosplist[b][0]) + "," + str(hosplist[b][1])
                            for i in range(len(tablelsit)):
                                if i == 0:
                                    d = str(hosplist[b][0]) + "," + str(hosplist[b][1])
                                print([tablelsit[i]])
                                e = insertValue[0][eval(tablelsit[i])]
                                f = insertValue[1][eval(tablelsit[i])]
                                d = d + ',' + str(e) + ',' + str(f)
                            print('insertValue[1][0]:{}'.format(insertValue[1][0]))
                            d = "'" + d + "," + insertValue[1][0] + "'"
                            d = d.replace(",", "','")
                            print('insert %s' % type(insert))
                            print('ddddddddddd %s' % d)
                            insert1 = insert % (tableName, insertColumns, d)
                            DoMysql('DB', 'db_config').insert(insert1)
                            print(hosplist[b][0], hosplist[b][1])
                    self.isrun = 1
                    self.logger.info(" {}数据已成功抓取，数据存入至：{}:".format(insertValue[1][0],tableName) )
                except Exception as e:
                    dropTable=' drop table  '+str(tableName)
                    DoMysql('DB', 'db_config').insert(dropTable)
                    self.logger.info("Unexpected error:", sys.exc_info()[0])
                    self.logger.info('发生错误 删除表'+str(tableName)+'重新获取数据')
                    aa, bb, cc = sys.exc_info()
                    for i in traceback.extract_tb(cc):
                        self.logger.info('错误信息：{}'.format(i))
                    self.isrun = 0
                    self.logger.info('发生错误 ' + 'insertValue = %s' % insertValue)
                    self.logger.info('发生错误 ' + 'hosplist =  %s' % hosplist)
                    self.logger.info(e)
                    self.isrun=0

            else:
                print('本月数据已抓取成功！')
        else:
            self.isrun = 0
            print('非当月月末')

if __name__ == '__main__':
    a = operation()
    while True:
        a.run()
        time.sleep(10)

import pymssql
from conf.get_config import ReadConfig
from conf.get_path import *
'''
操作数据库的步骤：
1.连接数据库，通过connect函数连接，生成connection对象
2.定义游标cursor,再通过游标执行脚本并获取结果
3.关闭连接

常用方法：
1.cursor()：使用当前连接创建并返回游标
2.commit():提交当前事务，如果脚本对数据库做了修改，那么必须要做提交动作，例如：insert，update
3.rollback():回滚当前事务
4.close()：关闭当前连接

游标操作方法：
1.execute():执行数据库查询或者命令，将结果从数据库返回给客户端
2.fetchone():获取结果集的下一行，返回的数据格式是元祖形式的
3.fetchall():获取结果集的所有行，返回的数据是列表形式的，列表嵌套元祖
4.fetchmany():获取结果集的几行

中文乱码解决方案：
charset=GBK，varchar表正常，nvarchar表空值
charset=utf8，varchar表乱码，nvarchar正常
charset不使用，varchar表乱码，nvarchar正常
'''

class DoMysql:
    def __init__(self,db,config):
        db_config=eval(ReadConfig.read_config(config_path, db, config))
        # print(db_config)
        try:
            self.con = pymssql.connect(**db_config)
            if self.con:
                print('连接成功！')
        except Exception as e:
            print('初始化数据库连接失败：%s' % e)

    def select(self,query,state='all'):#默认了state=all，若不指定state的值，则调用fetchall()方法
        try:
            print(state)
            cursor = self.con.cursor()
            cursor.execute(query)
            list=[]
            if state == 1:
                res = cursor.fetchone()  # 元祖，针对一条数据
                while res:
                    list.append(res)
                    res = cursor.fetchone()  # 元祖，针对一条数据
            else:
                res = cursor.fetchall()  # 列表，针对多条数据
                while res:
                    list.append(res)
                    res = cursor.fetchall()  # 列表，针对多条数据
            return list
        except Exception as e:
            print('数据库查询失败:%s'%e)
        finally:
            cursor.close()
            self.con.close()
    def create(self,query):
        cursor = self.con.cursor()
        try:
            cursor.execute(query)
            self.con.commit()
            print('创建成功')
        except Exception as e:
            print('数据库创建失败:%s' % e)
        finally:
            cursor.close()
            self.con.close()
    def insert(self,query):
        try:
            cursor = self.con.cursor()
            cursor.execute(query)
            self.con.commit()
            return True
        except Exception as e:
            print('数据库插入失败：%s'%e)
            cursor.rollback()
        finally:
            cursor.close()
            self.con.close()


    def  close(self):

        self.con.close()


if __name__ == '__main__':

    query='select b.id,b.code,b.name from ts_dip_check_master a,ts_dip_check_detail b where a.id=b.masterid and a.id=b.masterid and a.id=1 order by code'
    res=(DoMysql('DB2', 'db_config').select(query, 1))
    print(res)
    print(res[0])
    for i in range(len(res)):
        print(res[i][1])
        print(res[i][2])
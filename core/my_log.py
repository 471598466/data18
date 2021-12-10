import logging
from conf.get_path import *
'''
学习网址：https://www.cnblogs.com/yyds/p/6901864.html
日志分为五个级别：debug、info、warning、error、critical，未指定级别时默认只输出warning及以上级别的日志，
默认的输出渠道为控制台，若想要以文件的形式输出，是要使用handler中的函数
'''
class MyLog:
    #1.创建一个日志收集器
    logger=logging.getLogger('mylogger')

    #2.设定级别
    logger.setLevel('DEBUG')#如果不设置级别，会默认从warning及以上级别输出，跟输出渠道对接时，谁输出的级别高则遵从谁

    #3.创建自己的输出渠道，输出在哪里，输出什么级别的，输出什么格式的
    ch=logging.StreamHandler()#控制台渠道
    ch.setLevel('ERROR')
    ch.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(name)s - 日志信息：%(message)s'))

    fh=logging.FileHandler(log_path,encoding='utf-8')#文件渠道
    fh.setLevel('DEBUG')
    fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    #4.两者对接，将输出渠道加入到日志收集器中
    logger.addHandler(ch)
    logger.addHandler(fh)

    def debug(self,msg):
        self.logger.debug(msg)

    def info(self,msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)


if __name__ == '__main__':
    MyLog().debug('111')
    MyLog().info('222')
    MyLog().warning('333')
    MyLog().error('444')
    MyLog().critical('555')
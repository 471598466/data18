import datetime
from conf.get_config import ReadConfig
from conf.get_path import *
def last_day_of_month(any_day):
    """
    获取获得一个月中的最后一天
    :param any_day: 任意日期
    :return: string
    """
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)

def setTime():
    if datetime.date.today().month - 1 == 0:
        objectTime = str(datetime.date.today().year - 1) + '12'
        lastObjectTime = str(datetime.date.today().year - 1) + '11'
    elif datetime.date.today().month - 1 == 1:
        objectTime = str(datetime.date.today().year) + '0' + str(datetime.date.today().month - 1)
        lastObjectTime = str(datetime.date.today().year - 1) + '12'
    else:
        objectTime = str(datetime.date.today().year) + str(datetime.date.today().month - 1)
        lastObjectTime = str(datetime.date.today().year) + str(datetime.date.today().month - 2)
        if len(objectTime) == 5:
            objectTime1 = objectTime[0:4]
            objectTime2 = objectTime[4]
            objectTime = objectTime1 + '0' + objectTime2
        if len(lastObjectTime) == 5:
            lastObjectTime1 = lastObjectTime[0:4]
            lastObjectTime2 = lastObjectTime[4]
            lastObjectTime = lastObjectTime1 + '0' + lastObjectTime2
    time = '%s%s%s' % (datetime.datetime.year, datetime.datetime.month, datetime.datetime.day)
    ReadConfig.read_config(config_path, 'MONTH', 'month')
    ReadConfig.setConfig(config_path, 'MONTH', 'month', objectTime)
    ReadConfig.read_config(config_path, 'MONTH', 'monthold')
    ReadConfig.setConfig(config_path, 'MONTH', 'monthold', lastObjectTime)

if __name__ == '__main__':

    # 当前日期
    now= datetime.datetime.now().date()
    year,month,day = str(now).split("-")  # 切割
    # 年月日，转换为数字
    year = int(year)
    month = int(month)
    day = int(day)

    # 获取这个月最后一天
    last_day = last_day_of_month(datetime.date(year, month, day))
    # 判断当前日期是否为月末
    if str(now) == str(last_day):
        print('yes')
    else:
        print('no')
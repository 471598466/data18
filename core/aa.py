import time
import datetime
print ("格式参数：")
print (" %a  星期几的简写")
print (" %A  星期几的全称")
print (" %b  月分的简写")
print (" %B  月份的全称")
print (" %c  标准的日期的时间串")
print (" %C  年份的后两位数字")
print (" %d  十进制表示的每月的第几天")
print (" %D  月/天/年")
print (" %e  在两字符域中，十进制表示的每月的第几天")
print (" %F  年-月-日")
print (" %g  年份的后两位数字，使用基于周的年")
print (" %G  年分，使用基于周的年")
print (" %h  简写的月份名")
print (" %H  24小时制的小时")
print (" %I  12小时制的小时")
print (" %j  十进制表示的每年的第几天")
print (" %m  十进制表示的月份")
print (" %M  十时制表示的分钟数")
print (" %n  新行符")
print (" %p  本地的AM或PM的等价显示")
print (" %r  12小时的时间")
print (" %R  显示小时和分钟：hh:mm")
print (" %S  十进制的秒数")
print (" %t  水平制表符")
print (" %T  显示时分秒：hh:mm:ss")
print (" %u  每周的第几天，星期一为第一天 （值从0到6，星期一为0）")
print (" %U  第年的第几周，把星期日做为第一天（值从0到53）")
print (" %V  每年的第几周，使用基于周的年")
print (" %w  十进制表示的星期几（值从0到6，星期天为0）")
print (" %W  每年的第几周，把星期一做为第一天（值从0到53）")
print (" %x  标准的日期串")
print (" %X  标准的时间串")
print (" %y  不带世纪的十进制年份(值从0到99)")
print (" %Y  带世纪部分的十制年份")
print (" %z,%Z   时区名称，如果不能得到时区名称则返回空字符。")
print (" %%  百分号")

print ("----------------------------------------------------------")
print ("python里使time模块来获取当前的时间")


print ("24小时格式：" + time.strftime("%H:%M:%S"))
print ("12小时格式：" + time.strftime("%I:%M:%S"))
print ("今日的日期：" + time.strftime("%d/%m/%Y"))

print ("----------------------------------------------------------")

print ("使用datetime模块来获取当前的日期和时间")

i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" %i.year)
print ("当前的月份是 %s" %i.month)
print ("当前的日期是  %s" %i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" %i.hour)
print ("当前分钟是 %s" %i.minute)
print ("当前秒是  %s" %i.second)
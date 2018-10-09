# coding=utf-8
# 地点：国家海洋环境监测中心
# 作者：李炳南
# 时间：2017-12-14
# 说明：生成博客园需要的标题格式的HTML代码
import os

str1 = raw_input("input:")
num = '0'

# <div class="title_hh"><a name="A01"></a><strong>一、Python数学函数</strong></div>
# <div class="arrow-left">&nbsp;</div>
# 
# 通过判断输入数据里面的数字来给代码增加Anchor
# 参考：http://blog.csdn.net/jarvischu/article/details/8962497
# 处理含中文的的字符串需要转码

str_chn = unicode(str1, "gbk")

if(str_chn.find(u'一') == 0):
	num = '1'
elif(str_chn.find(u'二') == 0):
	num = '2'
elif(str_chn.find(u'三') == 0):
	num = '3'
elif(str_chn.find(u'四') == 0):
	num = '4'
elif(str_chn.find(u'五') == 0):
	num = '5'
elif(str_chn.find(u'六') == 0):
	num = '6'

str_title = "<div class=\"title_hh\"><a name=\"A0" + num + "\"></a><strong>" + str1 + "</strong></div>\n<div class=\"arrow-left\">&nbsp;</div>"

print(str_title)

os.system("pause")
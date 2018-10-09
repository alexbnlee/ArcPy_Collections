# coding=utf-8
# 地点：国家海洋环境监测中心
# 作者：李炳南
# 时间：2018-01-14
# 说明：对于指定文件夹内部的所有 GeoTIFF 文件进行 Calculate Statistics 操作

import os
fo = open("D:\\03-Study\\Python\\test\\cnblog1.txt", "r+")
all_str = fo.read()
fo.close()
str1 = all_str.replace("font-family: times new roman, times;", "font-family: Georgia;")
str2 = str1.replace("-----------------------------------------------", "----------------------------------------------------------------------------------")
str3 = str2.replace("#800080", "#FFCC00")
str4 = str3.replace("background-color: #000000", "background-color: #333333")
str5 = str4.replace("background-color: #dddddd", "background-color: #333333")
fo1 = open("D:\\03-Study\\Python\\test\\cnblog1.txt", "w+")
fo1.write(str5)
fo1.close()


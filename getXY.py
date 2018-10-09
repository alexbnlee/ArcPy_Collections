# coding=utf-8
# 地点：国家海洋环境监测中心
# 作者：李炳南
# 时间：2017-12-11
# 说明：查询符合要求文件的xy坐标

import arcpy
arcpy.env.workspace = r"D:\McDelfino\dev\bdh_red\IDL80\resource\maps\shape"
fc = "states.shp"
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@XY"])
for row in cursor:
	# 通过数组对x和y进行赋值
    x, y = row[0]
    print("{0}, {1}".format(x,y))
    


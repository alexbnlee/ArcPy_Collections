# coding=utf-8
# 地点：国家海洋环境监测中心
# 作者：李炳南
# 时间：2017-12-11
# 说明：查询矢量数据的相关field内容

import arcpy
arcpy.env.workspace = r"D:\McDelfino\dev\bdh_red\IDL80\resource\maps\shape"
fc = "country.dbf"
cursor = arcpy.da.SearchCursor(fc, ["CNTRY_NAME"])
for row in cursor:
    print "Name = {0}".format(row[0])
    


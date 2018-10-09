# coding=utf-8
# 地点：国家海洋环境监测中心
# 作者：李炳南
# 时间：2017-12-07
# 说明：对于指定文件夹内部的所有 GeoTIFF 文件进行 Calculate Statistics 操作

print("------Start Processing------")

import arcpy

arcpy.env.workspace = r"D:\01-Working\2017\20171204-IDL_Average\test"
files_raster = arcpy.ListRasters()

for f in files_raster:
	print("------Processing " + f)
	arcpy.CalculateStatistics_management(f)

print("------Processing Completion------")

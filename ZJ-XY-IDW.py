# coding=utf-8
# 地点：国家海洋环境监测中心
# 作者：李炳南
# 时间：2017-12-27
# 说明：首先将txt数据导入ArcGIS

print("------ Start Processing ------")
print("")

import arcpy
import os
# import shutil


#开启覆盖模式，故因提前处理用于指示文件名的字段中的重名情况
arcpy.env.overwriteOutput = True

# 处理文件所在系的工作空间，即文件夹，注意反斜杠前面的“r”
arcpy.env.workspace = r"D:\01-Working\2017\20171204-IDL_Average\chen-sd\ASCII"

# 获取内部的数据
files_txt = arcpy.ListFiles()

# 对数据进行遍历，并执行工具操作，注意加扩展名，否则容易出错
for f in files_txt:
	print("-- Processing " + f)
	# 将txt数据导入
	arcpy.MakeXYEventLayer_management(f, "Longitude", "Latitude", f)
	# 将导入的数据执行IDW操作
	#arcpy.env.workspace = r"D:\Windows-Linux\Data\2015\IDW"

	# outIDW = arcpy.sa.Idw(f, "sd")
	# outIDW.save("D:/Windows-Linux/Data/2015/IDW/" + f + ".tif")

	(arcpy.sa.Idw(f, "sd")).save(arcpy.env.workspace + "/IDW/" + f + ".tif")

	# rs = arcpy.ListRasters()
	# shutil.rmtree(arcpy.env.workspace + rs[0])
	# shutil.rmtree(arcpy.env.workspace + "/info")
	# xml = arcpos.remove(arcpy.env.workspace + xml[0])



print("")
print("------ Processing Completion ------")

# 用于暂停显示，否则窗体会一闪而过
os.system("pause")
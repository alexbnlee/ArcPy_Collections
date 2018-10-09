# coding=utf-8
# 地点：国家海洋环境监测中心
# 作者：李炳南
# 时间：2017-12-07
# 说明：对于指定文件夹内部的所有 GeoTIFF 文件进行 Calculate Statistics 操作

mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]
lyrs = arcpy.mapping.ListLayers(mxd)
len(lyrs)
lyrs[42-8]
lyrs[42-8].name
lyrs[34].name
lyrs[35].name
arcpy.mapping.UpdateLayer(df, lyrs[1], lyrs[34])
lyrs[5]
lyrs[6]
arcpy.mapping.UpdateLayer(df, lyrs[6], lyrs[34])
lyrs[6].visible=False
arcpy.RefreshActiveView()
for i in range(7, 16):
    arcpy.mapping.UpdateLayer(df, lyrs[i], lyrs[34])
    lyrs[i].visible = False
    
arcpy.mapping.UpdateLayer(df, lyrs[16], lyrs[34])
lyrs = arcpy.mapping.ListLayers(mxd)
lyrs[6]
lyrs[17]
lyouts = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")
len(lyouts)
lyouts[0].text
print lyouts[0].text
print lyouts[1].text
lyouts[1].text = "坐标系：WGS-84     投影：经纬度     制图时间：2018年     制图单位：国家海洋环境监测中心"
arcpy.RefreshActiveView()
print lyouts[2].text
lyouts[2].text = "浙江及邻近海域悬浮物卫星遥感专题图\n2017年1月"
arcpy.RefreshActiveView()
mon = 0    
arcpy.env.workspace = r"D:\01-Working\2017\20171204-IDL_Average\Final-TSM"
lyouts[2].text = "浙江及邻近海域悬浮物卫星遥感专题图\n2017年" + str(mon) + "月"
lyouts[2].text = "浙江及邻近海域悬浮物卫星遥感专题图\n2017年" + mon + "月"
import os
lyouts[2].text = "浙江及邻近海域悬浮物卫星遥感专题图\n2017年" + str(mon) + "月"
str
del str
lyouts[2].text = "浙江及邻近海域悬浮物卫星遥感专题图\n2017年" + str(mon) + "月"
for i in range(6, 18):
    mon = mon + 1
    lyouts[2].visible=True
    lyouts[2].text = "浙江及邻近海域悬浮物卫星遥感专题图\n2017年" + str(mon) + "月"
    arcpy.mapping.ExportToJPEG(mxd, lyrs[i].name + ".jpg", resolution=300)
    lyouts[2].visible=False
    
for i in range(6, 18):
    mon = mon + 1
    lyouts[2].visible=True
    lyouts[2].text = "浙江及邻近海域悬浮物卫星遥感专题图\n2017年" + str(mon) + "月"
    arcpy.mapping.ExportToJPEG(mxd, r"D:\01-Working\2017\20171204-IDL_Average\Final-TSM\" + lyrs[i].name + ".jpg", resolution=300)
    lyouts[2].visible=False
    
for i in range(6, 18):
    mon = mon + 1
    lyouts[2].visible=True
    lyouts[2].text = "浙江及邻近海域悬浮物卫星遥感专题图\n2017年" + str(mon) + "月"
    arcpy.mapping.ExportToJPEG(mxd, "D:\\01-Working\\2017\\20171204-IDL_Average\\Final-TSM\\" + lyrs[i].name + ".jpg", resolution=300)
    lyouts[2].visible=False
    
lyrs = arcpy.mapping.ListLayers(mxd)
lyrs[7]
lyrs[19]
lyrs[18]
mon = 0
for i in range(7, 19):
    mon = mon + 1
    lyrs[i].visible=True
    lyouts[2].text = "浙江及邻近海域悬浮物卫星遥感专题图\n2017年" + str(mon) + "月"
    arcpy.mapping.ExportToJPEG(mxd, "D:\\01-Working\\2017\\20171204-IDL_Average\\Final-TSM\\" + lyrs[i].name + ".jpg", resolution=300)
    lyrs[i].visible=False
    


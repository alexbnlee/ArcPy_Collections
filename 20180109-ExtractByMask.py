arcpy.ExtractByMask_sa('file01.tif', 'zjwt12_Erase', r'D:\McDelfino\Documents\ArcGIS\Default.gdb\fdgdfgdfgdf')
mon = 0
for i in range(8,20):
    mon = mon + 1
    arcpy.sa.ExtractByMask(lyrs[i], lyrs[0], "D:/01-Working/2017/20171204-IDL_Average/temp/TSM/Extract_TSM3_MON_" + str(mon))
    
arcpy.ExtractByMask_sa('file01.tif', 'zjwt12_Erase', r'D:\McDelfino\Documents\ArcGIS\Default.gdb\fdgdfgdfgdf')
ms = arcpy.sa.ExtractByMask(lyrs[8], lyrs[0])
ms = arcpy.sa.ExtractByMask(lyrs[9], lyrs[0])
arcpy.env.workspace = r"D:\01-Working\2017\20171204-IDL_Average\temp\TSM"
(arcpy.sa.ExtractByMask(lyrs[8], lys[0])).save("D:/01-Working/2017/20171204-IDL_Average/temp/TSM/aaa")
(arcpy.sa.ExtractByMask(lyrs[8], lyrs[0])).save("D:/01-Working/2017/20171204-IDL_Average/temp/TSM/aaa")
(arcpy.sa.ExtractByMask(lyrs[8], lyrs[0])).save("D:/01-Working/2017/20171204-IDL_Average/temp/TSM/aaa.tif")
mon = 0
for i in range(8,20):
    mon = mon + 1
    arcpy.sa.ExtractByMask(lyrs[i], lyrs[0], "D:/01-Working/2017/20171204-IDL_Average/temp/TSM/Extract_TSM5_MON_" + str(mon))
    
mon = 0
for i in range(8,20):
    mon = mon + 1
    (arcpy.sa.ExtractByMask(lyrs[i], lyrs[0])).save("D:/01-Working/2017/20171204-IDL_Average/temp/TSM/Extract_TSM5_MON_" + str(mon))
    

# mon 用来命名文件
# 将栅格数据通过给定的矢量文件剪切

mon = 0
for i in range(8,20):
    mon = mon + 1
    (arcpy.sa.ExtractByMask(lyrs[i], lyrs[0])).save("D:/01-Working/2017/20171204-IDL_Average/temp/TSM/Extract_TSM_MON_" + str(mon) + ".tif")
    


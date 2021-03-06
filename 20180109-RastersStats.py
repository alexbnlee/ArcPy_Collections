
# 获取栅格数据
arcpy.env.workspace=r"D:\01-Working\2017\20171204-IDL_Average\temp\TSM"
rs = arcpy.ListRasters()

# 遍历栅格数据获取统计信息
# 首先需要建立栅格文件
# 将数据结果保留两位小数
# 输出到txt文档中

fo = open("D:\\01-Working\\2017\\20171204-IDL_Average\\temp\\tsm_stats.txt", "w+")
for r in rs:
    ro = arcpy.Raster(r)
    fo.writelines(ro.name + "\n")
    fo.writelines("MAX: " + str(round(ro.maximum, 2)) + "\n")
    fo.writelines("MIN: " + str(round(ro.minimum, 2)) + "\n")
    fo.writelines("MEAN: " + str(round(ro.mean, 2)) + "\n\n")
    
fo.close()


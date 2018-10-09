
# 将12个月份排序
# 获取12个月所在的图层
# 获取图层唯一可查询变量
# 获取月份数据上面的一个图层作为基准

for f in range(12, 0, -1):
    lyrs = arcpy.mapping.ListLayers(mxd)
    for i in range(8, 20):
        sn = lyrs[i].name
        if sn.find("MON_" + str(f) + ".tif") > 0:
            arcpy.mapping.MoveLayer(df, lyrs[7], lyrs[i], "AFTER")
# 添加字段
arcpy.AddField_management(r"Clip_DAY\clip_day2016_1009", "area", "FLOAT")

# 批量添加列，没有必要，通过Calculateareas计算的时候会自动添加列的
for i in range(2, 22):
    arcpy.AddField_management(lyrs[i], "area", "FLOAT")
    
ap.setEnvWorkspace(r'D:\01-Working\2018\20180201-Data_Clip\shp_clip_areas')
feas = arcpy.ListFeatureClasses()

# 只能通过对工作空间内的shp文件操作，否则报错
# 文件存在同一个文件夹内，名字在元原名字前增加字符
for i in range(0, 22):
    arcpy.CalculateAreas_stats(feas[i], "areas_"+feas[i])
    
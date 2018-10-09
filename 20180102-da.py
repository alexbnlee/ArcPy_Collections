lyrs = arcpy.mapping.ListLayers(mxd)
mxd = arcpy.mapping.MapDocument("CURRENT")
lyrs = arcpy.mapping.ListLayers(mxd)
print len(lyrs)
for i in range(0, 70-5):
    arcpy.Clip_analysis(lyrs[i], "Ningbo", "cc_nb_" + lyrs[i].name + ".shp")
    
print len(lyrs)
arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\chichao\Taizhou"
for i in range(0, 70-5):
    arcpy.Clip_analysis(lyrs[i], "Taizhou", "cc_tz_" + lyrs[i].name + ".shp")
    
arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\chichao\Wenzhou"
for i in range(0, 70-5):
    arcpy.Clip_analysis(lyrs[i], "Wenzhou", "cc_wz_" + lyrs[i].name + ".shp")
    
arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\chichao\Zhoushan"
for i in range(0, 70-5):
    arcpy.Clip_analysis(lyrs[i], "Zhoushan", "cc_zs_" + lyrs[i].name + ".shp")
    
lyrs = arcpy.mapping.ListLayers(mxd)
print len(lyrs)
arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\maweizao\Ningbo"
for i in range(0, 70-5):
    arcpy.Clip_analysis(lyrs[i], "Ningbo", "mwz_nb_" + lyrs[i].name + ".shp")
    
for i in range(0, 85-5):
    arcpy.Clip_analysis(lyrs[i], "Ningbo", "mwz_nb_" + lyrs[i].name + ".shp")
    
lyrs = arcpy.mapping.ListLayers(mxd)
print len(lyrs)
for i in range(0, 85-5):
    arcpy.Clip_analysis(lyrs[i], "Ningbo", "mwz_nb_" + lyrs[i].name + ".shp")
    
arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\maweizao\Taizhou"
for i in range(0, 85-5):
    arcpy.Clip_analysis(lyrs[i], "Taizhou", "mwz_tz_" + lyrs[i].name + ".shp")
    
arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\maweizao\Wenzhou"
for i in range(0, 85-5):
    arcpy.Clip_analysis(lyrs[i], "Wenzhou", "mwz_wz_" + lyrs[i].name + ".shp")
    
arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\maweizao\Zhoushan"
for i in range(0, 85-5):
    arcpy.Clip_analysis(lyrs[i], "Zhoushan", "mwz_zs_" + lyrs[i].name + ".shp")
    
arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\chichao\Ningbo"
shps = arcpy.ListFeatureClasses()
arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\chichao"
arcpy.Merge_management(shps, "Chichao_Ningbo.shp")
arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\chichao\Ningbo"
shps = arcpy.ListFeatureClasses()
arcpy.Merge_management(shps, "Chichao_Ningbo.shp")
arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\chichao\Taizhou"
shps = arcpy.ListFeatureClasses()
arcpy.Merge_management(shps, "Chichao_Taizhou.shp")
arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\chichao\Wenzhou"
shps = arcpy.ListFeatureClasses()
arcpy.Merge_management(shps, "Chichao_Wenzhou.shp")
arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\chichao\Zhoushan"
arcpy.Merge_management(shps, "Chichao_Wenzhou.shp")
shps = arcpy.ListFeatureClasses()
arcpy.Merge_management(shps, "Chichao_Zhoushan.shp")
arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\maweizao\Ningbo"
shps = arcpy.ListFeatureClasses()
arcpy.Merge_management(shps, "Maweizhao_Ningbo.shp")
arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\maweizao\Taizhou"
shps = arcpy.ListFeatureClasses()
arcpy.Merge_management(shps, "Maweizhao_Taizhou.shp")
arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\maweizao\Wenzhou"
shps = arcpy.ListFeatureClasses()
arcpy.Merge_management(shps, "Maweizhao_Wenzhou.shp")
arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\maweizao\Zhoushan"
shps = arcpy.ListFeatureClasses()
arcpy.Merge_management(shps, "Maweizhao_Zhoushan.shp")
lyrs = arcpy.mapping.ListLayers(mxd)
fs = arcpy.ListFields(lys[0])
fs = arcpy.ListFields(lyrs[0])
fs
fs[3].name
cursor = arcpy.da.SearchCursor("Maweizhao_Zhoushan", ["area"])
for row in cursor:
    print row[0]
    
len(cursor)
cursor
sum = 0
for row in cursor:
    sum = sum + row[0]
    
sum
print sum
cursor = arcpy.da.SearchCursor("Maweizhao_Zhoushan", ["area"])
sum = 0
for row in cursor:
    sum = sum + row[0]
    
sum
cursor = arcpy.da.SearchCursor("Maweizhao_Ningbo", ["area"])
sum = 0
for row in cursor:
    sum = sum + row[0]
    
sum
cursor = arcpy.da.SearchCursor("Maweizhao_Taizhou", ["area"])
sum = 0
for row in cursor:
    sum = sum + row[0]
    
sum
cursor = arcpy.da.SearchCursor("Maweizhao_Wenzhou", ["area"])

sum = 0
for row in cursor:
    sum = sum + row[0]
    
sum
cursor = arcpy.da.SearchCursor("Chichao_Ningbo", ["area"])
sum = 0
for row in cursor:
    sum = sum + row[0]
    
sum
cursor = arcpy.da.SearchCursor("Chichao_Taizhou", ["area"])
sum = 0
for row in cursor:
    sum = sum + row[0]
    
sum
cursor = arcpy.da.SearchCursor("Chichao_Wenzhou", ["area"])
sum = 0
for row in cursor:
    sum = sum + row[0]
    
sum
cursor = arcpy.da.SearchCursor("Chichao_Zhoushan", ["area"])
sum = 0
for row in cursor:
    sum = sum + row[0]
    
sum


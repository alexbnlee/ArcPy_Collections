arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Result"
fs = arcpy.ListFiles()
len(fs)
for i in range(0, 12):
    arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Result" + "\\" + fs[i]
    shps = arcpy.ListFeatureClasses()
    arcpy.Merge_management(shps, r"D:\01-Working\2018\20180329-MergeData-zhao\Merge_Result" + "\\Merge_" + fs[i] + ".shp")
    
for i in range(5, 12):
    arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Result" + "\\" + fs[i]
    shps = arcpy.ListFeatureClasses()
    arcpy.Merge_management(shps, r"D:\01-Working\2018\20180329-MergeData-zhao\Merge_Result" + "\\Merge_" + fs[i] + ".shp")
    
for i in range(6, 12):
    arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Result" + "\\" + fs[i]
    shps = arcpy.ListFeatureClasses()
    arcpy.Merge_management(shps, r"D:\01-Working\2018\20180329-MergeData-zhao\Merge_Result" + "\\Merge_" + fs[i] + ".shp")
    
fs = arcpy.ListFiles()
for i in range(0, 12):
    arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Result" + "\\" + fs[i]
    shps = arcpy.ListFeatureClasses()
    arcpy.Merge_management(shps, r"D:\01-Working\2018\20180329-MergeData-zhao\Merge_Result" + "\\Merge_" + fs[i] + ".shp")
    
arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Result"
fs = arcpy.ListFiles()
fs
for i in range(0, 12):
    arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Result" + "\\" + fs[i]
    shps = arcpy.ListFeatureClasses()
    arcpy.Merge_management(shps, r"D:\01-Working\2018\20180329-MergeData-zhao\Merge_Result" + "\\Merge_" + fs[i] + ".shp")
    


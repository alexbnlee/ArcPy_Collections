arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Data"
folders = arcpy.ListFiles()
len(folders)
folders[0]
shps = arcpy.ListFeatureClasses()
len(shps)
arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Data" + "\\" + folders[0]
shps = arcpy.ListFeatureClasses()
len(shps)
shps
a = shps[0]
a
arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Data" + "\\" + folders[1]
shps = arcpy.ListFeatureClasses()
b = shps[0]
b
arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Data"
arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Data"
arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Data\AA-Merge"
arcpy.Merge_management(a;b,"RESP.shp")
arcpy.Merge_management(a,b,"RESP.shp")
arcpy.Merge_management([a,b],"RESP.shp")
arcpy.Merge_management([a,b],r"D:\01-Working\2018\20180329-MergeData-zhao\Data\AA-Merge\RESP.shp")
arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Data" + "\\" + folders[0]
shps = arcpy.ListFeatureClasses()
b = shps[0]
arcpy.CopyFeatures_management(b, r"D:\01-Working\2018\20180329-MergeData-zhao\Result\AANP\" + b
b
b.title
arcpy.CopyFeatures_management(b, r"D:\01-Working\2018\20180329-MergeData-zhao\Result\AANP\" + b + ".shp"
arcpy.CopyFeatures_management(b, r"D:\01-Working\2018\20180329-MergeData-zhao\Result\AANP\a.shp"

arcpy.CopyFeatures_management(shps[0], r"D:\01-Working\2018\20180329-MergeData-zhao\Result\AANP\a.shp")
arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Data"
folders = arcpy.ListFiles()
len(folders)
for i in range(0, 77):
    arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Data\" + folders[i]
    
arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Data\" + folders[0]
folders[0]
arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Data" + "\\" + folders[0]
shps = arcpy.ListFeatureClasses()
shps
for i in range(0, 77):
    arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Data" + "\\" + folders[i]
    shps = arcpy.ListFeatureClasses()
    a = shps[0]
    arcpy.CopyFeatures_management(a, r"D:\01-Working\2018\20180329-MergeData-zhao\Result" + "\\" + a + "\\" + a + i + ".shp")
    
a = shps[0]
a
b = r"D:\01-Working\2018\20180329-MergeData-zhao\Result" + "\\" + a + "\\" + a + i + ".shp"
b = r"D:\01-Working\2018\20180329-MergeData-zhao\Result" + "\\" + a + "\\" + a + str(i) + ".shp"
b
b = r"D:\01-Working\2018\20180329-MergeData-zhao\Result" + "\\" + a + "\\" + a + str(i).zfill(2) + ".shp"
b
for i in range(0, 77):
    arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Data" + "\\" + folders[i]
    shps = arcpy.ListFeatureClasses()
    a = shps[0]
    arcpy.CopyFeatures_management(a, r"D:\01-Working\2018\20180329-MergeData-zhao\Result" + "\\" + a + "\\" + a + "_" + str(i).zfill(2) + ".shp")
    
for j in range(1, 12):
    for i in range(0, 77):
        arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Data" + "\\" + folders[i]
        shps = arcpy.ListFeatureClasses()
        a = shps[j]
        arcpy.CopyFeatures_management(a, r"D:\01-Working\2018\20180329-MergeData-zhao\Result" + "\\" + a + "\\" + a + "_" + str(i).zfill(2) + ".shp")
        
for j in range(3, 12):
    for i in range(0, 77):
        arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Data" + "\\" + folders[i]
        shps = arcpy.ListFeatureClasses()
        a = shps[j]
        arcpy.CopyFeatures_management(a, r"D:\01-Working\2018\20180329-MergeData-zhao\Result" + "\\" + a + "\\" + a + "_" + str(i).zfill(2) + ".shp")
        


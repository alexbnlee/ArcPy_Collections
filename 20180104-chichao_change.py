import arcpy
arcpy.env.workspace = r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\chichao\Ningbo"
shps = arcpy.ListFeatureClasses()
for shp in shps:
    if shp.find("20170422") >= 0:
        print shp
        
for shp in shps:
    if shp.find("20170429") >= 0:
        print shp
        
for shp in shps:
    if shp.find("20170429") >= 0 && shp.find("40"):
        print shp
        
for shp in shps:
    if shp.find("20170429") >= 0 adn shp.find("40"):
        print shp
        
for shp in shps:
    if shp.find("20170429") >= 0 and shp.find("40"):
        print shp
        
for shp in shps:
    if shp.find("20170429") >= 0 and shp.find("40") >= 0:
        print shp
        
for shp in shps:
    if shp.find("20170429") >= 0:
        print shp
        
arcpy.CopyFeatures_management(shp[0], "D:/test/test.shp")
arcpy.CopyFeatures_management(shp[0], "D:/test/test.shp")
arcpy.Copy_management(shps[0], "D:/test/test.shp")
strs = ["Ningbo", "Wenzhou", "Taizhou", "Zhoushan"]
rootdir = r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\chichao\"
rootdir = "D:\\01-Working\\2017\\20171229-chen-Data_Analysis\\Results"
shps = arcpy.ListFeatureClasses(rootdir + "\\chichao\\" + strs[0] + "\\*")
len(shps)
arcpy.env.workspace = rootdir + "\\chichao\\" + strs[0]
shps = arcpy.ListFeatureClasses()
len(shps)
for str in strs:
    arcpy.env.workspace = rootdir + "\\chichao\\" + str
    shps = arcpy.ListFeatureClasses()
    len(shps)
    

for str in strs:
    arcpy.env.workspace = rootdir + "\\chichao\\" + str
    shps = arcpy.ListFeatureClasses()
    print len(shps)
    
for str in strs:
    arcpy.env.workspace = rootdir + "\\maweizao\\" + str
    shps = arcpy.ListFeatureClasses()
    print len(shps)
    
arcpy.Copy_management(shps[0], "D:/test/" + shps[0])
arcpy.env.workspace = "D:/test"
shps = arcpy.ListFeatureClasses()
for shp in shps:
    arcpy.Delete_management(shp)
    
arcpy.env.workspace = "D:\\01-Working\\2017\\20171229-chen-Data_Analysis\\Results\\Change"
for str in strs:
    os.makedir(str)
    
import os
for str in strs:
    os.makedir(str)
    
for str in strs:
    os.mkdir(str)
    
rootdir = ""D:\\01-Working\\2017\\20171229-chen-Data_Analysis\\Results\\Change\\"
rootdir = ""D:\\01-Working\\2017\\20171229-chen-Data_Analysis\\Results\\Change"
rootdir = "D:\\01-Working\\2017\\20171229-chen-Data_Analysis\\Results\\Change"
for str in strs:
    os.mkdir(rootdir + "\\" + str)
    
str_cc_change = r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\赤潮shp-change"
str_cc_change = r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\赤潮shp-change\\"
str_cc = r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\chichao\\"
str_change = r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\Change\\"
arcpy.env.workspace = str_cc
shps_cc = arcpy.ListFeatureClasses()
len(shps_cc)
str_cc = r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\chichao"
arcpy.env.workspace = str_cc
str_cc = r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\chichao"
len(shps_cc)
shps_cc = arcpy.ListFeatureClasses()
len(shps_cc)
arcpy.env.workspace = str_cc_change
shps_cc_change = arcpy.ListFeatureClasses()
len(shps_cc_change)
strs
str_cc = r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\chichao\\"
str_cc_o = r"D:\01-Working\2017\20171229-chen-Data_Analysis\赤潮shp\\"
arcpy.env.workspace = str_cc_o
shps_cc_o = arcpy.ListFeatureClasses()
len(shps_cc_o)
for shp in shps_cc_o:
    if shps_cc_change.count(shp) == 0:
        print shp
        
shps_add = []
for shp in shps_cc_o:
    if shps_cc_change.count(shp) == 0:
        shps_add.append(shp)
        
len(shps_add)
for str in strs:
    arcpy.env.workspace = str_cc + str
    shps = arcpy.ListFeatureClasses()
    for shp_add in shps_add:
        for shp in shps:
            if shp.find(shp_add) >= 0:
                print shp
                
for str in strs:
    arcpy.env.workspace = str_cc + str
    shps = arcpy.ListFeatureClasses()
    for shp_add in shps_add:
        for shp in shps:
            if shp.find(shp_add) >= 0:
                arcpy.Copy_management(shp, str_cc_change + str + "\\" +shp)
                
str_cc_change
str_cc_change = r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\Change\"
str_cc_change = r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\Change\"
str_cc_change = "D:\\01-Working\\2017\\20171229-chen-Data_Analysis\\Results\\Change\\"
str_cc_change
for str in strs:
    arcpy.env.workspace = str_cc + str
    shps = arcpy.ListFeatureClasses()
    for shp_add in shps_add:
        for shp in shps:
            if shp.find(shp_add) >= 0:
                arcpy.Copy_management(shp, str_cc_change + str + "\\" +shp)
                
for str in strs:
    arcpy.env.workspace = str_cc_change + str
    shps = arcpy.ListFeatureClasses()
    print len(shps)
    
for str in strs:
    arcpy.env.workspace = str_cc_change + str
    shps = arcpy.ListFeatureClasses()
    arcpy.Merge_management(shps, str + "_change.shp")
    
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]
lyrs = arcpy.mapping.ListLayers(df)
for i in range(0,4):
    cursor = arcpy.da.SearchCursor(lyrs[i], "area")
    sum = 0
    for row in cursor:
        sum = sum + row[0]
    print lyrs[i] + sum
    
for i in range(0,4):
    cursor = arcpy.da.SearchCursor(lyrs[i], "area")
    sum = 0
    for row in cursor:
        sum = sum + row[0]
    print lyrs[i] + str(sum)
    
import os
for i in range(0,4):
    cursor = arcpy.da.SearchCursor(lyrs[i], "area")
    sum = 0
    for row in cursor:
        sum = sum + row[0]
    print lyrs[i] + str(sum)
    
for i in range(0,3):
    cursor = arcpy.da.SearchCursor(lyrs[i], "area")
    sum = 0
    for row in cursor:
        sum = sum + row[0]
    print sum
    
for i in range(0,3):
    print lyrs[i]
    cursor = arcpy.da.SearchCursor(lyrs[i], "area")
    sum = 0
    for row in cursor:
        sum = sum + row[0]
    print sum
    
for i in range(0,4):
    print lyrs[i]
    cursor = arcpy.da.SearchCursor(lyrs[i], "area")
    sum = 0
    for row in cursor:
        sum = sum + row[0]
    print sum
    
for i in range(0,4):
    print i
    print lyrs[i]
    cursor = arcpy.da.SearchCursor(lyrs[i], "area")
    sum = 0
    for row in cursor:
        sum = sum + row[0]
    print sum
    
for i in range(0,4)
for i in range(0,4):
    print i
    
for i in range(4):
    print i
    
for i in range(0, 4, 2):
    print i
    


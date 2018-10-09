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
    


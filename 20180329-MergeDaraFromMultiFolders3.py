from arcpy_diy import *
ap.setEnvWorkspace(r"D:\01-Working\2018\20180329-MergeData-zhao\Result")
import arcpy
fs = arcpy.ListFiles()

    
arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Result" + "\\" + fs[0]
shps = arcpy.ListFeatureClasses()
arcpy.Merge_management(shps, r"D:\01-Working\2018\20180329-MergeData-zhao\Merge_Result" + "\\Merge_" + fs[0] + ".shp")

arcpy.env.workspace = r"D:\01-Working\2018\20180329-MergeData-zhao\Result" + "\\" + fs[0]
shps = arcpy.ListFeatureClasses()
arcpy.Merge_management(shps, r"D:\01-Working\2018\20180329-MergeData-zhao\Merge_Result" + "\\Merge_" + fs[0] + ".shp")



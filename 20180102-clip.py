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
>>> lyrs = arcpy.mapping.ListLayers(mxd)
Runtime error 
Traceback (most recent call last):
  File "<string>", line 1, in <module>
NameError: name 'mxd' is not defined
>>> mxd = arcpy.mapping.MapDocument("CURRENT")
>>> lyrs = arcpy.mapping.ListLayers(mxd)
>>> print len(lyrs)
70
>>> for i in range(0, 70-5):
...     arcpy.Clip_analysis(lyrs[i], "Ningbo", "cc_nb_" + lyrs[i].name + ".shp")
...     
>>> print len(lyrs)
70
>>> arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\chichao\Taizhou"
>>> for i in range(0, 70-5):
...     arcpy.Clip_analysis(lyrs[i], "Taizhou", "cc_tz_" + lyrs[i].name + ".shp")
...     
>>> arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\chichao\Wenzhou"
>>> for i in range(0, 70-5):
...     arcpy.Clip_analysis(lyrs[i], "Wenzhou", "cc_wz_" + lyrs[i].name + ".shp")
...     
>>> arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\chichao\Zhoushan"
>>> for i in range(0, 70-5):
...     arcpy.Clip_analysis(lyrs[i], "Zhoushan", "cc_zs_" + lyrs[i].name + ".shp")
...     
>>> lyrs = arcpy.mapping.ListLayers(mxd)
>>> print len(lyrs)
85
>>> arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\maweizao\Ningbo"
>>> for i in range(0, 70-5):
...     arcpy.Clip_analysis(lyrs[i], "Ningbo", "mwz_nb_" + lyrs[i].name + ".shp")
...     
Runtime error  Traceback (most recent call last):   File "<string>", line 2, in <module>   File "c:\program files (x86)\arcgis\desktop10.2\arcpy\arcpy\analysis.py", line 56, in Clip     raise e ExecuteError: ERROR 000210: Cannot create output D:\01-Working\2017\20171229-chen-Data_Analysis\Results\maweizao\Ningbo\mwz_nb_20170315_4,888.shp ERROR 000354: The name contains invalid characters Failed to execute (Clip).  
>>> for i in range(0, 85-5):
...     arcpy.Clip_analysis(lyrs[i], "Ningbo", "mwz_nb_" + lyrs[i].name + ".shp")
...     
Runtime error  Traceback (most recent call last):   File "<string>", line 2, in <module>   File "c:\program files (x86)\arcgis\desktop10.2\arcpy\arcpy\analysis.py", line 56, in Clip     raise e ExecuteError: ERROR 000210: Cannot create output D:\01-Working\2017\20171229-chen-Data_Analysis\Results\maweizao\Ningbo\mwz_nb_20170315_4,888.shp ERROR 000354: The name contains invalid characters Failed to execute (Clip).  
>>> lyrs = arcpy.mapping.ListLayers(mxd)
>>> print len(lyrs)
85
>>> for i in range(0, 85-5):
...     arcpy.Clip_analysis(lyrs[i], "Ningbo", "mwz_nb_" + lyrs[i].name + ".shp")
...     
>>> arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\maweizao\Taizhou"
>>> for i in range(0, 85-5):
...     arcpy.Clip_analysis(lyrs[i], "Taizhou", "mwz_tz_" + lyrs[i].name + ".shp")
...     
>>> arcpy.env.workspace=r"D:\01-Working\2017\20171229-chen-Data_Analysis\Results\maweizao\Wenzhou"
>>> for i in range(0, 85-5):
...     arcpy.Clip_analysis(lyrs[i], "Wenzhou", "mwz_wz_" + lyrs[i].name + ".shp")

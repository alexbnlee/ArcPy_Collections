>>> import arcpy
>>> arcpy.env.workspace = r"D:\01-Working\2017\20171229-chen-数据统计\赤潮shp"
>>> shps = arcpy.ListFeatureClasses()
>>> arcpy.Merge_management(shps, "all_chichao.shp")




#文件夹中有一个不是Polygon

>>> import arcpy
>>> arcpy.env.workspace = r"D:\01-Working\2017\20171229-chen-数据统计\马尾藻shp"
>>> shps = arcpy.ListFeatureClasses()
>>> arcpy.Merge_management(shps, "all_chichao1.shp")
>>> shpMian = arcpy.ListFeatureClasses(feature_type="Polygon")
>>> print len(shpMian)
80
>>> print len(shps)
81
>>> for shp in shps:
...     print shpMian.count(shp)
...   
20170907fg.shp
>>> shps = arcpy.ListFeatureClasses()
>>> arcpy.Merge_management(shps)
<Result 'D:\\McDelfino\\Documents\\ArcGIS\\Default.gdb\\c20170128_13_Merge'>
>>> 


>>> mxd = arcpy.mapping.MapDocument("CURRENT")
>>> lyrs = arcpy.mapping.ListLayers(mxd)
>>> lyrs
[<map layer u'Zhoushan'>, <map layer u'Wenzhou'>, <map layer u'Taizhou'>, <map layer u'Ningbo'>, <map layer u'zjwt12'>, <map layer u'all_chichao'>, <map layer u'All_maweizao'>]

>>> lyrs[5].name + "_mwz.shp"
u'all_chichao_mwz.shp'

mxd = arcpy.mapping.MapDocument("CURRENT")
len(lyrs)
lyrs = arcpy.mapping.ListLayers(mxd)
len(lyrs)
lyrs[6]
lyrs[7]
lyrs[19]
lyouts = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")
lyouts[1].text = "坐标系：WGS-84     投影：经纬度     制图时间：2018年     制图单位：国家海洋环境监测中心"
mon = 0
for i in range(7, 19):
    arcpy.mapping.UpdateLayer(df, lyrs[i], lyrs[19])
    lyrs[i].visible = False
    
for i in range(7, 19):
    mon = mon + 1
    lyrs[i].visible=True
    lyouts[2].text = "浙江及邻近海域透明度卫星遥感专题图\n2017年" + str(mon) + "月"
    arcpy.mapping.ExportToJPEG(mxd, "D:\\01-Working\\2017\\20171204-IDL_Average\\Final-SD\\" + lyrs[i].name + "_SD.jpg", resolution=300)
    lyrs[i].visible=False
    
for i in range(7, 19):
    mon = mon + 1
    lyrs[i].visible=True
    lyouts[2].text = "浙江及邻近海域透明度卫星遥感专题图\n2017年" + str(mon) + "月"
    arcpy.mapping.ExportToJPEG(mxd, "D:\\01-Working\\2017\\20171204-IDL_Average\\Final-SD\\" + lyrs[i].name + "_SD.jpg", resolution=300)
    lyrs[i].visible=False
    
mon = 0
for i in range(7, 19):
    mon = mon + 1
    lyrs[i].visible=True
    lyouts[2].text = "浙江及邻近海域透明度卫星遥感专题图\n2017年" + str(mon) + "月"
    arcpy.mapping.ExportToJPEG(mxd, "D:\\01-Working\\2017\\20171204-IDL_Average\\Final-SD\\" + lyrs[i].name + "_SD.jpg", resolution=300)
    lyrs[i].visible=False
    
lyrs = arcpy.mapping.ListLayers(mxd)
mon = 0
for i in range(7, 19):
    mon = mon + 1
    lyrs[i].visible=True
    lyouts[2].text = "浙江及邻近海域透明度卫星遥感专题图\n2017年" + str(mon) + "月"
    arcpy.mapping.ExportToJPEG(mxd, "D:\\01-Working\\2017\\20171204-IDL_Average\\Final-SD\\" + lyrs[i].name + "_SD.jpg", resolution=300)
    lyrs[i].visible=False
    


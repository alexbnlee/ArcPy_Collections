mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]
lyrs = arcpy.mapping.ListLayers(mxd)
len(lyrs)

len(lyrs)
lyrs[7]
lyrs[19]
lyrs[18]
for i in range(7, 19):
    arcpy.mapping.UpdateLayer(df, lyrs[i], lyrs[46])
    lyrs[i].visible = False
    
lyouts = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")
len(lyouts)

len(lyouts)
print lyouts[0].text
print lyouts[1].text
lyouts[1].text = "坐标系：WGS-84     投影：经纬度     制图时间：2018年     制图单位：国家海洋环境监测中心"
print lyouts[2].text
mon = 0
lyrs = arcpy.mapping.ListLayers(mxd)
for i in range(7, 19):
    mon = mon + 1
    lyrs[i].visible=True
    lyouts[2].text = "浙江及邻近海域叶绿素a卫星遥感专题图\n2017年" + str(mon) + "月"
    arcpy.mapping.ExportToJPEG(mxd, "D:\\01-Working\\2017\\20171204-IDL_Average\\Final-CHL\\" + lyrs[i].name + "_CHL.jpg", resolution=300)
    lyrs[i].visible=False
    


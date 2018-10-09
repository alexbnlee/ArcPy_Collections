ap.setEnvWorkspace(r'D:\01-Working\2018\20180201-Data_Clip\shp_clip')

lyrs = ap.getLyrs()
# 找到裁切图层
ap.findIndexByName('nhh')
# 遍历图层进行裁切
for i in range(8, 35):
    arcpy.Clip_analysis(lyrs[i], lyrs[35], 'clip_'+lyrs[i].name+'.shp')
    


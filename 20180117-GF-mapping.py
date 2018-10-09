len(lyrs)
lyrs[20]
lyrs[30]
lyrs[36]
lyrs[20].name
a = lyrs[20].name
a
a.find('2017')
a[4+4, 2]
a[4+4:4+4+2]
index = (lyrs[20].name).find('2017')
mon = (lyrs[20].name)[index+4, index+6]
mon = (lyrs[20].name)[index+4:index+6]
day = (lyrs[20].name)[index+6:index+8]
mon
day
ap.setEnvWorkspace(r"D:\01-业务工作\2017\20171228-高分专题图\专题图")
los = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")
print los[2].text
a = "004"
a.lstrip('0')
los[2].text = "浙江及邻近海域悬浮泥沙卫星遥感专题图\n2017年"+str(mon)+"月"+str(day).lstrip('0')+"日"
arcpy.RefreshActiveView()
df.extent = lyrs[20].getExtent()
for i in range(20, 37):
    print lyrs[i]
    
for i in range(20, 37):
    lyrs[i].visible = True
    s = lyrs[i].name
    index = s.find('2017')
    mon = s[index+4:index+6]
    day = s[index+6:index+8]
    los[2].text = "浙江及邻近海域悬浮泥沙卫星遥感专题图\n2017年"+str(mon)+"月"+str(day).lstrip('0')+"日"
    df.extent = lyrs[20].getExtent()
    arcpy.RefreshActiveView()
    mxd.saveACopy(arcpy.env.workspace + "\\SSC_2017" + str(mon) + str(day) + ".mxd")
    ap.exportToJpeg("SSC_2017" + str(mon) + str(day) + ".jpg")
    lyrs[i].visible = False
    
lyrs = ap.getLyrs()
for i in range(20, 37):
    print lyrs[i]
    
for i in range(20, 36):
    lyrs[i].visible = True
    s = lyrs[i].name
    index = s.find('2017')
    mon = s[index+4:index+6]
    day = s[index+6:index+8]
    los[2].text = "浙江及邻近海域悬浮泥沙卫星遥感专题图\n2017年"+str(mon).lstrip('0')+"月"+str(day).lstrip('0')+"日"
    df.extent = lyrs[i].getExtent()
    arcpy.RefreshActiveView()
    mxd.saveACopy(arcpy.env.workspace + "\\SSC_2017" + str(mon) + str(day) + ".mxd")
    ap.exportToJpeg("SSC_2017" + str(mon) + str(day) + ".jpg")
    lyrs[i].visible = False
    


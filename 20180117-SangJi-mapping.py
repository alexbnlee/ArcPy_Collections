from arcpy_diy import *
mxd = ap.getCurrentMxd()
df = ap.getDataFrame_0()
lyrs = ap.getLyrs()

loys = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT")

for i in range(0, 10):
    lyrs[i].visible = True
    lyrs[i+30].visible = True
    s = lyrs[i+30].name
    ih = s.find('-')
    iat = s.rfind('-')
    sd = s[ih-2:ih]
    sh = s[ih+1:iat]
    sat = s[iat+1]
    if sat=="A":
        loys[0].text = "卫星/传感器：MODIS-AQUA\n成像时间：2018年1月"+str(sd)+"日 "+str(sh)+"时\n制作单位：国家海洋环境监测中心"  
    else:
        loys[0].text = "卫星/传感器：MODIS-TERRA\n成像时间：2018年1月"+str(sd)+"日 "+str(sh)+"时\n制作单位：国家海洋环境监测中心"
    arcpy.RefreshActiveView()
    mxd.saveACopy(arcpy.env.workspace + "\\point-" + str(i+6).zfill(2) + ".mxd")
    ap.exportToJpeg("point-" + str(i+6).zfill(2) + ".jpg")
    lyrs[i].visible = False
    lyrs[i+30].visible = False
    lyrs[0].visible = True
    


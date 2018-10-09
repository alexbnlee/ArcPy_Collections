# 取字符串前7个字符
for i in range(0, len(fsn)):
    fsn[i] = fsn[i][0:7]

# 去除重复字符串
fsnn = []
for f in fsn:
    if f not in fsnn:
        fsnn.append(f)

# 建立函数，将相同名字的合并一起
def get_mon_merge_shp(string):
    arcpy.Merge_management(get_day_list(string), 'mon_'+string+'.shp')
    
lyrs = ap.getLyrs()
for f in fsnn:
    get_mon_merge_shp(f)
    


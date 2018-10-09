from arcpy_diy import *
mxd = ap.getCurrentMxd()
df = ap.getDataFrame_0()
lyrs = ap.getLyrs()
ap.setEnvWorkspace('D:\01-Working\2018\20180201-Data_Clip\shp_day')

# 定义函数，获取指定字符串的图层
def get_day_list(string):
    list1 = []
    for lyr in lyrs:
        if lyr.name.find(string) >= 0:
            list1.append(lyr)
    return list1

# 定义函数，将指定字符串的图层进行合并    
def get_day_merge_shp(string):
    arcpy.Merge_management(get_day_list(string), 'day'+string+'.shp')

# 获取文件夹内所有文件名
fs = os.listdir(r'D:\01-Working\2018\20180201-Data_Clip\fanwei')

# 对文件名进行截取前9个字符，获取年月日，例如“2016_1028”
for i in range(0, 525):
    fs[i] = fs[i][0:9]

# 将重复的字符串删除 
fsn = []
for f in fs:
    if f not in fsn:
        fsn.append(f)
        
# 对于没有重复的数据进行遍历，调用merge函数
for f in fsn:
    get_day_merge_shp(f)
    


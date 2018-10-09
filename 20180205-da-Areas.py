
# 通过名称获取日期
for i in range(0, 22):
    print (lyrs[i].name)[13:22]

# 打印统计的面积值
for i in range(0, 22):
    sum = 0
    cursor = arcpy.da.SearchCursor(lyrs[i], "F_AREA")
    for row in cursor:
        sum = sum + row[0]
    print sum/1000000
    


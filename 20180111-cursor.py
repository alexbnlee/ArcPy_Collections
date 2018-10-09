mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]
lyrs = arcpy.mapping.ListLayers(mxd)

lyr = lyrs[0]

# 内容需要用单引号引起来

# for 循环
cursor = arcpy.SearchCursor(lyr, "NAME='辽宁省'")
for row in cursor:
    print row.getValue("ID")
  
# while 循环，需要得到 row，然后判断 row 是否存在  
cursor = arcpy.SearchCursor(lyr, "NAME='辽宁省'")
row = cursor.next()
while row:
    print row.getValue("ID")
    row = cursor.next()
    
cursor = arcpy.UpdateCursor(lyr)
field1 = "BOU2_4M_"
field2 = "BOU2_4M_ID"
for row in cursor:
    row.setValue(field1, row.getValue(field2)*2)
    cursor.updateRow(row)
    
cursor = arcpy.UpdateCursor(lyr)
row = cursor.next()
while row:
    row.setValue(field1, row.getValue(field2)/2)
    cursor.updateRow(row)
    row = cursor.next()
    

